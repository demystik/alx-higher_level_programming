#!/usr/bin/node

const args = process.argv.slice(2);
const fs = require('node:fs');

fs.readFile(args[0], 'utf-8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
