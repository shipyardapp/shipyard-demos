console.log('here i am');

const { execSync } = require('child_process');

const stdio = execSync('ls -laR /home/shipyard');
console.log(stdio.toString());

console.log('whoami');

const stdio2 = execSync('ls -laR /tmp');
console.log(stdio2.toString());

// , (err, stdout, stderr) => {
// 	console.log(err);
// 	console.log(stdout);
// 	console.log(stderr);
// });

///////////////////////////////

const dataForge = require('data-forge');
require('data-forge-fs')
const { v4: uuidv4 } = require('uuid');

console.log('Hello, World!');
console.log(`My name is ${process.env.NAME}`);
console.log(`Here's a random UUID: ${uuidv4()}`);
console.log(`This Vessel is named "${process.env.SHIPYARD_VESSEL_NAME}" and has an ID of ${process.env.SHIPYARD_VESSEL_ID}`);

columns = ["A", "B", "C"]
rows = []
let i = 0;
do {
  i += 1;
  rows.push(Array.from({length: columns.length}, () => Math.floor(Math.random() * 100)));
} while (i < 1000);

const df = new dataForge.DataFrame({
    columnNames: columns,
    rows: rows
});
df. asCSV().writeFileSync('output.csv');

console.log('File output.csv successfully created')
console.log(df.toString())

