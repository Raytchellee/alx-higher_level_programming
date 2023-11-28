#!/usr/bin/node

const req = require('request');
const link = process.argv[2];

req(link, function (err, res, data) {
  if (err) {
    console.log(err);
  } else {
    const tasks = JSON.parse(data);
    let done = {};
    tasks.forEach((todo) => {
      if (todo.completed && !(todo.userId in done)) {
        done[todo.userId] = 1;
      } else if (todo.completed) {
        done[todo.userId] += 1;
      }
    });
    console.log(done);
  }
});
