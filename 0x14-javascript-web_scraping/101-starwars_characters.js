#!/usr/bin/node

const request = require('request');

async function getMovieCharacters(movieId) {
  const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

  try {
    const movieData = await getRequest(apiUrl);
    
    // Use Promise.all to fetch character details asynchronously
    await Promise.all(movieData.characters.map(async (characterUrl) => {
      const characterData = await getRequest(characterUrl);
      console.log(characterData.name);
    }));
  } catch (error) {
    console.error(error);
  }
}

function getRequest(url) {
  return new Promise((resolve, reject) => {
    request.get(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

const movieId = process.argv[2];
getMovieCharacters(movieId);

