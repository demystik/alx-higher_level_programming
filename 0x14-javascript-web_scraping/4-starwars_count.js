#!/usr/bin/node

const args = process.argv.slice(2);
const request = require('request');

const apiUrl = args[0];
const characterId = 18;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode !== 200) {
    console.log(`Failed to retrieve Data ${response.statusCode}`);
    process.exit(1);
  } else {
    const filmsData = JSON.parse(body).results;
    const moviesWithWedgeAntilles = filmsData.filter((film) =>
      film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
    );
    console.log(moviesWithWedgeAntilles.length);
  }
});
