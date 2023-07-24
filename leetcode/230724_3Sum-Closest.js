// https://leetcode.com/problems/3sum-closest

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function (nums, target) {
  // 1. 3 <= nums.length 라는 조건이 있기에, result는 다음과 같이 초기화
  let result = nums[0] + nums[1] + nums[nums.length - 1];

  // 2. 포인터 활용을 위한 오름차순 정렬
  nums.sort((a, b) => a - b);

  for (let i = 0; i < nums.length - 2; i++) {
    // 3. i를 기준으로 start, end 포인터 셋팅
    let start = i + 1;
    let end = nums.length - 1;

    while (start < end) {
      // 4. 포인터를 기준으로 임시의 sum 구하기
      let sum = nums[i] + nums[start] + nums[end];

      if (sum > target) {
        // 5. 해당 케이스에서의 합이 구하고자 하는 target 보다 큰 경우, end--
        end--;
      } else {
        // 6. 해당 케이스에서의 합이 구하고자 하는 target 보다 작거나 같은 경우, start++
        start++;
      }

      // 7. 해당 문제는 target과 같거나 가장 작은 차이를 가지는 3개의 수의 합을 구하는 문제이므로,
      // 현재 케이스에서의 target과의 차이가 이전 케이스에서의 target과의 차이보다 작은 경우, result 변경
      if (Math.abs(sum - target) < Math.abs(result - target)) {
        result = sum;
      }
    }
  }
  return result;
};

// 후기

// 문제 이해하기
// target과 같거나 가장 작은 차이를 가지는 3개의 수의 합을 구하는 문제이다.
// 정렬, 포인터를 활용하여 문제를 해결할 수 있다.
// 정렬된 리스트에서 포인터를 활용하여, 임의의 3개 수의 합을 구한 후,
// 타겟과 같거나 가장 차이가 적은 3sum 조합의 합을 답으로 리턴한다.

// 해결 방안
// 1. 3Sum 정의. 다음과 같이 정리할 수 있다.
//   - nums[기준 인덱스], 포인터를 활용하여 nums[기준 인덱스+1] ~ nums[nums.length -1] 탐색
//   - 3 <= nums.length 라는 조건이 있기에 가능하다
//   - 따라서 첫 초기화 값은 nums[0] + nums[1] + nums[nums.length - 1] 로 셋팅하였다.
// 2. 포인터 활용을 위해 오름차순 정렬
//   - 포인터를 활용하여 target 값과 3Sum 값을 비교할 예정이다.
// 3. i~nums.length-2 까지 탐색한다
//   - 1번에서 정의한 3sum에 따라, 포인터를 통해 target 값과 비교한다.
// 4. target과 가장 차이가 적거나 같은 result 갱신
//   - 유의할 점은 차이는 절댓값 (Math.abs) 으로 구해야한다.

// 결론
// O(n^2) 으로 해결할 수 있다.
