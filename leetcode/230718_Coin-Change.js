// https://leetcode.com/problems/coin-change
// 소요시간 26m

/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
let coinChange = function (coins, amount) {
  // 0~amount 까지 coins 의 조합을 통해 각 amount 를 나타낼 수 있는 양
  let dp = Array(amount + 1).fill(amount + 1);

  // 음수, 0에 대한 예외 처리
  if (amount < 0) return -1;
  if (amount === 0) return 0;

  dp[0] = 0; // 0을 만드는 횟수는 0이므로

  for (let i = 1; i <= amount; i++) {
    for (let j = 0; j < coins.length; j++) {
      if (i >= coins[j]) {
        dp[i] = Math.min(dp[i], dp[i - coins[j]] + 1);
      }
    }
  }

  return dp[amount] > amount ? -1 : dp[amount]; // min값으로 초기화 되지 않았다면 -1 return
};

// 후기

// 문제 이해하기
// 주어진 coins를 활용해 amount를 나타낼 수 있는 케이스가 몇 개인지를 묻는 문제이다.
// 예를 들어 amount = 5, coins = [1,2,5] 일때, '5 = 5', '5 = 2+2+1', '5 = 2+1+1+1', '5 = 1+1+1+1+1' 로 4가지

// 해결 방안
// 해당 문제는 DP로 접근할 수 있다. DP 로 해결시 O(amount*coin) 정도의 시간 복잡도로 해결할 수 있다.
