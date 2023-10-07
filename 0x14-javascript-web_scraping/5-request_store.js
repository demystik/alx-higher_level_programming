#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const args = process.argv.slice(2);
const url = args[0];
const filePath = args[1];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
      console.error(`${response.statusCode}`);
  } else {
      fs.writeFile(filePath, body, 'utf8', (writeError) => {
        console.error(error)
      });
    }
});
