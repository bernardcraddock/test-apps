/**
 * MongoDB Sample Data Script
 * Populates the learning_db database with student and course data
 * Run with: node sample-data.js
 */

const { MongoClient } = require('mongodb');

const MONGO_URI = 'mongodb://localhost:27017';
const DB_NAME = 'learning_db';

async function main() {
  const client = new MongoClient(MONGO_URI);

  try {
    // Connect to MongoDB
    await client.connect();
    console.log('✅ Connected to MongoDB');

    const db = client.db(DB_NAME);

    // Drop existing collections to start fresh
    console.log('\n📋 Clearing existing collections...');
    try {
      await db.collection('students').drop();
      console.log('  ✓ Dropped students collection');
    } catch (e) {
      // Collection doesn't exist, that's fine
    }

    try {
      await db.collection('courses').drop();
      console.log('  ✓ Dropped courses collection');
    } catch (e) {
      // Collection doesn't exist, that's fine
    }

    // Create collections with validation
    console.log('\n🔧 Creating collections...');
    await db.createCollection('students');
    await db.createCollection('courses');
    console.log('  ✓ Collections created');

    // Insert sample students
    console.log('\n👥 Inserting student data...');
    const studentResult = await db.collection('students').insertMany([
      {
        _id: 1,
        name: 'Alice Johnson',
        age: 25,
        email: 'alice@example.com',
        major: 'Computer Science',
        gpa: 3.8,
        enrollmentDate: new Date('2023-09-01'),
        active: true,
        courses: ['CS101', 'CS201', 'MATH101'],
      },
      {
        _id: 2,
        name: 'Bob Smith',
        age: 23,
        email: 'bob@example.com',
        major: 'Mathematics',
        gpa: 3.6,
        enrollmentDate: new Date('2023-09-01'),
        active: true,
        courses: ['MATH101', 'MATH201', 'CS101'],
      },
      {
        _id: 3,
        name: 'Carol White',
        age: 24,
        email: 'carol@example.com',
        major: 'Physics',
        gpa: 3.9,
        enrollmentDate: new Date('2023-09-15'),
        active: true,
        courses: ['PHYS101', 'PHYS201', 'MATH101'],
      },
      {
        _id: 4,
        name: 'David Brown',
        age: 25,
        email: 'david@example.com',
        major: 'Computer Science',
        gpa: 3.5,
        enrollmentDate: new Date('2023-08-20'),
        active: true,
        courses: ['CS101', 'CS301'],
      },
      {
        _id: 5,
        name: 'Eve Davis',
        age: 22,
        email: 'eve@example.com',
        major: 'Chemistry',
        gpa: 3.7,
        enrollmentDate: new Date('2024-01-15'),
        active: true,
        courses: ['CHEM101', 'CHEM201'],
      },
      {
        _id: 6,
        name: 'Frank Miller',
        age: 26,
        email: 'frank@example.com',
        major: 'Computer Science',
        gpa: 3.4,
        enrollmentDate: new Date('2023-08-20'),
        active: false,
        courses: ['CS101', 'CS201'],
      },
      {
        _id: 7,
        name: 'Grace Lee',
        age: 23,
        email: 'grace@example.com',
        major: 'Physics',
        gpa: 3.8,
        enrollmentDate: new Date('2023-09-10'),
        active: true,
        courses: ['PHYS101', 'MATH101'],
      },
      {
        _id: 8,
        name: 'Henry Wilson',
        age: 24,
        email: 'henry@example.com',
        major: 'Mathematics',
        gpa: 3.2,
        enrollmentDate: new Date('2023-10-01'),
        active: true,
        courses: ['MATH101', 'CS101'],
      },
    ]);
    console.log(`  ✓ Inserted ${studentResult.insertedCount} students`);

    // Insert sample courses
    console.log('\n📚 Inserting course data...');
    const courseResult = await db.collection('courses').insertMany([
      {
        _id: 'CS101',
        name: 'Introduction to Computer Science',
        department: 'Computer Science',
        credits: 3,
        instructor: 'Dr. Anderson',
        enrolledStudents: [1, 2, 4, 6, 8],
        maxCapacity: 30,
        currentEnrollment: 5,
        semester: 'Fall 2023',
      },
      {
        _id: 'CS201',
        name: 'Data Structures',
        department: 'Computer Science',
        credits: 4,
        instructor: 'Dr. Chen',
        enrolledStudents: [1, 4, 6],
        maxCapacity: 25,
        currentEnrollment: 3,
        semester: 'Fall 2023',
      },
      {
        _id: 'CS301',
        name: 'Algorithms',
        department: 'Computer Science',
        credits: 4,
        instructor: 'Dr. Martinez',
        enrolledStudents: [4],
        maxCapacity: 20,
        currentEnrollment: 1,
        semester: 'Spring 2024',
      },
      {
        _id: 'MATH101',
        name: 'Calculus I',
        department: 'Mathematics',
        credits: 4,
        instructor: 'Dr. Thompson',
        enrolledStudents: [2, 3, 7, 8],
        maxCapacity: 35,
        currentEnrollment: 4,
        semester: 'Fall 2023',
      },
      {
        _id: 'MATH201',
        name: 'Linear Algebra',
        department: 'Mathematics',
        credits: 3,
        instructor: 'Dr. Patel',
        enrolledStudents: [2],
        maxCapacity: 30,
        currentEnrollment: 1,
        semester: 'Spring 2024',
      },
      {
        _id: 'PHYS101',
        name: 'Physics I: Mechanics',
        department: 'Physics',
        credits: 4,
        instructor: 'Dr. Garcia',
        enrolledStudents: [3, 7],
        maxCapacity: 25,
        currentEnrollment: 2,
        semester: 'Fall 2023',
      },
      {
        _id: 'PHYS201',
        name: 'Physics II: Electricity & Magnetism',
        department: 'Physics',
        credits: 4,
        instructor: 'Dr. Rodriguez',
        enrolledStudents: [3],
        maxCapacity: 25,
        currentEnrollment: 1,
        semester: 'Spring 2024',
      },
      {
        _id: 'CHEM101',
        name: 'General Chemistry',
        department: 'Chemistry',
        credits: 4,
        instructor: 'Dr. Kim',
        enrolledStudents: [5],
        maxCapacity: 30,
        currentEnrollment: 1,
        semester: 'Spring 2024',
      },
      {
        _id: 'CHEM201',
        name: 'Organic Chemistry',
        department: 'Chemistry',
        credits: 4,
        instructor: 'Dr. Brown',
        enrolledStudents: [5],
        maxCapacity: 25,
        currentEnrollment: 1,
        semester: 'Spring 2024',
      },
    ]);
    console.log(`  ✓ Inserted ${courseResult.insertedCount} courses`);

    // Create indexes for faster queries
    console.log('\n⚡ Creating indexes...');
    await db.collection('students').createIndex({ email: 1 });
    await db.collection('students').createIndex({ major: 1 });
    await db.collection('students').createIndex({ gpa: -1 });
    console.log('  ✓ Indexes created');

    // Display summary
    console.log('\n📊 Database Summary:');
    const studentCount = await db.collection('students').countDocuments();
    const courseCount = await db.collection('courses').countDocuments();
    console.log(`  • Students: ${studentCount}`);
    console.log(`  • Courses: ${courseCount}`);

    // Show sample data
    console.log('\n📋 Sample Students:');
    const students = await db.collection('students').find().limit(3).toArray();
    students.forEach((student) => {
      console.log(
        `  • ${student.name} (${student.major}) - GPA: ${student.gpa}`,
      );
    });

    console.log('\n✅ Data population complete!');
    console.log('\n💡 Next: Try these queries in mongosh:');
    console.log('  use learning_db');
    console.log('  db.students.find()'); // All students
    console.log('  db.students.find({ major: "Computer Science" })'); // Only Computer Science majors
    console.log('  db.students.find().sort({ gpa: -1 }).limit(3)'); // Top 3 students by GPA
    console.log(
      '  db.students.aggregate([{ $group: { _id: "$major", count: { $sum: 1 } } }])',
    ); // Count students by major
  } catch (error) {
    console.error('❌ Error:', error.message);
    process.exit(1);
  } finally {
    await client.close();
    console.log('\n✓ Disconnected from MongoDB');
  }
}

main();
