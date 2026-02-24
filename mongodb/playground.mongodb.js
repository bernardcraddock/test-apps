// Playground: `learning_db` — ready-to-run query examples
// Instructions:
// 1) Select the connection in the top-right (choose your local `learning_db` connection).
// 2) Run the selection or Run All (Play button / Cmd+Enter).
// 3) Results appear in the Playground output pane; save this file for reuse.

use('learning_db');

// ---------- 1) Quick list (first 10 students)
use('learning_db');
db.students.find().limit(10);

// ---------- 2) Top 3 students by GPA
use('learning_db');
db.students.find().sort({ gpa: -1 }).limit(3);

// ---------- 3) Count students by major (group) — sorted by count desc, then avgGpa desc
use('learning_db');
db.students.aggregate([
  { $group: { _id: '$major', count: { $sum: 1 }, avgGpa: { $avg: '$gpa' } } },
  { $sort: { count: -1, avgGpa: -1 } },
]);

// ---------- 4) $lookup example — populate a student with its course documents
use('learning_db');
db.students.aggregate([
  { $match: { _id: 1 } },
  {
    $lookup: {
      from: 'courses',
      localField: 'courses',
      foreignField: '_id',
      as: 'courseDocs',
    },
  },
]);

// ---------- 5) Add a compound index (useful for filter+sort queries)
// (Run this once; it will persist on the server)
// use('learning_db');
// db.students.createIndex({ major: 1, gpa: -1 });

// ---------- 6) Explain plan for a sort (verify index usage)
// use('learning_db');
// db.students.find().sort({ gpa: -1 }).limit(3).explain('executionStats');

// ---------- 7) Example update (toggle active)
// use('learning_db');
// db.students.updateOne({ _id: 6 }, { $set: { active: true } });

// ---------- Tips
// - Select any line or block and press Run Selected; use Run All to execute every statement.
// - Save the playground to keep your favorite queries in the repo.
// - If a command modifies data (createIndex, updateOne), run it intentionally (uncomment first).
// - Note: MongoDB Playground requires use('learning_db') before each query block (unlike mongosh CLI where it persists).
