#!/usr/bin/node

const args = process.argv.slice(2)

const request = require('request');
const movieId = args[0]
const apiUrl = `https://swapi-api.alx-tools.com/api/films/:id`

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
      console.error(`${response.statusCode}`);
  } else {
      const movieData = JSON.parse(body);
      console.log(`${movieData.title}`);
  }

});
