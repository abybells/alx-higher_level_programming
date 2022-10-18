#!/usr/bin/node
/* script that reads and prints the content of a file
the first argument is the file path
The content of the file must be read in utf-8
if error occurs print error object */

const myfile = process.argv;
const fs = require('fs');

fs.readFile(myfile[2], 'utf8', function (err, data) {
  if (err) {
    console.log(err);
    } else {
      console.log(data.toString());
      }
});
