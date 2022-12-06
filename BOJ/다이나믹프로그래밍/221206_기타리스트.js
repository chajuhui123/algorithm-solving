// 1495

// let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

// let input = "3 5 10\n5 3 7".split("\n");
let input = "4 8 20\n15 2 9 10".split("\n");

const [n, s, m] = input[0].split(" ").map(Number);
const v = input[1].split(" ").map(Number);

let dp = Array.from(Array(n + 1), () => Array(m + 1).fill(0));
dp[0][s] = 1;

for (let i = 0; i < n; i++) {
  for (let j = 0; j < m + 1; j++) {
    // if (dp[i][j] == 1) {
    // }
    if (j + v[i] <= m) dp[i + 1][j + v[i]] = 1;
    if (j - v[i] >= 0) dp[i + 1][j - v[i]] = 1;
  }
}

let answer = -1;

for (let k = m; k >= 0; k--) {
  if (dp[n][k] == 1) {
    answer = k;
    break;
  }
}

console.log(answer);
