// 2805

let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

// const input = "1 7\n20 15 10 17".split("\n");
// const input = "5 20\n4 42 40 26 46".split("\n");

// 입력되는 나무의 갯수 : N
// 가져가야할 나무의 높이 : M
const [N, M] = input[0].split(" ").map(Number);
// 주어진 나무 토막 : woods
const woods = input[1]
  .split(" ")
  .map(Number)
  .sort((a, b) => a - b);

let answer = 0;

let start = 0;
let end = woods[woods.length - 1];

while (start <= end) {
  let mid = Math.floor((start + end) / 2);
  let sum = 0; // 가져갈 수 있는 나무의 총 높이 (M과 비교)

  // 가져갈 수 있는 나무의 높이 구하기
  for (let wood of woods) {
    if (wood > mid) sum += wood - mid;
  }

  if (sum >= M) {
    // 최댓값 계속 구해주기.
    if (mid > answer) answer = mid;
    start = mid + 1;
  } else {
    end = mid - 1;
  }
}

console.log(answer);

// IDEA (이진탐색)
// 1. 정렬 (이진탐색을 활용하기 위해선 정렬 필요)
// 2. 중앙값 mid 구하기
// 3. mid 값을 기준으로 잘라진 나무의 합을 구하기 (단, 필요한 나무 값 M값이 나오면 return)
// 4. mid 값보다 잘라진 나무의 합이 크다면? (end = mid - 1)
// 5. mid 값보다 잘라진 나무의 합이 작다면? (start = mid + 1)

// -------------------------------------------------------------------------------------

// 다른 분의 코드
// 1. reduce 메서드를 활용해 잘라진 나무의 합을 한 줄로 표현한 게 인상 깊다.
// 2. 재귀 방식으로 이진 탐색을 구현한 것이 인상깊다.

// console.log(maxHeight(trees, 0, trees[N - 1]));

// function maxHeight(arr, start, end) {
//     const height = parseInt((start + end) / 2);
//     if (start > end)
//         return height;
//     const cutLength = arr.reduce((accu, pres) =>
//         pres > height ? accu + pres - height : accu + 0, 0);

//     if (cutLength >= M) {
//         return maxHeight(arr, height + 1, end);
//     } else {
//         return maxHeight(arr, start, height - 1);
//     }
// } // 재귀 방식으로
