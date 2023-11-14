#!/usr/bin/node

const err = 'Missing size';
const shape = 'X';
const argv = process.argv;

const n = Number(argv[2]);
if (!n) {
  console.log(err);
} else {
  for (let i = 0; i < n; i++) {
    console.log(shape.repeat(n));
  }
}
