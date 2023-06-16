#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i += 1) {
      let rec = '';
      for (let j = 0; j < this.width; j += 1) { rec += 'X'; }
      console.log(rec);
    }
  }
}
module.exports = Rectangle;
