#!/usr/bin/node
// script that displays the status code of a GET request
// first argument is the URl to GET
// print status code as: code: <status code>
// Use module request

const args = process.argv;
const URLrequest = args[2];
const req = require('request');
req.get(URLrequest).on('response', function (response) {
  console.log('code: ${response.statusCode}');
});
