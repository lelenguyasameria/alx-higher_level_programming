#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    try {
      const filmsData = JSON.parse(body).results;
      const moviesWithWedgeAntilles = filmsData.filter((film) =>
        film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
      );

      console.log(`Number of movies with Wedge Antilles: ${moviesWithWedgeAntilles.length}`);
    } catch (parseError) {
      console.error(parseError);
    }
  }
});

