#!/usr/bin/node
const argv = process.argv;
argv = argv.slice(2);

if (argv[0]) {
  argv.forEach((item, idx) => {
    console.log(item);
  });
} else {
  console.log('No argument');
}
