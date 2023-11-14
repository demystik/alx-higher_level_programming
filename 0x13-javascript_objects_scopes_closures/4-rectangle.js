#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 & h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let size = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        size += 'X';
      }
      console.log(size);
      size = '';
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
