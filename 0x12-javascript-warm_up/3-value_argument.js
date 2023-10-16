#!/usr/bin/node
const argv = process.argv;
let count = 0;

argv.forEach((item, idx) => {
  if (idx > 1) {
    console.log(item);
    count++;
  }
});

if (count === 0) {
  console.log('No argument');
}
