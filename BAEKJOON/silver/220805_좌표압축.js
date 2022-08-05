let fs = require("fs");

const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

// const input = ["5", "2 4 -10 4 -9"];
// const input = ["6", "1000 999 1000 999 1000 999"];

const numArr = input[1].split(" ").map(Number);
const numSet = new Set(numArr);
const sortedNumArr = [...numSet].sort((a, b) => a - b);

const answer = [];

for (let num of numArr) answer.push(sortedNumArr.indexOf(num));

console.log(answer.join(" "));
