function solution(x, y, n) {
  if (x == y) return 0;

  const dp = Array(y + 1).fill(Infinity);

  dp[x] = 0;

  // x to y 순환하며, 해당 숫자를 만들기 위한 연산 횟수를 저장
  for (let i = x + 1; i <= y; i++) {
    // n 더하는 경우
    if (x <= i - n) {
      dp[i] = Math.min(dp[i], dp[i - n] + 1);
    }

    // 2 곱하는 경우
    if (i % 2 === 0 && x <= i / 2) {
      dp[i] = Math.min(dp[i], dp[i / 2] + 1);
    }

    // 3 곱하는 경우
    if (i % 3 === 0 && x <= i / 3) {
      dp[i] = Math.min(dp[i], dp[i / 3] + 1);
    }
  }

  return dp[y] === Infinity ? -1 : dp[y];
}
