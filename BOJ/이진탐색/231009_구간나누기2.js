// https://www.acmicpc.net/problem/13397

let fs = require("fs");
let input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "test.txt")
  .toString()
  .trim()
  .split("\n");

function canDivide(arr, M, score) {
  let count = 1; // 구간 갯수
  let minVal = arr[0];
  let maxVal = arr[0];

  for (let i = 1; i < arr.length; i++) {
    // 구간에서 가장 작은 값과 큰 값
    minVal = Math.min(minVal, arr[i]);
    maxVal = Math.max(maxVal, arr[i]);

    // (max_x - min_x)의 값이 score 보다 크다면 구간이 하나 만들어짐
    if (maxVal - minVal > score) {
      count++;
      minVal = arr[i];
      maxVal = arr[i];
    }
  }
  return count <= M;
}

function solution(M, arr) {
  let result = 0;

  let left = 0;
  let right = Math.max(...arr);

  while (left <= right) {
    let mid = Math.floor((left + right) / 2);

    if (canDivide(arr, M, mid)) {
      // 해당 mid 점수로 구간의 최대 갯수에 만족한다면
      result = mid;
      right = mid - 1;
    } else {
      // 만족하지 못한다면
      left = mid + 1;
    }
  }

  return result;
}

const M = Number(input.shift().split(" ")[1]);
const arr = input.shift().split(" ").map(Number);

console.log(solution(M, arr));

// 풀이

// 문제 이해하기

// 구하고자 하는 값 : 각 구간의 (최댓값-최솟값)의 최댓값 중에 최솟값
// 예를 들어 arr = [1, 5, 4, 6, 2, 1, 3, 7] 이고, M = 3인 경우,
// [1, 5], [4, 6, 2], [1, 3, 7] 로 구간을 나누면 각 구간의 점수(최댓값-최솟값)는 4, 4, 6, 이때 최댓값 6
// [1, 5, 4], [6, 2, 1], [3, 7] 로 구간을 나누면, 각 구간의 점수 3, 5, 4, 이때 최댓값 5
// 최댓값 6,5 중 작은 것은 5, 따라서 최종 정답은 5
