#!/usr/bin/node

const fs = require('fs');
const f = process.argv[2];

fs.readFile(f, 'utf8', function (err, data) {
  console.log(err || data);
});
