#!/usr/bin/node

const err = 'No argument';
const argv = process.argv;

if (!argv[2]) {
  console.log(err);
} else {
  console.log(argv[2]);
}
