#!/usr/bin/node

const fs = require('fs');
const req = require('request');
const link = process.argv[2];
const f = process.argv[3];

req(link).pipe(fs.createWriteStream(f));
