#!/usr/bin/node
const process = require('process');

const args = process.argv;
if (args.length < 3) {
  console.log('No argument');
} else {
  console.log('Arguments found');
}
