#!/usr/bin/node
// script that returns all characters in a Star Wars movie

const request = require('request');
const film = process.argv[2];
const requestURL = `https://swapi-api.hbtn.io/api/films/${film}`;

request(requestURL, (error, response, body) => {
  if (!error) {
    const characters = JSON.parse(body).characters;
    characters.forEach((character) => {
      request(character, function (error, response, body) {
        if (!error) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
