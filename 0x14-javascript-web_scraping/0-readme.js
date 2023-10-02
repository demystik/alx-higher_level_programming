#!/usr/bin/node

const args = process.argv.slice(2);

const fs = require('fs');
const filePath = args[0];

fs.readFile(filePath, 'utf8', (error, data) => {
  if (error) {
    console.error(error);
    return;
  }

  console.log(data);
});
