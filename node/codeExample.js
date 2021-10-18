const { v4: uuidv4 } = require('uuid');

console.log('Hello, World!');
console.log(`My name is ${process.env.NAME}`);
console.log(`Here's a random UUID: ${uuidv4()}`);
console.log(`This Vessel is named "${process.env.SHIPYARD_VESSEL_NAME}"\
	and has an ID of ${process.env.SHIPYARD_VESSEL_ID}`);
