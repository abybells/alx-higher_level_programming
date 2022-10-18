#!/usr/bin/node
// prints the title of a star wars movie where episode no.
// matches given integer

const arg = process.argv;
const movieId = arg[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;
const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
