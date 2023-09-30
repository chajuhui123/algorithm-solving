// 20125

let fs = require("fs");
let input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "test.txt")
  .toString()
  .trim()
  .split("\n");

const N = Number(input.shift());

let head = -1;
let headLocation = -1;

let leftArmLength = 0;
let rightArmLength = 0;
let bodyLength = 0;
let leftLegLength = 0;
let rightLegLength = 0;

input.forEach((value, idx) => {
  // 1. 머리 부분 찾기
  if (head === -1 && value.indexOf("*") !== -1) {
    head = idx;
    headLocation = value.indexOf("*");
  }

  // 2. 심장 기준 왼쪽팔 오른쪽팔 찾기
  if (head !== -1 && idx === head + 1) {
    leftArmLength = value
      .slice(0, headLocation)
      .split("")
      .filter((value) => value === "*").length;

    rightArmLength = value
      .slice(headLocation + 1)
      .split("")
      .filter((value) => value === "*").length;
  }

  // 3. 몸길이, 왼쪽다리, 오른쪽다리 길이 계산
  if (head !== -1 && idx > head + 1) {
    if (value[headLocation] === "*") bodyLength++;
    if (value[headLocation - 1] === "*") leftLegLength++;
    if (value[headLocation + 1] === "*") rightLegLength++;
  }
});

console.log(head + 2, headLocation + 1);
console.log(
  leftArmLength,
  rightArmLength,
  bodyLength,
  leftLegLength,
  rightLegLength
);
