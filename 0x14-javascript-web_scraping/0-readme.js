#!/usr/bin/node

const fs = require('node:fs');

fs.readFile(process.argv[2], 'utf-8', (err, data) => {
  if (err) {
    console.log(`{ Error: ${err.code}: no such file or directory, ${err.syscall} '${err.path}'
    at Error (native)
  errno: ${err.errno},
  code: '${err.code}',
  syscall: '${err.syscall}',
  path: '${err.path}' }`);
  } else {
    console.log(data);
  }
});
