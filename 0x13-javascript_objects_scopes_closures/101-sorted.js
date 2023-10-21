#!/usr/bin/node
const dict = require('./101-data.js').dict;

const newDict = {};

for (const [key, val] of Object.entries(dict)) {
  if (!(val in newDict)) {
    newDict[val] = [];
  }
  newDict[val].push(key);
}

console.log(newDict);
