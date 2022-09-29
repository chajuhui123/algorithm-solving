// 2470

let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

// const input = "5\n-2 4 -99 -1 98".split("\n");

const N = +input[0];
const arr = input[1]
  .split(" ")
  .map(Number)
  .sort((a, b) => a - b); // 투포인터 알고리즘 활용 전, 정렬

let start = 0; // 가장 앞쪽과
let end = N - 1; // 가장 뒷쪽부터 포인터 옮겨가며 체크

let sum = 0;
let answer = Infinity; // 가장 작은 수 (절댓값)
let answerPair = [0, 0]; // 가장 작은 수를 만드는 조합 저장

while (start < end) {
  sum = arr[start] + arr[end];

  if (Math.abs(sum) < answer) {
    // 나온 값 중 가장 작은 값으로 갱신시켜줌
    answer = Math.abs(sum);
    answerPair[0] = arr[start];
    answerPair[1] = arr[end];
  }

  if (sum === 0) {
    break; // 0인 경우가 최소이므로
  } else if (sum > 0) {
    end--; // sum 이 크면 수를 줄여야 하므로 end--
  } else if (sum < 0) {
    start++; // sum이 작으면 수를 키워야 하므로 start++
  }
}

console.log(answerPair.join(" "));
