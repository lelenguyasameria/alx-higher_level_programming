#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    try {
      const movieData = JSON.parse(body);

      // Print character names
      movieData.characters.forEach((characterUrl) => {
        request.get(characterUrl, (charError, charResponse, charBody) => {
          if (charError) {
            console.error(charError);
          } else {
            const characterData = JSON.parse(charBody);
            console.log(characterData.name);
          }
        });
      });
    } catch (parseError) {
      console.error(parseError);
    }
  }
});

