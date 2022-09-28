//9465

let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

// const input =
//   "2\n5\n50 10 100 20 40\n30 50 70 10 60\n7\n10 30 10 50 100 20 40\n20 40 30 50 60 20 80".split(
//     "\n"
//   );

const answer = [];
const TC = +input.shift(); // TC 갯수

let TCIndex = 0; // TC 별로 인덱스 접근하기 위해 선언
for (let i = 0; i < TC; i++) {
  const N = input[TCIndex];
  const sticker1 = input[TCIndex + 1].split(" ").map(Number);
  const sticker2 = input[TCIndex + 2].split(" ").map(Number);

  // [아무것도 고르지 않은경우, 위에 값을 고른 경우, 아랫 값을 고른 경우] 로 정의
  let dp = [[0, sticker1[0], sticker2[0]]];

  for (let j = 1; j < N; j++) {
    // dp[j][0] => 아무것도 고르지 않을 때는 dp[j-1] 중 최댓값
    // dp[j][1] => 위의 값을 고를 때는, dp[j-1][0] VS dp[j-1][2] 아무것도 고르지 않은 경우와 아랫쪽 값을 고른 경우 중 최댓값 + 현재 위치 (위 값)
    // dp[j][2] => 아래 값을 고를 때는, dp[j-1][0] VS dp[j-1][1] 아무것도 고르지 않은 경우와 위쪽 값을 고른 경우 중 최댓값 + 현재 위치 (아래 값)
    dp.push([
      Math.max(...dp[j - 1]),
      Math.max(dp[j - 1][0], dp[j - 1][2]) + sticker1[j],
      Math.max(dp[j - 1][0], dp[j - 1][1]) + sticker2[j],
    ]);
  }

  answer.push(Math.max(...dp[N - 1]));
  TCIndex += 3;
}

console.log(answer.join("\n"));

// IDEA

// 1. DP 정의
// dp[i][0] : 왼쪽에 있는 값 중 아무것도 고르지 않은 경우
// dp[i][1] : 위의 값을 고른 경우
// dp[i][2] : 아래 값을 고른 경우

// 2. 로직 정의
// 따라서 dp[i] 구할 때,
// dp[i][0] => 아무것도 고르지 않을 때는 dp[i-1] 중 최댓값
// dp[i][1] => 위의 값을 고를 때는, dp[i-1][0] VS dp[i-1][2] 아무것도 고르지 않은 경우와 아랫쪽 값을 고른 경우 중 최댓값
// dp[i][2] => 아래 값을 고를 때는, dp[i-1][0] VS dp[i-1][1] 아무것도 고르지 않은 경우와 위쪽 값을 고른 경우 중 최댓값
