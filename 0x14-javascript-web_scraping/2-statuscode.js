#!/usr/bin/node
// script that displays the status code of a GET request
// first argument is the URl to GET
// print status code as: code: <status code>
// Use module request

const args = process.argv;
const URLrequest = args[2];
const req = require('request');
req(URLrequest, function (error, response, body) {
  if (error) {
    console.log('error:', error);
    } else {
      console.log('code:', response && response.statusCode);
      }
});
