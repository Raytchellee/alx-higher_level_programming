#!/usr/bin/node

const req = require('request');
const id = process.argv[2];
const link = `https://swapi-api.alx-tools.com/api/films/${id}`;

req(link, function (err, res, data) {
  console.log(err || JSON.parse(data).title);
});
