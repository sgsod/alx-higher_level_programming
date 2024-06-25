#!/usr/bin/node
const { argv } = require('node:process');
let length = 0;
let numbersArr = [];
let secondBiggest = 0;

const copyInts = (element) => {
  if (!(isNaN(element))) {
    numbersArr.push(Number(element));
  }
};

argv.forEach(copyInts);
length = numbersArr.length;
if (length < 1) {
  console.log(secondBiggest);
} else if (length === 1) {
  if (numbersArr[0] > 1) {
    console.log(numbersArr[0])
  } else {
    console.log(secondBiggest);
  }
} else {
  numbersArr.sort();
  console.log(numbersArr[length - 2]);
}
