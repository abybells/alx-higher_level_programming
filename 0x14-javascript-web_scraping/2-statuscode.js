#!/usr/bin/node
// script that displays the status code of a GET request
// first argument is the URl to GET

const arg = process.argv;
const requestURL = arg[2];
const request = require('request');

request.get(requestURL).on('response', function (eroor, response, body) {
  if (error) {
    console.log('error:', error);
  } else console.log('code:', response && response.statusCode);
});
