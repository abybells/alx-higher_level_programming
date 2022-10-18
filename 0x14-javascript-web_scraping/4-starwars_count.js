#!/usr/bin/node
// prints the number of movies
// where the character Wedge Antilles is present

const arg = process.argv;
let URLreq = arg[2];
const request = require('request');

request(URLreq, function (error, response, body) {
  if (error) {
    console.log('error:', error);
  } else {
    let listFilms = (JSON.parse(body).results);
    let movieCount = 0;
    for (let i = 0; i < listFilms.length; i++) {
      let chars = (listFilms[i]['characters']);
      for (let j = 0; j < chars.length; j++) {
        let check18 = chars[j].endsWith('18/');
        if (check18) {
          count++;
        }
      }
    }
    console.log(movieCount);
  }
});
