// 동적 계획법 (Dynamic Programming)
// https://leetcode.com/problems/jump-game

/**
 * 각 인덱스에 저장된 숫자만큼 점프할 수 있을 때, 마지막 인덱스에 도달할 수 있는지 여부를 return 하는 함수
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function (nums) {
  // 1. DP 배열에 해당 칸에 도달할 수 있는지 여부 저장
  let dp = Array.from({ length: nums.length }, () => false);

  // 2. 첫 칸은 갈 수 있음
  dp[0] = true;

  // 3. 마지막 칸 이전까지 탐색
  for (let i = 0; i < nums.length - 1; i++) {
    // 4. 도달할 수 있는 칸에 대해서, 몇 칸 더 점프할 수 있는지 탐색한 후, dp에 저장해줌
    if (dp[i] === true) {
      for (let jump = 1; jump <= nums[i]; jump++) {
        const nextStep = i + jump;

        if (nextStep < nums.length) {
          dp[nextStep] = true;
        }
      }
    }
  }

  // 5. 최종칸에 도달 가능한지 여부 리턴
  return dp[dp.length - 1];
};
