#!/usr/bin/node
const { argv } = require('node:process');

let num = parseInt(argv[2]);
const numX = num;
const charX = 'X';
if (isNaN(num)) {
  console.log('Missing size');
} else {
  while (num > 0) {
    console.log(charX.repeat(numX));
    num--;
  }
}
