#!/usr/bin/node
const MainSquare = require('./5-square.js');

module.exports = class Square extends MainSquare {
  charPrint (c = 'X') {
    for (let idx = 0; idx < this.height; idx++) {
      const temp = [];
      for (let idy = 0; idy < this.width; idy++) {
        temp.push(c);
      }
      console.log(temp.join(''));
    }
  }
};
