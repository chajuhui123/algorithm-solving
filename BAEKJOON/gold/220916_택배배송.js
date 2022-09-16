// let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const input =
  "6 8\n4 5 3\n2 4 0\n4 1 4\n2 1 1\n5 6 1\n3 6 2\n3 2 6\n3 4 4".split("\n");

const [N, M] = input.shift().split(" ").map(Number);

// const dist = new Array(N + 1).fill(Infinity);
const graph = Array.from({ length: N + 1 }, () =>
  Array.from({ length: N + 1 }, () => Infinity)
);
// const priorityQueue = [];

// input.map((road) => {
//   const [Ai, Bi, Ci] = road.split(" ").map(Number);
//   // 인접리스트 양방향 초기화
//   adj[Ai][Bi] = Ci;
//   adj[Bi][Ai] = Ci;
// });

// priorityQueue.push([1, 0]);
// dist[1] = 0; // 출발 노드

// while (priorityQueue.length) {
//   // cost 기준 오름차순
//   priorityQueue.sort((a, b) => a - b);

//   const [to, cost] = priorityQueue.shift();

//   adj[to].forEach((nextNodeCost, nextNodeIndex) => {
//     if (dist[nextNodeIndex] > dist[to] + nextNodeCost) {
//       dist[nextNodeIndex] = dist[to] + nextNodeCost;
//       priorityQueue.push([nextNodeIndex, nextNodeCost]);
//     }
//   });
// }

// console.log(dist[N]);

input.map((road) => {
  const [Ai, Bi, Ci] = road.split(" ").map(Number);
  // 인접리스트 양방향 초기화
  graph[Ai].push([Bi, Ci]);
  graph[Bi].push([Ai, Ci]);
});

const dijkstra = (from, to) => {
  let dist = Array.from({ length: N + 1 }, () => Infinity);
  let priorityQueue = [];

  priorityQueue.push([0, from]);

  dist[from] = 0; // 시작 노드

  while (priorityQueue.length) {
    const [cost, here] = priorityQueue.sort((a, b) => a - b).shift();
    if (dist[here] < cost) continue;
    for (let there of graph[here].entries()) {
      const [thereIndex, thereCost] = there;
      let nextCost = cost + thereCost[0];
      if (dist[thereCost[1]] > nextCost) {
        dist[thereCost[1]] = nextCost;
        priorityQueue.push([nextCost, thereCost[1]]);
      }
    }
  }
  console.log(dist[to]);
};

dijkstra(1, N);

// console.log(dist);
