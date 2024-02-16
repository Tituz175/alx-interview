#!/usr/bin/node
const axios = require('axios').default;
const movieId = process.argv[2];

async function fetch (url) {
  try {
    const response = await axios.get(url);
    return response;
  } catch (error) {
    console.error(error);
  }
}

const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

async function getMovieCharacters () {
  try {
    const characters = [];
    const movieData = await fetch(movieUrl);
    for (const url of movieData.data.characters) {
      const characterData = await fetch(url);
      characters.push(characterData.data.name);
    }
    characters.forEach(element => {
      console.log(element);
    });
  } catch (error) {
    console.error(error);
  }
}

getMovieCharacters();
