// 동적 계획법 (Dynamic Programming)
// https://leetcode.com/problems/combination-sum-iv

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var combinationSum4 = function (nums, target) {
  let dp = new Uint32Array(target + 1); // 각 자리의 숫자를 만드는 조합 갯수 저장하기

  dp[0] = 1;

  for (let i = 1; i <= target; i++) {
    for (let num of nums) {
      if (num <= i) dp[i] += dp[i - num];
    }
  }

  return dp[target];
};

// 후기

// 문제 이해하기
// 주어진 nums로 target 이라는 숫자를 만들 수 있는 조합의 갯수를 리턴하기

// 해결 방안

// 1~target 까지 숫자를 1씩 증가하면서, 해당 숫자를 만들 수 있는 조합의 갯수를 더해준다.
// 단, "answer can fit in a 32-bit integer." 이라는 조건에 맞춰 answer를 <Uint32Array> 배열을 생성하여 저장하였다.

// 예시
// 1, 2, 3
// 1 => dp[1] = dp[1-1] = dp[0] = 1;
// 2 => dp[2] = dp[2-1] + dp[2-2] = dp[1] + dp[0] = 1 + 1 = 2;
// 3 => dp[3] = dp[3-1] + dp[3-2] + dp[3-3] = dp[2] + dp[1] + dp[1] = 2 + 1 + 1 = 4;
// 4 => dp[4] = dp[4-1] + dp[4-2] + dp[4-3] = dp[3] + dp[2] + dp[1] = 4 + 2 + 1 = 7;
