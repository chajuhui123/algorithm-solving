let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

// const input = "6\n10 20 10 30 20 50".split("\n");

const N = +input[0]; // 수열 A의 길이
const A = input[1].split(" ").map(Number); // 수열 A

if (N === 1) {
  console.log(1);
  return;
}

let answer = 0;
let dp = Array.from({ length: N }, () => 1);

for (let i = 1; i < N; i++) {
  let cnt = 0;

  for (let j = 0; j < i; j++) {
    // 현재 값과 이전 값들을 비교하여 수열을 세울 수 있는지 검사함
    if (A[i] > A[j]) {
      cnt = Math.max(cnt, dp[j]);
    }
  }

  dp[i] += cnt;
}

answer = Math.max(...dp); // 큰 값으로 갱신

console.log(answer);

// IDEA
// 1. 점화식 세우기
// // 길이가 1일 때, [10] : 가장 긴 부분 수열의 길이는 1. dp[0]에 저장한다 (현재 dp = [1, ...])
// // 길이가 2일 때, [10, 20] : A[1] 이전의 숫자들과 비교한다. A[0] < A[1] 이므로 수열 성립가능하다. dp[1] = dp[0] + 1 (현재 dp = [1, 2 ...])
// // 길이가 3일 때. [10, 20, 10] : A[2] 이전의 숫자들과 비교한다. A[0] === A[2], A[1] > A[2] 이므로 수열 성립이 불가능하다. 현재 dp = [1, 2, 1 ...])
// // 길이가 4일 때. [10, 20, 10, 30] : A[3] 이전의 숫자들과 비교한다. A[0] < A[3], A[1] < A[3], A[2] < A[3] 이므로 수열 성립이 가능하다. 1, 2, 1 중 최댓값에 +1 하여 저장 (dp = [1, 2, 1, 3])
// 수열을 차례로 돌면서, 현재 순서보다 앞선 원소들과 값을 비교하여, 현재 원소가 더 크다면
// (비교 하고 있는) 앞선 원소들의 d[앞선 원소] 값을 구하고
// (dp[앞선 원소] 값들 중) 최댓값에 + 1 하여 dp[현재 원소] 의 값으로 지정한다.

// 2. dp 배열의 최댓값을 구하기
