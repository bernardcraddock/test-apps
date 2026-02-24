# MongoDB Learning Workspace

## What is MongoDB?

MongoDB is a **NoSQL (non-relational) database** that stores data in JSON-like documents instead of traditional tables. Key features:

- **Document-oriented**: Data stored as flexible JSON documents
- **No fixed schema**: Each document can have different structures
- **Scalable**: Built for horizontal scaling across multiple servers
- **Query-rich**: Powerful query language similar to SQL but more flexible
- **Aggregation**: Complex data processing pipelines

### MongoDB vs SQL (Quick Comparison)

| SQL         | MongoDB     |
| ----------- | ----------- |
| Database    | Database    |
| Table       | Collection  |
| Row         | Document    |
| Column      | Field       |
| Primary Key | `_id` field |

---

## Setup Instructions (macOS)

### ✅ Already Installed?

If you ran:

```bash
brew tap mongodb/brew
brew install mongodb-community
```

You're ready! Skip to **Starting MongoDB**.

### Starting MongoDB

```bash
# Start as background service
brew services start mongodb-community

# Verify it's running
brew services list
```

### Connecting to MongoDB

```bash
# Open MongoDB shell
mongosh

# You should see:
# >
```

### Stopping MongoDB

```bash
# Stop the service
brew services stop mongodb-community
```

---

## Local Connection Details

```
Host: localhost (127.0.0.1)
Port: 27017 (default)
Username: (none - local development)
Password: (none - local development)
Connection String: mongodb://localhost:27017
```

---

## Basic MongoDB Commands (mongosh)

### Database Operations

```javascript
// Show all databases
show dbs

// Create/switch to a database
use learning_db

// Get current database
db

// Delete current database
db.dropDatabase()
```

### Collection Operations

```javascript
// Show all collections in current database
show collections

// Create a collection
db.createCollection("students")

// Drop a collection
db.students.drop()
```

### Document Operations (CRUD)

```javascript
// CREATE - Insert one document
db.students.insertOne({ name: 'Alice', age: 25, major: 'CS' });

// CREATE - Insert multiple documents
db.students.insertMany([
  { name: 'Bob', age: 23, major: 'Math' },
  { name: 'Carol', age: 24, major: 'Physics' },
]);

// READ - Find all documents
db.students.find();

// READ - Find with filter
db.students.find({ major: 'CS' });

// READ - Find one
db.students.findOne({ name: 'Alice' });

// UPDATE - Update one document
db.students.updateOne({ name: 'Alice' }, { $set: { age: 26 } });

// UPDATE - Update multiple documents
db.students.updateMany({ major: 'CS' }, { $set: { year: 2 } });

// DELETE - Delete one document
db.students.deleteOne({ name: 'Alice' });

// DELETE - Delete multiple documents
db.students.deleteMany({ major: 'Math' });
```

---

## Learning Path in This Workspace

### Step 1: ✅ **MongoDB README** (You are here)

- Understand what MongoDB is
- Know how to start/stop it
- Learn basic shell commands

### Step 2: 📄 **Advanced Queries Guide** (`queries.md`)

- Filtering and searching
- Sorting and limiting
- Updating with operators
- Aggregation pipelines
- Real-world query examples

### Step 3: 📊 **Sample Data Script** (`sample-data.js`)

- Node.js script to populate test data
- Learn how to use MongoDB driver in code
- Practice queries on real data

### Step 4: 🚀 **Node.js Application** (`app.js`)

- Express server with MongoDB
- RESTful CRUD endpoints
- Real-world application example

---

## VS Code Integration

**MongoDB for VS Code** extension is already installed. Features:

- **Playground**: Test queries in VS Code
- **Connection Browser**: Browse databases/collections
- **Syntax Highlighting**: For MongoDB shell scripts

### How to Use It

1. Open Command Palette: `Cmd+Shift+P`
2. Search: "MongoDB: Launch Playground"
3. Write queries with full IntelliSense

### Auto-reload (nodemon) — development

Use nodemon to automatically restart the Express server when you save code changes so you can see updates immediately.

- Install (dev dependency):
  - `npm install --save-dev nodemon`
- Run directly (no script):
  - `npx nodemon ./mongodb/app.js`
- Run via package.json script (convenient):
  - `npm run dev-mongo` # runs `nodemon ./mongodb/app.js`

Notes:

- Run commands from the `test-apps` workspace root so the `./mongodb/app.js` path resolves correctly.
- nodemon watches files and restarts the Node process on save — stop with `Ctrl+C`.
- After restart, check the Integrated Terminal for `🚀 Server running at http://localhost:3000` to confirm the server is up.

---

## System Dependencies

### macOS (Already Installed)

- `mongodb-community` via Homebrew
- `mongosh` (MongoDB shell) - included with mongodb-community

### Verify Installation

```bash
mongosh --version
mongod --version
```

---

## Troubleshooting

### MongoDB won't start

```bash
# Check if service is running
brew services list | grep mongodb

# Try manual start
mongod --config /usr/local/etc/mongod.conf

# Check logs
tail -f /usr/local/var/log/mongodb/mongo.log
```

### mongosh connection error

```bash
# Ensure MongoDB is running
brew services start mongodb-community

# Try connecting with explicit host
mongosh --host localhost --port 27017
```

### Need to reset everything

```bash
# Stop MongoDB
brew services stop mongodb-community

# Remove all data (careful!)
rm -rf /usr/local/var/mongodb

# Start fresh
brew services start mongodb-community
```

---

## Resources

- **Official Docs**: https://docs.mongodb.com
- **Query Language**: https://docs.mongodb.com/manual/reference/operator/query/
- **Node.js Driver**: https://www.mongodb.com/docs/drivers/node/
- **MongoDB University**: https://university.mongodb.com (free courses)

---

## Next Steps

Once you're comfortable with basic commands:

1. ✅ Read this README
2. 📖 Review `queries.md` for advanced examples
3. 🔧 Run `sample-data.js` to populate test data
4. 🚀 Start `app.js` and test the API

Ready for Step 2? Let me know when you want to create the **Advanced Queries Guide**! 🎯
