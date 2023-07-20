/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
const twoSum = function (nums, target) {
  const N = nums.length;

  for (let i = 0; i < N; i++) {
    const value1 = nums[i];

    for (let j = i + 1; j < N; j++) {
      const value2 = nums[j];

      if (value1 + value2 === target) return [i, j];
    }
  }
};

// 후기

// 문제 이해하기
// 주어진 nums에서 2개의 숫자의 합이 target 인 조합의 인덱스를 리턴하는 문제

// 해결 방안
// i~N, i+1~N 의 합을 구해보며, 모든 조합을 탐색할 수 있다.
// 문제에서 1개의 답안만 리턴되는 것이 명시되어 있기에 for 문 안에서 바로 return 문을 작성할 수 있었다.
