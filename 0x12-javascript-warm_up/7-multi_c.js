#!/usr/bin/node

const err = 'Missing number of occurrences';
const message = 'C is fun';
const argv = process.argv;

const n = Number(argv[2]);
if (!n) {
  console.log(err);
} else {
  for (let i = 0; i < n; i++) {
    console.log(message);
  }
}
