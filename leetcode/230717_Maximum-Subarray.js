// https://leetcode.com/problems/maximum-subarray/description/

/**
 * @param {number[]} nums
 * @return {number}
 */
let maxSubArray = function (nums) {
  const N = nums.length;
  const cache = Array.from({ length: N }, () => 0);
  cache[0] = nums[0];

  // 연속된 숫자의 부분합 중 가장 큰 값을 구하는 문제
  // 구간 별로 합을 구해야하기에 O(n^2) 로직을 활용할 수도 있으나
  // 문제에는 O(n) 안에 끝내는 것이 목표이다. 이럴 땐 동적 계획법을 활용하여 부분합을 구할 수 있다.
  for (let i = 1; i < N; i++) {
    cache[i] = Math.max(0, cache[i - 1]) + nums[i];
  }

  return Math.max(...cache);
};
