#!/usr/bin/node

const fs = require('node:fs');

fs.readFile(process.argv[2], 'utf8', (data, err) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
