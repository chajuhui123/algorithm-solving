// 11650

let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

// const input = "5\n3 4\n1 1\n1 -1\n2 2\n3 3".split("\n");

const N = +input.shift();
const xyArr = input.map((xy) => xy.split(" ").map(Number));

// x, y 정렬
xyArr.sort((a, b) => {
  if (a[0] === b[0]) return a[1] - b[1];
  return a[0] - b[0];
});

const answer = xyArr.map((xy) => xy.join(" ")).join("\n");
console.log(answer);
