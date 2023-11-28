#!/usr/bin/node

const req = require('request');
const id = process.argv[2];
const link = `https://swapi-api.alx-tools.com/api/films/${id}`;

req(link, function (err, res, data) {
  if (err) {
    console.log(err);
  } else {
    const c = JSON.parse(data).characters;
    logAll(c, 0);
  }
});

function logAll (c, idx) {
  req(c[idx], function (err, res, data) {
    if (err) {
      console.log(err);
    } else {
      console.log(JSON.parse(data).name);
      if (idx + 1 < c.length) {
        logAll(c, idx + 1);
      }
    }
  });
}
