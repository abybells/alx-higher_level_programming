#!/usr/bin/node
// script that displays the status code of a GET request
// first argument is the URl to GET
// print status code as: code: <status code>
// Use module request

const arg = process.argv;
const requestURL = arg[2];
const request = require('request');

req.get(requestURL).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
