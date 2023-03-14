#!/usr/bin/node

const process = require('process');
const args = process.argv;

if (args.length <= 3) {
  console.log('0');
} else {
  const array = args.slice(2).map(Number);
  const get = array.sort(function (a, b) { return b - a; })[1];
  console.log(get);
}
