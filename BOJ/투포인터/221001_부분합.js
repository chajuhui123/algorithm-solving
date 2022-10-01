// 1806

let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

// const input = "10 15\n5 1 3 5 10 7 4 9 2 8".split("\n");

// N : arr 길이
// S : S 이상의 부분합을 가져함
const [N, S] = input[0].split(" ").map(Number);
const arr = input[1].split(" ").map(Number);

// 포인터 정의
let left = 0;
let right = 0;
let sum = 0;

// 구간 길이의 최소값 저장
let answer = Infinity;

while (left <= right) {
  if (sum >= S) {
    answer = Math.min(answer, right - left);
    sum -= arr[left];
    left++;
  } else if (right === N) {
    break;
  } else {
    sum += arr[right];
    right++;
  }
}

answer === Infinity ? console.log(0) : console.log(answer);

// IDEA
// 1. sum >= S 인 경우, 구간합이 m 이상되는 구간
// // answer 에 Math.min함수를 통하여 작은 구간의 길이를 저장
// // 최소구간을 찾아야하므로 arr[left]값을 sum에서 빼고 left 포인터를 1증가시킴 (다음 구간의 시작으로 이동)
// 2. right 포인터가 N이 되면 끝까지 탐색한 것이므로 종료
// 3. sum < S 인 경우, right 포인터를 증가시키면서 sum값에 더함
