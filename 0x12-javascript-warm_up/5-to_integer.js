#!/usr/bin/node

const err = 'Not a number';
const argv = process.argv;

const n = Number(argv[2]);
if (!n) {
  console.log(err);
} else {
  console.log(`My number: ${n}`);
}
