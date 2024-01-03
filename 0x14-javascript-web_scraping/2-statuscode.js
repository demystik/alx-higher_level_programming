#!/usr/bin/node

const args = process.argv.slice(2);
const request = require('request');

const url = args[0];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
