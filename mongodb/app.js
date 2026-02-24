/**
 * MongoDB Learning App
 * Express server with MongoDB CRUD operations
 * Run with: node app.js
 * Access at: http://localhost:3000
 * npm run dev-mongo # runs `npx nodemon ./mongodb/app.js`
 */

const express = require('express');
const { MongoClient, ObjectId } = require('mongodb');

const app = express();
const PORT = 3000;

const MONGO_URI = 'mongodb://localhost:27017';
const DB_NAME = 'learning_db';

let db;

// Middleware
app.use(express.json());

// MongoDB Connection
async function connectMongoDB() {
  try {
    const client = new MongoClient(MONGO_URI);
    await client.connect();
    db = client.db(DB_NAME);
    console.log('✅ Connected to MongoDB');
    return client;
  } catch (error) {
    console.error('❌ MongoDB connection failed:', error);
    process.exit(1);
  }
}

// ============================================
// STUDENTS ROUTES
// ============================================

// GET all students
app.get('/students', async (_req, res) => {
  try {
    const students = await db.collection('students').find().toArray();

    res.json({
      success: true,
      count: students.length,
      data: students,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: error.message,
    });
  }
});

// GET student by ID
app.get('/students/:id', async (req, res) => {
  try {
    const id = parseInt(req.params.id);
    const student = await db.collection('students').findOne({ _id: id });

    if (!student) {
      return res.status(404).json({
        success: false,
        error: 'Student not found',
      });
    }

    res.json({
      success: true,
      data: student,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: error.message,
    });
  }
});

// GET students by major
app.get('/students/major/:major', async (req, res) => {
  try {
    const students = await db
      .collection('students')
      .find({ major: req.params.major })
      .toArray();

    res.json({
      success: true,
      count: students.length,
      data: students,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: error.message,
    });
  }
});

// POST create new student
app.post('/students', async (req, res) => {
  try {
    const { name, age, email, major, gpa } = req.body;

    // Validation
    if (!name || !age || !email || !major || gpa === undefined) {
      return res.status(400).json({
        success: false,
        error: 'Missing required fields: name, age, email, major, gpa',
      });
    }

    // Get next ID
    const lastStudent = await db
      .collection('students')
      .find()
      .sort({ _id: -1 })
      .limit(1)
      .toArray();

    const nextId = lastStudent.length > 0 ? lastStudent[0]._id + 1 : 1;

    const newStudent = {
      _id: nextId,
      name,
      age,
      email,
      major,
      gpa,
      enrollmentDate: new Date(),
      active: true,
      courses: [],
    };

    const result = await db.collection('students').insertOne(newStudent);

    res.status(201).json({
      success: true,
      message: 'Student created',
      data: { _id: result.insertedId, ...newStudent },
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: error.message,
    });
  }
});

// PUT update student
app.put('/students/:id', async (req, res) => {
  try {
    const id = parseInt(req.params.id);
    const updates = req.body;

    const result = await db
      .collection('students')
      .updateOne({ _id: id }, { $set: updates });

    if (result.matchedCount === 0) {
      return res.status(404).json({
        success: false,
        error: 'Student not found',
      });
    }

    res.json({
      success: true,
      message: 'Student updated',
      modifiedCount: result.modifiedCount,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: error.message,
    });
  }
});

// DELETE student
app.delete('/students/:id', async (req, res) => {
  try {
    const id = parseInt(req.params.id);

    const result = await db.collection('students').deleteOne({ _id: id });

    if (result.deletedCount === 0) {
      return res.status(404).json({
        success: false,
        error: 'Student not found',
      });
    }

    res.json({
      success: true,
      message: 'Student deleted',
      deletedCount: result.deletedCount,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: error.message,
    });
  }
});

// ============================================
// COURSES ROUTES
// ============================================

// GET all courses
app.get('/courses', async (req, res) => {
  try {
    const courses = await db.collection('courses').find().toArray();

    res.json({
      success: true,
      count: courses.length,
      data: courses,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: error.message,
    });
  }
});

// GET course by ID
app.get('/courses/:id', async (req, res) => {
  try {
    const course = await db
      .collection('courses')
      .findOne({ _id: req.params.id });

    if (!course) {
      return res.status(404).json({
        success: false,
        error: 'Course not found',
      });
    }

    res.json({
      success: true,
      data: course,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: error.message,
    });
  }
});

// ============================================
// ANALYTICS ROUTES
// ============================================

// GET students by GPA (top performers)
// http://localhost:3000/analytics/top-students?limit=3
app.get('/analytics/top-students', async (req, res) => {
  try {
    const limit = parseInt(req.query.limit) || 5;

    const topStudents = await db
      .collection('students')
      .find()
      .sort({ gpa: -1 })
      .limit(limit)
      .toArray();

    res.json({
      success: true,
      data: topStudents,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: error.message,
    });
  }
});

// GET students grouped by major
app.get('/analytics/by-major', async (req, res) => {
  try {
    const majorStats = await db
      .collection('students')
      .aggregate([
        {
          $group: {
            _id: '$major',
            count: { $sum: 1 },
            avgGpa: { $avg: '$gpa' },
            maxGpa: { $max: '$gpa' },
            minGpa: { $min: '$gpa' },
          },
        },
        { $sort: { count: -1, avgGpa: -1 } },
      ])
      .toArray();

    res.json({
      success: true,
      data: majorStats,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: error.message,
    });
  }
});

// GET course enrollment stats
// .project() is equivalent to SELECT in SQL, fields to include or exclude in the result set.
// In this case, we are including the course details
// number 1 means turn this field on and number 0 means tun this field off
// calculating the available seats by subtracting currentEnrollment from maxCapacity.
app.get('/analytics/courses', async (req, res) => {
  try {
    const courseStats = await db
      .collection('courses')
      .find()
      .project({
        _id: 1,
        name: 1,
        department: 1,
        enrolledStudents: 1,
        currentEnrollment: 1,
        maxCapacity: 1,
        availableSeats: {
          $subtract: ['$maxCapacity', '$currentEnrollment'],
        },
      })
      .toArray();

    res.json({
      success: true,
      data: courseStats,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: error.message,
    });
  }
});

// ============================================
// ROOT ROUTE
// ============================================

app.get('/', (req, res) => {
  res.json({
    message: '🎓 MongoDB Learning API',
    version: '1.0.0',
    endpoints: {
      students: {
        'GET /students': 'Get all students',
        'GET /students/:id': 'Get student by ID',
        'GET /students/major/:major': 'Get students by major',
        'POST /students': 'Create new student',
        'PUT /students/:id': 'Update student',
        'DELETE /students/:id': 'Delete student',
      },
      courses: {
        'GET /courses': 'Get all courses',
        'GET /courses/:id': 'Get course by ID',
      },
      analytics: {
        'GET /analytics/top-students': 'Get top students by GPA',
        'GET /analytics/by-major': 'Get statistics by major',
        'GET /analytics/courses': 'Get course enrollment stats',
      },
    },
  });
});

// ============================================
// ERROR HANDLING
// ============================================

app.use((req, res) => {
  res.status(404).json({
    success: false,
    error: 'Endpoint not found',
  });
});

// ============================================
// SERVER START
// ============================================

async function startServer() {
  try {
    await connectMongoDB();

    app.listen(PORT, () => {
      console.log(`\n🚀 Server running at http://localhost:${PORT}`);
      console.log(`\n📚 API Documentation:`);
      console.log(`   GET http://localhost:${PORT}`);
      console.log(`\n💡 Try these endpoints:`);
      console.log(`   GET http://localhost:${PORT}/students`);
      console.log(`   GET http://localhost:${PORT}/courses`);
      console.log(`   GET http://localhost:${PORT}/analytics/by-major`);
      console.log(`   GET http://localhost:${PORT}/analytics/top-students`);
      console.log(`\n⏹️  Press Ctrl+C to stop the server\n`);
    });
  } catch (error) {
    console.error('Failed to start server:', error);
    process.exit(1);
  }
}

startServer();
