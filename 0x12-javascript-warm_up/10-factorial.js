#!/usr/bin/node

const process = require('process');
let get = 0;
args = process.argv;
const num = args[2];

if (!(args[2])) {
  console.log('1');
} else {
  factorial(Number(args[2]));
  console.log(get);
}
function factorial(num) {
  get = get + num;
  num--;
  while (num > 0) {
    factorial(num);
  }
}
