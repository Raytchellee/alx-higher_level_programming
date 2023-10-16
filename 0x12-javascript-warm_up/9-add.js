#!/usr/bin/node
const { argv } = require('node:process');
const one = parseInt(argv[2]);
const two = parseInt(argv[3]);

function add (a, b) {
  console.log(a + b);
}

add(one, two);
