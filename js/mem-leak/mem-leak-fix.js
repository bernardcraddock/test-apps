// leak.js
const leakedArray = [];

function createGarbage() {
  // 1. Create a large object (simulating user data)
  const data = {
    id: Math.random(),
    content: new Array(100000).fill('Some heavy data string to take up space'),
    timestamp: Date.now()
  };

  // 2. Push it to a global array (So the GC CANNOT delete it)
  leakedArray.push(data);

 // 2.5 THE FIX: If the array gets too big, delete the old stuff!
  if (leakedArray.length > 500) { // Keep max 500 items
      leakedArray.shift(); // Remove the oldest item
      console.log(`Max items ${leakedArray.length} removing oldest item`);
  }

  // 3. Log current memory usage every 100 items
  if (leakedArray.length % 100 === 0) {
    const used = process.memoryUsage().heapUsed / 1024 / 1024;
    console.log(`Array size: ${leakedArray.length} items | Memory Used: ${Math.round(used)} MB`);
  }
}

console.log("Starting memory leak...");

// Run this function every 5 milliseconds
setInterval(createGarbage, 5);