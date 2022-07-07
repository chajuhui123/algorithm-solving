let fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "BAEKJOON/example.txt";
const input = require("fs")
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n");

const TESTCASE = Number(input.shift()); // 총 TC 갯수

const getDistance = (x, y, targetX, targetY) =>
  Math.abs(x - targetX) + Math.abs(y - targetY);

const isInclude = (array, searchTarget) => {
  let isInclude = false;
  array.map((item) => {
    if (JSON.stringify(item) === JSON.stringify(searchTarget)) isInclude = true;
  });
  return isInclude;
};

for (let i = 0; i < TESTCASE; i++) {
  const marketCount = Number(input.shift());
  let [startX, startY] = input.shift().split(" ").map(Number); // 출발지 (상근 집)
  const marketArr = [];
  for (let j = 0; j < marketCount; j++)
    marketArr.push(input.shift().split(" ").map(Number)); // 편의점 위치 Array
  const [endX, endY] = input.shift().split(" ").map(Number); // 도착지 (페스티벌)
  const toGo = [...marketArr, [endX, endY]].sort((a, b) => a - b);

  const queue = [[startX, startY]];
  const visited = [];

  while (queue) {
    const [nowX, nowY] = queue.shift();

    console.log(nowX, nowY);

    for (let [goX, goY] of toGo) {
      if (!isInclude(visited, [goX, goY])) {
        if (getDistance(nowX, nowY, goX, goY) <= 1000) {
          if (goX === endX && goY === endY) {
            console.log("happy");
            break;
          }
          visited.push([goX, goY]);
          queue.push([goX, goY]);
        }
      }
    }
  }
  console.log("sad");
}
