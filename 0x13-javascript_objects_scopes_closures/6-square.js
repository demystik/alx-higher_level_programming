#!/usr/bin/node

const supSquare = require('./5-square.js');

class Square extends supSquare {
  charPrint (c) {
    if (c === undefined) { c = 'X'; }
    let shape = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        shape += c;
      }
      console.log(shape);
      shape = '';
    }
  }
}
module.exports = Square;
