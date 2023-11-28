#!/usr/bin/node

const fs = require('fs');
const f = process.argv[2];
const c = process.argv[3];

fs.writeFile(f, c, err => {
  if (err) console.log(err);
});
