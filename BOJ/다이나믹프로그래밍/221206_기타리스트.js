// 1495

let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

// let input = "3 5 10\n5 3 7".split("\n");
// let input = "4 8 20\n15 2 9 10".split("\n");
// let input = "14 40 243\n74 39 127 95 63 140 99 96 154 18 137 162 14 88".split(
//   "\n"
// );

const [n, s, m] = input[0].split(" ").map(Number);
const v = input[1].split(" ").map(Number);

let dp = Array.from(Array(n + 1), () => Array(m + 1).fill(0));
dp[0][s] = 1;

for (let i = 1; i <= n; i++) {
  for (let j = 0; j <= m; j++) {
    // 기존 값이 0인 경우 넘어감
    if (dp[i - 1][j] == 0) continue;
    // 현재 인덱스에 볼륨 값을 + 한 경우, 주어진 범위 값에 포함된다면 dp 1로 변경
    if (j + v[i - 1] <= m) dp[i][j + v[i - 1]] = 1;
    // 현재 인덱스에 볼륨 값을 - 한 경우, 주어진 범위 값에 포함된다면 dp 1로 변경
    if (j - v[i - 1] >= 0) dp[i][j - v[i - 1]] = 1;
  }
}

let answer = -1;

// console.log(dp);

for (let k = m; k >= 0; k--) {
  if (dp[n][k]) {
    answer = k;
    break;
  }
}

console.log(answer);

// IDEA
// 오랜만에 NodeJS 풀이가 하고 싶어서 했는데 2중 배열 초기화 하는 것부터 어색해져서 까먹어서 난감 ^^... Array.from 을 잊고 있었다..
