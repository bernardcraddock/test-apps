# MongoDB Advanced Queries Guide

This guide contains practical MongoDB queries you can test in `mongosh` shell. Copy and paste examples directly into your terminal.

---

## 🏁 Getting Started

```javascript
// Start mongosh
mongosh

// Create/switch to a database
use learning_db

// You're now ready to run queries below!
```

---

## 📝 CREATE Operations (Insert)

### Insert a Single Document
```javascript
db.students.insertOne({
  _id: 1,
  name: "Alice Johnson",
  age: 25,
  email: "alice@example.com",
  major: "Computer Science",
  gpa: 3.8,
  enrollmentDate: new Date("2023-09-01")
})
```

### Insert Multiple Documents
```javascript
db.students.insertMany([
  {
    _id: 2,
    name: "Bob Smith",
    age: 23,
    email: "bob@example.com",
    major: "Mathematics",
    gpa: 3.6,
    enrollmentDate: new Date("2023-09-01")
  },
  {
    _id: 3,
    name: "Carol White",
    age: 24,
    email: "carol@example.com",
    major: "Physics",
    gpa: 3.9,
    enrollmentDate: new Date("2023-09-15")
  },
  {
    _id: 4,
    name: "David Brown",
    age: 25,
    email: "david@example.com",
    major: "Computer Science",
    gpa: 3.5,
    enrollmentDate: new Date("2023-08-20")
  }
])
```

### Insert with Timestamp
```javascript
db.students.insertOne({
  name: "Eve Davis",
  major: "Chemistry",
  createdAt: new Date(),
  active: true
})
```

---

## 🔍 READ Operations (Find/Query)

### Find All Documents
```javascript
db.students.find()

// More readable format
db.students.find().pretty()
```

### Find with Equality Filter
```javascript
// Find all Computer Science students
db.students.find({ major: "Computer Science" })

// Find specific student by name
db.students.find({ name: "Alice Johnson" })

// Find by ID
db.students.find({ _id: 1 })
```

### Find with Comparison Operators

```javascript
// Greater than ($gt)
db.students.find({ age: { $gt: 23 } })  // Age greater than 23

// Greater than or equal ($gte)
db.students.find({ gpa: { $gte: 3.8 } })  // GPA 3.8 and above

// Less than ($lt)
db.students.find({ age: { $lt: 25 } })  // Age less than 25

// Less than or equal ($lte)
db.students.find({ gpa: { $lte: 3.6 } })  // GPA 3.6 and below

// Not equal ($ne)
db.students.find({ major: { $ne: "Computer Science" } })  // Not CS students

// Equal to any value in array ($in)
db.students.find({ major: { $in: ["CS", "Computer Science", "Mathematics"] } })

// Not in array ($nin)
db.students.find({ major: { $nin: ["Physics", "Chemistry"] } })
```

### Find with Logical Operators

```javascript
// AND (implicit - multiple conditions)
db.students.find({ major: "Computer Science", age: { $gt: 23 } })

// AND (explicit $and)
db.students.find({
  $and: [
    { major: "Computer Science" },
    { gpa: { $gte: 3.5 } }
  ]
})

// OR ($or)
db.students.find({
  $or: [
    { major: "Computer Science" },
    { major: "Mathematics" }
  ]
})

// AND with OR
db.students.find({
  $and: [
    { $or: [{ major: "CS" }, { major: "Computer Science" }] },
    { gpa: { $gte: 3.5 } }
  ]
})
```

### Find with String Patterns

```javascript
// Starts with ($regex)
db.students.find({ name: { $regex: "^Alice" } })

// Contains
db.students.find({ email: { $regex: "example" } })

// Case-insensitive
db.students.find({ major: { $regex: "computer", $options: "i" } })
```

### Find with Array Conditions

```javascript
// Document has array field with value
db.courses.find({ students: 1 })

// Array contains any value from list ($in)
db.courses.find({ students: { $in: [1, 2] } })

// Array contains all values ($all)
db.courses.find({ students: { $all: [1, 2] } })

// Array size
db.courses.find({ students: { $size: 3 } })
```

### Projection (Select Specific Fields)

```javascript
// Return only name and major (exclude others)
db.students.find({}, { name: 1, major: 1 })

// Return all except GPA
db.students.find({}, { gpa: 0 })

// Rename field in result
db.students.find({}, { name: 1, major: 1, _id: 0 })

// Computed field ($project used in aggregation - see below)
```

### Sorting, Limiting, and Pagination

```javascript
// Sort ascending
db.students.find().sort({ name: 1 })

// Sort descending
db.students.find().sort({ gpa: -1 })

// Sort by multiple fields
db.students.find().sort({ major: 1, gpa: -1 })

// Limit results
db.students.find().limit(2)

// Skip and limit (pagination)
db.students.find().skip(1).limit(2)  // Skip first 1, get next 2

// Count documents
db.students.countDocuments()
db.students.countDocuments({ major: "Computer Science" })

// Find first matching
db.students.findOne({ major: "Physics" })
```

---

## ✏️ UPDATE Operations

### Update One Document

```javascript
// Replace single field
db.students.updateOne(
  { _id: 1 },
  { $set: { age: 26 } }
)

// Update multiple fields
db.students.updateOne(
  { name: "Alice Johnson" },
  { $set: { gpa: 3.9, age: 26 } }
)

// Increment a field
db.students.updateOne(
  { _id: 1 },
  { $inc: { age: 1 } }  // Add 1 to age
)

// Multiply a field
db.students.updateOne(
  { _id: 1 },
  { $mul: { gpa: 1.05 } }  // Multiply GPA by 1.05
)

// Add to array
db.students.updateOne(
  { _id: 1 },
  { $push: { courses: "CS101" } }  // Add course to courses array
)

// Add to array if not exists
db.students.updateOne(
  { _id: 1 },
  { $addToSet: { courses: "CS101" } }  // Only add if not already there
)

// Remove from array
db.students.updateOne(
  { _id: 1 },
  { $pull: { courses: "CS101" } }  // Remove course from array
)

// Set field only if document doesn't have it
db.students.updateOne(
  { _id: 1 },
  { $setOnInsert: { enrollmentDate: new Date() } }
)
```

### Update Multiple Documents

```javascript
// Update all CS students
db.students.updateMany(
  { major: "Computer Science" },
  { $set: { department: "Engineering" } }
)

// Increment all students' ages by 1
db.students.updateMany(
  {},
  { $inc: { age: 1 } }
)

// Update with conditional
db.students.updateMany(
  { gpa: { $gte: 3.8 } },
  { $set: { honorStatus: "Dean's List" } }
)
```

### Replace Entire Document

```javascript
// Replace entire document (all fields)
db.students.replaceOne(
  { _id: 1 },
  {
    name: "Alice Johnson",
    age: 26,
    major: "Computer Science",
    gpa: 3.95,
    active: true
  }
)
```

---

## 🗑️ DELETE Operations

### Delete One Document

```javascript
// Delete by ID
db.students.deleteOne({ _id: 1 })

// Delete first matching document
db.students.deleteOne({ major: "Physics" })
```

### Delete Multiple Documents

```javascript
// Delete all CS students
db.students.deleteMany({ major: "Computer Science" })

// Delete all with low GPA
db.students.deleteMany({ gpa: { $lt: 2.0 } })

// Delete all documents
db.students.deleteMany({})
```

---

## 📊 AGGREGATION Pipelines

Aggregation is MongoDB's powerful data processing engine. Queries flow through stages like a pipeline.

### Basic Aggregation

```javascript
// Match stage (like WHERE in SQL)
db.students.aggregate([
  { $match: { major: "Computer Science" } }
])

// Group and count
db.students.aggregate([
  {
    $group: {
      _id: "$major",  // Group by major field
      count: { $sum: 1 }  // Count documents
    }
  }
])

// Sort results
db.students.aggregate([
  {
    $group: {
      _id: "$major",
      count: { $sum: 1 },
      avgGpa: { $avg: "$gpa" }
    }
  },
  { $sort: { count: -1 } }  // Sort by count descending
])
```

### Multi-Stage Aggregation

```javascript
// Complex pipeline: Filter -> Group -> Sort -> Project
db.students.aggregate([
  // Stage 1: Filter students with GPA >= 3.5
  { $match: { gpa: { $gte: 3.5 } } },
  
  // Stage 2: Group by major, calculate stats
  {
    $group: {
      _id: "$major",
      count: { $sum: 1 },
      avgGpa: { $avg: "$gpa" },
      maxAge: { $max: "$age" },
      minAge: { $min: "$age" }
    }
  },
  
  // Stage 3: Sort by count descending
  { $sort: { count: -1 } },
  
  // Stage 4: Rename fields for readability
  {
    $project: {
      major: "$_id",
      studentCount: "$count",
      averageGpa: "$avgGpa",
      oldestStudent: "$maxAge",
      youngestStudent: "$minAge",
      _id: 0  // Hide the _id field
    }
  }
])
```

### Aggregation with Arrays

```javascript
// Create new array from grouped data
db.students.aggregate([
  {
    $group: {
      _id: "$major",
      students: { $push: "$name" },  // Create array of names
      count: { $sum: 1 }
    }
  }
])

// Unwind array (flatten)
db.students.aggregate([
  { $match: { major: "Computer Science" } },
  {
    $group: {
      _id: null,
      names: { $push: "$name" }
    }
  },
  { $unwind: "$names" }  // Split array back into separate documents
])
```

### Aggregation with Lookups (Like SQL JOIN)

```javascript
// Assuming you have a courses collection
// Find all courses and their enrolled students

db.courses.aggregate([
  {
    $lookup: {
      from: "students",           // Join with students collection
      localField: "studentIds",   // Field in courses collection
      foreignField: "_id",        // Field in students collection
      as: "enrolledStudents"      // Name of result array
    }
  },
  { $limit: 5 }  // Show first 5 results
])
```

---

## 🔧 Useful Operators Reference

### Comparison
- `$eq` - Equal
- `$ne` - Not equal
- `$gt` - Greater than
- `$gte` - Greater than or equal
- `$lt` - Less than
- `$lte` - Less than or equal
- `$in` - In array
- `$nin` - Not in array

### Logical
- `$and` - AND condition
- `$or` - OR condition
- `$not` - NOT condition
- `$nor` - NOR condition

### Array
- `$all` - All elements in array
- `$elemMatch` - At least one element matches
- `$size` - Array size
- `$push` - Add to array
- `$pop` - Remove from array
- `$pull` - Remove matching from array
- `$addToSet` - Add to set (unique values only)

### Update
- `$set` - Set field value
- `$unset` - Remove field
- `$inc` - Increment field
- `$mul` - Multiply field
- `$min` - Update if new value is less
- `$max` - Update if new value is greater

### Aggregation
- `$match` - Filter documents
- `$group` - Group and aggregate
- `$sort` - Sort documents
- `$limit` - Limit number of documents
- `$skip` - Skip documents
- `$project` - Reshape documents
- `$unwind` - Deconstruct array
- `$lookup` - Join collections
- `$sum`, `$avg`, `$min`, `$max`, `$count` - Aggregation functions

---

## 💡 Real-World Query Examples

### Find Top Performing Students
```javascript
db.students.find(
  { gpa: { $gte: 3.7 } },
  { name: 1, gpa: 1, major: 1 }
).sort({ gpa: -1 })
```

### Find Students by Enrollment Date Range
```javascript
db.students.find({
  enrollmentDate: {
    $gte: new Date("2023-01-01"),
    $lt: new Date("2023-12-31")
  }
})
```

### Find and Update Student Status
```javascript
db.students.updateOne(
  { _id: 1 },
  {
    $set: {
      lastModified: new Date(),
      status: "active"
    }
  }
)
```

### Bulk Operations
```javascript
// Update multiple documents in one operation
db.students.bulkWrite([
  {
    updateOne: {
      filter: { major: "Computer Science" },
      update: { $set: { department: "Engineering" } }
    }
  },
  {
    updateOne: {
      filter: { major: "Mathematics" },
      update: { $set: { department: "Science" } }
    }
  }
])
```

---

## 🎯 Practice Exercises

Try these on your own:

1. Find all students older than 24
2. Find students with GPA between 3.5 and 3.8
3. Count how many students are in each major
4. Find the student with the highest GPA
5. Update all students to have a `lastReviewed` field set to today's date
6. Delete all students with a GPA below 2.0
7. Group students by major and show average GPA per major
8. Find all Physics and Chemistry students, sorted by name

---

## 📚 Next Steps

✅ You've learned queries!
📊 Ready to populate with real data? → Move to **Step 3: Sample Data Script** (`sample-data.js`)

Let me know when you're ready for Step 3! 🚀
