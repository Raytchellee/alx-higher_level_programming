#!/usr/bin/node

const req = require('request');
const id = process.argv[2];
const link = `https://swapi-api.alx-tools.com/api/films/${id}`;

req(link, function (err, res, data) {
  if (err) {
    console.log(err);
  } else {
    const c = JSON.parse(data).characters;
    c.forEach((character) => {
      req(character, function (err, res, data) {
        if (!err) {
          console.log(JSON.parse(data).name);
        }
      });
    });
  }
});
