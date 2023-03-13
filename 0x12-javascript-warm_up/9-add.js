#!/usr/bin/node
const process = require('process');

const args = process.argv;

if (!(args[2]) || !(args[3])) {
  console.log('NaN');
} else {
  add(args[2], args[3]);
}

function add (a, b) {
  console.log(Number(a) + Number(b));
}
