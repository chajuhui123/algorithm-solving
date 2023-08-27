// https://leetcode.com/problems/container-with-most-water/description/

/**
 * @param {number[]} height
 * @return {number}
 */
const maxArea = function (height) {
  // 막대를 기준으로 가능한 너비를 구했을 때, 가장 큰 너비가 나오는 경우를 찾아보자
  // 간단하게 O(n^2) 으로 탐색하여 풀수 있으나, 시간 제한으로 인해 포인터 알고리즘으로 풀기로 결정
  let answer = 0;

  // 1. two pointer 사용을 위한 정의
  let left = 0;
  let right = height.length - 1;

  while (right - left > 0) {
    const x = right - left;
    // 2. 둘 중 더 작은 쪽을 y축 길이로 사용하기 (너비를 구해야하기 때문)
    const y = height[right] > height[left] ? height[left] : height[right];
    const width = x * y;

    // 3. y 에서 사용했던 값은 제외시키고 포인터 순환 (다른 막대들 비교를 위해)
    height[right] > height[left] ? left++ : right--;
    answer = answer < width ? width : answer;
  }

  return answer;
};
