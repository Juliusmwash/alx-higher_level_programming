#!/usr/bin/node
function factorial (a) {
  if (a === 0 || isNaN(a)) {
    return (1);
  } else {
    return (a * factorial(a - 1));
  }
}
const num = parseInt(process.argv[2]);
console.log(factorial(num));
