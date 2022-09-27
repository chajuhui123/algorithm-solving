//10844

let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim();

// const input = '1';
// const input = "2";

const N = +input;
const DIVISION = 1000000000;

// N === 1인 경우 각 자리에서 계단 수가 몇인지 dp에 저장
let dp = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1]];
for (let i = 1; i < N; i++) dp.push([...Array(10)]);

// (N>=2 인 경우) dp 패러다임 활용하여 각 자리수에 저장되어 있는 계단 수 활용해 값을 갱신시켜나감
for (let i = 1; i < N; i++) {
  for (let j = 0; j <= 9; j++) {
    dp[i][j] = (dp[i - 1][j - 1] || 0) + ((dp[i - 1][j + 1] || 0) % DIVISION);
  }
}

// dp N-1 줄에 해당하는 계단 수를 result에 저장
const result = dp[N - 1].reduce((acc, i) => {
  return (acc + i) % DIVISION;
}, 0);

console.log(result);

// 다이나믹 프로그래밍(=동적 계획법) 은 '기억한 해로 풀어나가기'라고 정리할 수 있다.
// 최적화 이론의 한 기술이며, 특정 범위까지의 값을 구하기 위해서 그것과 다른 범위까지의 값을 이용하여 효율적으로 값을 구하는 알고리즘 설계 기법이다.
// 답을 재활용하는 거다. 동적 계획법은 "어떤 문제를 풀기 위해 그 문제를 더 작은 문제의 연장선으로 생각하고, 과거에 구한 해를 활용하는" 방식의 알고리즘을 총칭한다.
