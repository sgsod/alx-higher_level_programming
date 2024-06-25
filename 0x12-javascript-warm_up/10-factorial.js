#!/usr/bin/node
const { argv } = require('node:process');
const firstArg = Number(argv[2]);

function factorial (a) {
  if (a === 0) {
    return (1);
  } else {
    return (a * factorial(a - 1));
  }
}
if (isNaN(firstArg)) {
  console.log(firstArg);
} else {
  console.log(factorial(firstArg));
}
