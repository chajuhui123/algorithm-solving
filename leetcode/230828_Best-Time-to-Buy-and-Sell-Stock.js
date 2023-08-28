// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

/**
 * @param {number[]} prices
 * @return {number}
 */
const maxProfit = function (prices) {
  // 문제 컨셉: 제일 싸게 사고, 제일 비싸게 팔기 (Greedy?, Stack?, pointer? ...)
  // 유의해야할 점: 먼저 사야, 나중에 팔 수 있음. 해당 순서는 유지해야함.
  // 위를 쉽게 가능하게 하기 위해 포인터 활용

  let answer = 0;

  let left = 0; // buy
  let right = 1; // sell

  while (right < prices.length) {
    if (prices[left] < prices[right]) {
      let profit = prices[right] - prices[left];
      answer = Math.max(answer, profit);
    } else {
      left = right;
    }
    right++;
  }

  return answer;
};

// 후기

// 문제 이해하기
// 주어진 prices 에서 최대의 이윤을 낼 수 있는 케이스의 값을 리턴하기. 제일 싸게 사고, 제일 비싸게 팔기 (Greedy?, Stack?, pointer? ...)
// 유의해야할 점은 '순서'이다. 먼저 사야 이후에 팔 수 있다. 해당 순서는 유지해야한다.
// 위를 간단하게 해결하기 위해 '포인터'를 활용한다.

// 해결 방안

// 예를 들어 [7,1,5,3,6,4] 이라는 prices가 주어지면 사고 파는 순서를 유지하기 위해 left=0 right=1로 둔다 (left는 사는 가격 인덱스, right 파는 가격 인덱스)
// 1단계. 7, 1 이다. 7에 사고 1에 팔면 손해이기 때문에, left 포인터를 right 포인터 위치로 옮긴다. 이후에 right 포인터는 +1을 해준다. (1, 5 가 된다)
// 2단계. 1, 5 이다. 1에 사고 5에 팔면 이득이다. 최대값을 갱신해준다 max(max, now). right 포인터를 +1 해준다. (1, 3이 된다)
// 3단계. 1, 3 이다. 1에 사고 3에 팔면 이득이다. 최대값을 큰 값으로 갱신해준다.  right 포인터를 +1 해준다. (1, 6가 된다)
// 4단계. 1, 6 이다. 1에 사고 6에 팔면 이득이다. 최대값 갱신 후, right 포인터 +1을 한다 (1, 4가 된다)
// 5단계 1, 4 이다. 현재도 이득이고 갱신 가능하다. right가 마지막 값에 도달하여 탐색이 중단된다.

// 1. 사고, 파는 순서 유지를 위해 pointer 활용한다.
// 2. right < prices.length 까지 아래를 반복한다.
// 2-1. 현재 가리키고 있는 두 값이 이득이라면, 최댓값 갱신한다.
// 2-2. 현재 가리키고 있는 두 값이 이득이 아니라면, left 의 위치를 right의 위치로 옮겨준다.
// 2-3. 다음 탐색을 위해 right 포인터를 +1 해준다.

// 결론
// O(N) 으로 해당 문제를 해결할 수 있다.
