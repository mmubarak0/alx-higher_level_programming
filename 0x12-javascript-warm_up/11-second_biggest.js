#!/usr/bin/node

const argv = process.argv.slice(2);
argv.sort((x, y) => x - y);

if (argv.length < 2) {
  console.log(0);
} else {
  console.log(argv[argv.length - 2]);
}
