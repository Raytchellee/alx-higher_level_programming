#!/usr/bin/node
const req = require('request');
const link = process.argv[2];

req(link, function (err, _, data) {
  if (!err) {
    const res = JSON.parse(data).results;
    console.log(res.reduce((num, film) => {
      return film.characters.find((d) => d.includes('18'))
        ? num + 1
        : num;
    }, 0));
  }
});
