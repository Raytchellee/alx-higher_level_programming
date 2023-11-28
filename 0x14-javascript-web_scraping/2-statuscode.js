#!/usr/bin/node

const req = require('request');
const link = process.argv[2];

req.get(link).on('response', function (res) {
  console.log(`code: ${res.statusCode}`);
});
