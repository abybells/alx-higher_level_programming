#!/usr/bin/node
// Script that display the status code of a GET request

const request = require('request');
const args = process.argv;
request(args[2], function (error, response, body) {
  if (error) {
    console.log('error:', error); // Print the error if one occurred
  } else console.log('code:', response && response.statusCode);
});
