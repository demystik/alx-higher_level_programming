#!/usr/bin/node

const supSquare = require('./5-square.js');

class Square extends supSquare {
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    if (c === undefined) { c = 'X'; }
    let shape = '';
    for (let i = 0; i < this.size; i++) {
      for (let j = 0; j < this.size; j++) {
        shape += c;
      }
      console.log(shape);
      shape = '';
    }
  }
}
module.exports = Square;
