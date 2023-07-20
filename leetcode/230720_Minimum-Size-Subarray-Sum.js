// https://leetcode.com/problems/minimum-size-subarray-sum

/**
 * @param {number} target
 * @param {number[]} nums
 * @return {number}
 */
const minSubArrayLen = function (target, nums) {
  let res = [];

  let sum = 0;
  let startIdx = 0;

  for (let idx = 0; idx < nums.length; idx++) {
    sum += nums[idx];

    while (sum >= target) {
      res.push(idx - startIdx + 1); // 현재 더해진 수의 갯수
      sum -= nums[startIdx]; // 시작 값을 빼주고
      startIdx++; // 다시 start 기준으로 index++ 하여 탐색
    }
  }

  return res.length ? Math.min(...res) : 0;
};
