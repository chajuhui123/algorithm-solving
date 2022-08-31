// let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const input = "5\nX S X X T\nT X S X X\nX X X X X\nX T X X X\nX X T X X".split(
  "\n"
);

const N = Number(input.shift());
const graph = input.map((line) => line.split(" "));

// 장애물을 설치할 수 있는 'X' 좌표 모음
const XArray = [];
// 선생님 위치 좌표 모음
const TArray = [];

graph.map((line, lineIndex) => {
  line.map((item, itemIndex) => {
    if (graph[lineIndex][itemIndex] === "X")
      XArray.push([lineIndex, itemIndex]);
    if (graph[lineIndex][itemIndex] === "T")
      TArray.push([lineIndex, itemIndex]);
  });
});
