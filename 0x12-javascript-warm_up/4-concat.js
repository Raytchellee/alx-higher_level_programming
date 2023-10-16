#!/usr/bin/node
const { argv } = require('node:process');
const two = argv[2] ? argv[2] : 'undefined';
const three = argv[3] ? argv[3] : 'undefined';

console.log(two.concat(' is ', three));
