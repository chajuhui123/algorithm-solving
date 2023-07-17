/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
  // 1. 오름차순 정렬
  nums.sort((a, b) => a - b);

  // 2. 오름차순 정렬시, 양수 이후 부터는 시작 값으로 순환할 필요가 없기에 첫 양수 인덱스를 구해줌
  const lastIdx = nums.findIndex((num) => num > 0);

  // 3. 양수가 존재하지 않는다면 [0, 0, 0] 이외에는 답이 될 수 없으므로 예외처리
  if (lastIdx === -1) {
    if (nums.filter((num) => num == 0).length >= 3) return [[0, 0, 0]];
    return [];
  }

  const answer = [];
  const N = nums.length;

  for (let i = 0; i < lastIdx; i++) {
    // 4. 이전 값과 같은 target 인 경우, 연산 넘김
    if (i > 0 && nums[i] === nums[i - 1]) continue;

    const target = nums[i];
    let left = i + 1;
    let right = N - 1;

    while (left < right) {
      const sum = target + nums[left] + nums[right];
      if (sum > 0) {
        right--;
      } else if (sum < 0) {
        left++;
      } else {
        answer.push([target, nums[left], nums[right]]);
        right--;
        left++;

        // 5. 중복 answer 방지를 위해, 이전 값과 같은 경우 넘어감
        while (left < right && nums[left] === nums[left - 1]) left++;
        while (left < right && nums[right] === nums[right + 1]) right--;
      }
    }
  }

  return answer;
};

// 후기

// 문제 이해하기
// 주어진 nums 배열 중 3개의 값을 선택하여 합이 0이 되게 만드는 조합을 리턴하는 문제이다. 단 중복된 값은 허용하지 않는다!
// 0이 되기 위해선 음수, 양수 조합을 더하거나, [0,0,0] 만 정답 후보가 될 수 있다.
// 음수만 존재한다거나, 0이상의 양수만 존재한다면 [] 을 리턴해야할 것이다.

// 시간 복잡도
// 처음에는 단순하게 0을 만드는 모든 조합을 구하고, 중복을 제거하여 답을 리턴하는 것이 어떨까 생각하였다.
// 문제 조건에 따르면 nums의 갯수가 3000개까지가 가능하다. 따라서 O(N^2)에 대해서 9,000,000 연산으로 시간 초과를 일으키진 않을 것이다.
// 하지만 O(N^3) 이라면 270억... 연산으로 시간 초과 문제를 발생할 것이다. 따라서 해당 문제는 O(N^2) 혹은 O(N^2 * logN) 안에서 해결해야 한다.
// 따라서 처음에 생각한 방안은 O(N^3) 복잡도를 가지기 때문에 잘못된 설계였다.

// 해결 방안
// 정렬, 투 포인터를 활용하여 해당 문제를 해결하고자 했다.
// 1. 오름차순 정렬을 하게 되면 [음수~양수] 순서가 보장된다. 따라서 특정 타겟값을 선정하고, 포인터를 활용해 타겟값과 더했을 때 0이 되는 2개의 value를 순차적으로 구하고자 한다.
// 예를 들어 [-4, -1, -1, 0, 1, 2] 가 주어졌을 때, 타겟이 -4 이면 나머지 합이 4가 되도록 만들어야 한다. -1 + 2는 1 인데, 보다 큰 양수가 없으므로 다음 타겟으로 넘어간다.
// 타겟이 -1 일때, 나머지 합이 1이 되면 된다 -1 + 2는 1이므로 [-1, -1, 2] 는 정답 후보가 된다. 이런식으로 포인터를 이동해가며 답안을 구한다.
// 2. 해당 로직을 의사 코드로 작성하면...
// 0 === sums[target] + sums[left] + sums[right] 이면 답안. 해당 값을 저장 후 left++ right--
// 0 > sums[target] + sums[left] + sums[right] 라면 값이 작은 것이므로 left++
// 0 < sums[target] + sums[left] + sums[right] 라면 값이 큰 것이므로 값을 right--
// 3. 단, 해당 로직에서 문제점은 이전 값과 타겟이 같은 경우, 포인터로 가리키게 되는 값이 이전 값과 같은 경우, 중복을 발생시키고 무한루프를 발생시킬 수 있어 예외 처리가 필요하다.

// 결론
// O(N^2) 으로 해당 문제를 해결할 수 있다.
