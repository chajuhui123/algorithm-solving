// 동적 계획법 (Dynamic Programming)
// https://leetcode.com/problems/house-robber

/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function (nums, idx = 0, memo = {}) {
  // key (값에 방문한 집 번호) : value (해당 집 번호 털었을 때까지의 비용)
  if (idx in memo) return memo[idx];
  if (idx >= nums.length) return 0;

  // 2가지 선택지가 가능함
  // 1. 현재 집을 건너뛰기
  const sumIfSkipped = rob(nums, idx + 1, memo);
  // 2. 집을 털기 (바로 옆 집은 못 털기 때문에 idx+2)
  const sumIfRobbed = nums[idx] + rob(nums, idx + 2, memo);

  return (memo[idx] = Math.max(sumIfSkipped, sumIfRobbed));
};

// 후기

// 1️⃣ 문제 이해하기
// DP 문제에 접근 방법은 <1. 재귀적인 전략 떠올리기 -> 2. 메모화 전략 세우기 -> 3. 최적화> 로 정리할 수 있다.
// 이번 문제 풀이에서는 이 순서대로 문제를 접근해보았다.

// 2️⃣ 해결 방안
// 아래는 <재귀적인 전략을 떠올리기> 방식으로 문제를 해결하였다.
// 의도하는 값은 리턴하지만 중복의 연산이 반복되기 때문에 시간 초과 문제가 발생한다. <각 인덱스에서 동일한 연산 반복>
// 메모화 전략을 세워 시간 초과 문제를 해결해본다.

var rob_2 = function (nums, idx = 0) {
  if (idx >= nums.length) return 0;

  const sumIfSkipped = rob_2(nums, idx + 1);
  const sumIfRobbed = nums[idx] + rob_2(nums, idx + 2);

  return Math.max(sumIfSkipped, sumIfRobbed);
};

// 메모화 전략을 세워 제출한 것이 위에 첨부된 답안 코드이다.
// 여전히 재귀 방식을 사용하고 있는데, 더 개선하기 위해 반복문을 사용하는 방식으로 개선 가능하다.
// 1. i번째 집을 건너뛰기로 결정한다면, i+1의 집에서 시작하여 가능한 최대값을 계산한다.
// 2. i에서 집을 털기로 결정하면, i+2에서 집을 시작으로 가능한 최대값을 계산한다.
// 위 로직을 DP 테이블을 구성하고, 오른쪽에서 왼쪽으로 반복한다. '상향식 접근법'이라고 할 수 있다.

var rob_3 = function (nums) {
  const table = new Array(nums.length + 2);

  table[nums.length + 0] = 0;
  table[nums.length + 1] = 0;

  for (let i = nums.length - 1; i >= 0; i--) {
    const sumIfSkipped = table[i + 1];
    const sumIfRobbed = nums[i] + table[i + 2];

    table[i] = Math.max(sumIfSkipped, sumIfRobbed);
  }

  return table[0];
};

// 3️⃣ 결론
// DP 문제는 <1. 재귀적인 전략 떠올리기 -> 2. 메모화 전략 세우기 -> 3. 최적화> 의 과정으로 문제 해결법을 떠올려보자
