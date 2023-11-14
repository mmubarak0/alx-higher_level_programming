#!/usr/bin/node

const argv = process.argv;

console.log(factorial(Number(argv[2])));

function factorial (a) {
  if (!a) { return (1); }
  return a * factorial(a - 1);
}
