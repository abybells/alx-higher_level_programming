#!/usr/bin/node
// script that writes a string to a file

const fs = require('fs');
const myfile = process.argv;

fs.writeFile(myfile[2], myfile[3], 'utf8', function (err, data) {
if (err) {
console.log(err);
}
});
