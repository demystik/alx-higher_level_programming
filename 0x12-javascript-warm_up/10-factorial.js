#!/usr/bin/node

const process = require('process');
let get = 0;
args = process.argv;
const num = Number(args[2]);


function factorial (num) {
  if (num < 0) {
    return (-1);
  }
  if (num === 0 || isNaN(num)) {
    return (1);
  }
  return (num * factorial(num - 1));
  
}

console.log(factorial(num));
