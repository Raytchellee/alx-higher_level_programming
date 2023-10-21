#!/usr/bin/node
const argv = process.argv;
const count = parseInt(argv[2]);

if (isNaN(count)) {
  console.log(1);
} else {
  console.log(factorial(count));
}

function factorial (num) {
  if (num < 2) return 1;
  return num * factorial(num - 1);
}
