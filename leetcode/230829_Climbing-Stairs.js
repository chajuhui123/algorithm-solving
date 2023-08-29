// 동적 계획법 (Dynamic Programming)
// https://leetcode.com/problems/climbing-stairs/description/

let memo = [];

/**
 * @param {number} n
 * @return {number}
 */
const climbStairs = function (n) {
  if (n <= 2) return n;
  if (memo[n] != undefined) return memo[n];

  // 동적 계획 방식으로 (1 or 2 칸씩 올라갈 수 있음)
  memo[n] = climbStairs(n - 1) + climbStairs(n - 2);
  return memo[n];
};
