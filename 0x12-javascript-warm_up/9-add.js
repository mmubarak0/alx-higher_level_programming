#!/usr/bin/node

const argv = process.argv;

console.log(add(argv[2], argv[3]));

function add (a, b) {
  const x = Number(a);
  const y = Number(b);
  return (x + y);
}
