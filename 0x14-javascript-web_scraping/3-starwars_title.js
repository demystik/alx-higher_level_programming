#!/usr/bin/node

const args = process.argv.slice(2);
const request = require('request');

const id = args[0];
const endpoint = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(endpoint, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode != 200) {
    console.log(`Failed to retrieve Data ${response.statusCode}`)
    process.exit(1);
  } else {
    const movieData = JSON.parse(body);
    console.log(movieData.title)
  }
});
