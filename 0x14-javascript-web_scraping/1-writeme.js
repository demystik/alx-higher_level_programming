#!/usr/bin/node

const args = process.argv.slice(2);

const fs = require('fs');

const filePath = args[0];
const content = args[1];

fs.writeFile(filePath, content, 'utf8', (error) => {
  if (error) {
    console.error(error);
    return;
  }

});
