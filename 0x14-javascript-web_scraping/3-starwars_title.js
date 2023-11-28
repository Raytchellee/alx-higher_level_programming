#!/usr/bin/node

const req = require('request');
const id = process.argv[2];
let url = `https://swapi-api.alx-tools.com/api/films/${id}`;

req(url, function (err, res, data) {
  console.log(err || JSON.parse(data).title);
});
