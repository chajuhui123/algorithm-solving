let fs = require("fs");
let input = fs.readFileSync("../example.txt").toString().split(" ");
// let input = fs.readFileSync("/dev/stdin").toString().split(" "); // 백준 제출시

const inputArr = input[0].split("\n");

const solution = (inputArr) => {
  for (let item of inputArr) {
    // 1. X가 이긴 경우, X의 갯수+1 == O의 갯수
    // 2. O가 이긴 경우, X의 갯수 == O의 갯수
    // 3. 무승부인 경우, X의 갯수+1 == O의 갯수
  }
};

solution(inputArr);
