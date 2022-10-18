#!/usr/bin/node
/* script that reads and prints the content of a file
the first argument is the file path
The content of the file must be read in utf-8
if error occurs print error object */

const file = process.argv[2];
const fs = require('fs');

fs.readFile(file, 'utf8', function (error, data) {
if (error) {
console.log(error);
} else {
console.log(data);
}
});
