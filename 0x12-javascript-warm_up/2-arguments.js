#!/usr/bin/node

const a = 'No argument';
const b = 'Argument found';
const c = 'Arguments found';
const argv = process.argv;
const arglen = argv.length;

if (arglen === 2) {
  console.log(a);
} else if (arglen === 3) {
  console.log(b);
} else {
  console.log(c);
}
