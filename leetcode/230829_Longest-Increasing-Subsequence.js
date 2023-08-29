// 동적 계획법 (Dynamic Programming)
// https://leetcode.com/problems/longest-increasing-subsequence

/**
 * @param {number[]} nums
 * @return {number}
 */
const lengthOfLIS = function (nums) {
  // 최장으로 증가하는 구간의 값 갯수을 구해봅시다
  // 유의: 얼마나 많이 증가하는지가 아니라, 증가만 한다면 구간의 갯수를 늘려주는 것임

  const N = nums.length;
  // 1. 기본값은 1을 가지도록함 (구간의 갯수이기 때문에, 1이 최소값 (== 증가하는 구간 없음))
  let dp = new Array(N).fill(1);

  for (let i = 1; i < N; i++) {
    for (let j = 0; j < i; j++) {
      if (nums[j] < nums[i]) {
        // 2. j에서 i까지 증가하는 구간 갯수 누적시키기
        dp[i] = Math.max(dp[i], dp[j] + 1);
      }
    }
  }

  // 3. 가장 긴 구간 갯수 리턴
  return Math.max(...dp);
};
