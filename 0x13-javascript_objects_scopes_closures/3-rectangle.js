#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let idx = 0; idx < this.height; idx++) {
      const temp = [];
      for (let idy = 0; idy < this.width; idy++) {
        temp.push('X');
      }
      console.log(temp.join(''));
    }
  }
};
