// 피보나치 수열을 이용하자!
// (n+2 칸을 뛰는 방법) = (n+1 칸을 뛰는 방법) + (n 칸을 뛰는 방법)

function solution(n) {
  return fibonacci(n);
}

function fibonacci(n) {
  const dp = new Array(n + 1).fill(0);

  dp[0] = 1;
  dp[1] = 1;

  for (let i = 2; i <= n; i++) dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567;

  return dp[n];
}
