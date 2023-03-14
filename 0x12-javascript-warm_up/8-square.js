#!/usr/bin/node

const process = require('process');

const args = process.argv;
const count = [];
if (Number(args[2])) {
  for (let i = 0; i < Number(args[2]); i++) {
    count.push('X');
  }
  for (let i = 0; i < Number(args[2]); i++) {
    console.log(count.join(''));
  }
} else {
  console.log('Missing size');
}
