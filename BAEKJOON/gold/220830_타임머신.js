let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

// const input = "3 4\n1 2 4\n1 3 3\n2 3 -1\n3 1 -2".split("\n");

// N : 도시의 개수
// M : 버스 노선의 개수
const [N, M] = input.shift().split(" ").map(Number);

let cost = new Array(N + 1).fill(Infinity);
cost[1] = 0;

let answer = [];

for (let i = 0; i < N - 1; i++) {
  let change = false;

  input.forEach((v) => {
    const [A, B, C] = v.split(" ").map(Number);
    if (A !== Infinity && cost[A] + C < cost[B]) {
      cost[B] = cost[A] + C;
      change = true;
    }
  });
  if (!change) break;
}

answer = cost
  .slice(2, cost.length)
  .map((v) => {
    if (v === Infinity) return -1;
    return v;
  })
  .join("\n");

let check = false;

for (let i = 0; i < M; i++) {
  const [A, B, C] = input[i].split(" ").map(Number);

  if (A !== Infinity && cost[A] + C < cost[B]) {
    cost[B] = cost[A] + C;
    check = true;
  }

  if (check) answer = -1;
}

console.log(answer);
