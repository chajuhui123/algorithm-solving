// Product of Array Except Self

/**
 * @param {number[]} nums
 * @return {number[]}
 */
let productExceptSelf = function (nums) {
  const n = nums.length;
  const preFix = Array.from({ length: n + 1 }, () => 1);
  const postFix = Array.from({ length: n + 1 }, () => 1);

  for (let i = 0; i < nums.length; i++) {
    preFix[i + 1] = nums[i] * preFix[i];
  }

  for (let i = n - 1; i >= 0; i--) {
    postFix[i] = nums[i] * postFix[i + 1];
  }

  const answer = [];

  for (let i = 0; i < n; i++) answer.push(preFix[i] * postFix[i + 1]);

  return answer;
};

// 후기

// 문제 이해하기
// 주어진 nums와 같은 길이의 answer 배열을 리턴하는데, answer[i]에는 nums[i]를 제외한 나머지 값들의 곱이 담겨있어야 한다.
// O(n) 시간 복잡도를 가져야 하고, '나누기'를 사용하지 않아야 한다.

// 해결 방안
// 1. 모든 index 값들의 곱을 구하고 O(n)으로 순환하며 나누기 연산을 하는 것 (하지만, 나누기 연산 사용 금지 제한에 걸림)
// 2. nums를 순환하며, i번째 인덱스 제외한 값들을 곱해주고 저장하기 (하지만, O(n^2) 이므로 복잡도 제한에 걸림)
// 3. 필요한 값에 집중하는 경우
// i 번째 인덱스의 값을 구하기 위해선 어떻게 해야할까?
// i-1 번쨰까지 인덱스들의 곱이 필요하고, i+1 이후 인덱스들의 곱이 필요하다. 그렇다면 두가지 배열을 만들어 놓고 활용하는 로직으로 해당 문제를 해결할 수 있다.
// answer[i] = prefix[i - 1] * postfix[i + 1] 공식이 성립하도록 prefix, postfix 값을 선언하였다.

// 결론
// O(N) 으로 해당 문제를 해결할 수 있다.
