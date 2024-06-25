#!/usr/bin/node
const { argv } = require('node:process');
const firstArg = Number(argv[2]);
const secArg = Number(argv[3]);

function add (a, b) {
  return (a + b);
}
console.log(add(firstArg, secArg));
