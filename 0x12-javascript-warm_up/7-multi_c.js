#!/usr/bin/node
const argv = process.argv;
const count = parseInt(argv[2]);

if (isNaN(count)) {
  console.log('Missing number of occurrences');
} else {
  for (let idx = 0; idx < count; idx++) {
    console.log('C is fun');
  }
}
