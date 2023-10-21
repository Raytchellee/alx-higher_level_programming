#!/usr/bin/node
const argv = process.argv;
const count = parseInt(argv[2]);

if (isNaN(count)) {
  console.log('Missing size');
} else {
  for (let idx = 0; idx < count; idx++) {
    const line = [];
    for (let idy = 0; idy < count; idy++) {
      line.push('X');
    }
    console.log(line.join(''));
  }
}
