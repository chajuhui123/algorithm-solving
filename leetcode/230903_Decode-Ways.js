// 동적 계획법 (Dynamic Programming)
// https://leetcode.com/problems/decode-ways

/**
 * @param {string} s
 * @return {number}
 */
var numDecodings = function (s) {
  // 1. A~Z 에 대한 code 값 저장
  const decoder = {};
  for (let c = 65; c <= 90; c++) {
    decoder[c - 64] = String.fromCharCode(c);
  }

  // 2. 특정 지점까지 몇 개의 조합이 있는지 dp를 활용하여 저장
  let dp = new Array(s.length + 1).fill(0);
  dp[0] = 1;

  for (let i = 1; i <= s.length; i++) {
    for (let j = 0; j <= i - 1; j++) {
      const sub = s.substring(j, i);
      if (sub in decoder) dp[i] += dp[j];
    }
  }

  return dp[dp.length - 1];
};

// 후기

// 1️⃣ 문제 이해하기
// dp의 메모이제이션을 사용하여 특정 지점까지 얼마나 많은 조합이 있는지 누적해나가자!

// 2️⃣ 해결 방안
// 예를 들어 226이라고 해보자.

// i=1 인 경우,
// 1. j=0 -> sub = 2, dp[1] += dp[0] (1)

// i=2 인 경우
// 1. j=1 -> sub = 2, dp[2] += dp[1] (1)
// 2. j=0 -> sub = 22, dp[2] += dp[0] (2)

// i=3 인 경우
// 1. j=2 -> sub= 6, dp[3] += dp[2] (2)
// 2. j=1 -> sub= 26 O dp[3] += dp[1] (1)
// 3. j=0 -> sub= 226

// 최종 dp[3] = 3

// 3️⃣ 결론
