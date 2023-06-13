#!/usr/bin/node
const arg = process.argv[2];
const number = parseInt(arg);

if (Number.isNaN(number)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < number) {
    console.log('C is fun');
    i++;
  }
}
