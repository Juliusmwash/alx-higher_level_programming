#!/usr/bin/node
const arg = process.argv[2];
const number = parseInt(arg);

if (Number.isNaN(number)) {
  console.log('Missing size');
} else {
  let i = 0; let j = 0;
  while (i < number) {
    while (j < number) {
      process.stdout.write('#');
      j++;
    }
    process.stdout.write('\n');
    i++;
    j = 0;
  }
}
