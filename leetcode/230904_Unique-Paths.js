// 동적 계획법 (Dynamic Programming)
// https://leetcode.com/problems/unique-paths/

/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
const uniquePaths = function (m, n) {
  // 아래 혹은 오른쪽으로 밖에 이동하지 못한다.
  // [0][0] -> [n-1][n-1] 로 이동

  const dp = Array.from({ length: m }, () => Array(n).fill(0));

  for (let i = 0; i < m; ++i) {
    dp[i][0] = 1;
  }
  for (let j = 0; j < n; ++j) {
    dp[0][j] = 1;
  }

  for (let i = 1; i < m; ++i) {
    for (let j = 1; j < n; ++j) {
      dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
    }
  }

  return dp[m - 1][n - 1];
};
