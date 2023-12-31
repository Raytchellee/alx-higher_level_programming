#!/usr/bin/node
const argv = process.argv;
let largest = -Infinity;
let second = -Infinity;

if (argv.length < 4) {
  console.log(0);
} else {
  for (let idx = 2; idx < argv.length; idx++) {
    const num = parseInt(argv[idx]);
    if (num > largest) {
      second = largest;
      largest = num;
    } else if (second === -Infinity || num > second) {
      second = num;
    }
  }
  console.log(second);
}
