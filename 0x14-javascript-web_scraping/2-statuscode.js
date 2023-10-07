#!/usr/bin/node

const args = process.argv.slice(2);

const request = require('request');
const url = args[0]

request(url, (error, response) => {
  if (error) {
    console.error(error);
  } else {
      console.log(`code: ${response.statuscode}`);
  }
});
