let fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "BAEKJOON/example.txt";
const input = require("fs")
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n");

// 총 TC 갯수
const TESTCASE = Number(input.shift());

for (let i = 0; i < TESTCASE; i++) {
  const marketCount = Number(input.shift());
  const [startX, startY] = input.shift().split(" ").map(Number); // 출발지 (상근 집)
  const marketArr = []; // 편의점 위치 Array
  for (let j = 0; j < marketCount; j++)
    marketArr.push(input.shift().split(" ").map(Number));
  const [endX, endY] = input.shift().split(" ").map(Number); // 도착지 (페스티벌)

  let beerCount = 20;
}
