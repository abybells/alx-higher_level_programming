#!/usr/bin/node
// prints the number of movies where the character Wedge Antilles is present
// using module request

const arg = process.argv;
const requestURL = arg[2];
const request = require('request');

request(requestURL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const listFilms = (JSON.parse(body).results);
    let movieCount = 0;
    for (let i = 0; i < listFilms.length; i++) {
      for (let j = 0; j < listFilms[i].characters.length; j++) {
        if (listFilms[i].characters[j].includes('/18/')) {
          movieCount += 1;
        }
      }
    }
    console.log(movieCount);
  }
});
