#!/usr/bin/node

const err = 'No argument';
const argv = process.argv;

if (argv[2]) {
  console.log(...argv[2]);
} else {
  console.log(err);
}
