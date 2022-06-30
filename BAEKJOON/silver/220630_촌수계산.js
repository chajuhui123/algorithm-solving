let fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "BAEKJOON/example.txt";
const input = require("fs")
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n");

const PEOPLE = Number(input.shift()); // 총 사람 명수
const [me, target] = input.shift().split(" ").map(Number);
const relationCount = Number(input.shift());

const relationMapping = input.map((item) => item.split(" ").map(Number));

// 연결 관계를 나타내는 graph 초기화
const graph = [...Array(PEOPLE + 1)].map(() => []);
relationMapping.map(([x, y]) => {
  graph[x].push(y);
  graph[y].push(x);
});

// DFS
const DFS = (start, end) => {
  const stack = [start];
  const visited = Array(PEOPLE + 1).fill(false);

  let cntVillager = 0;

  while (stack.length) {
    const node = stack.pop();

    if (node === end) return cntVillager;

    if (!visited[node]) {
      cntVillager++;
      visited[node] = true;
      stack.push(...graph[node]);
    }
  }
  return -1;
};

graph.forEach((v) => v.sort((a, b) => b - a));
const answer = DFS(me, target);

console.log(answer);
