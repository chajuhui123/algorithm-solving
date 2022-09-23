// 3273

let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

// const input = "9\n5 12 7 10 9 1 2 3 11\n13".split("\n");
// const input = "1\n2\n4".split("\n");

const N = +input[0];
// 오름차순 정렬한 수열 numbers (서로 다른 양의 정수로 이루어짐)
const numbers = input[1]
  .split(" ")
  .map(Number)
  .sort((a, b) => a - b);
const targetX = +input[2];

let start = 0;
let end = numbers.length - 1;
let answer = 0;

while (start != end) {
  if (numbers[start] + numbers[end] == targetX) {
    answer++;
    start++; // 다음 포인터에서 탐색
  } else if (numbers[start] + numbers[end] > targetX) {
    end--; // 타겟보다 합이 더 크다면 오른쪽에 있는 포인터를 왼쪽으로 (합이 더 작아져야 함)
  } else {
    start++; // 타겟보다 합이 더 작다면 왼쪽에 있는 포인터를 오른쪽으로 (합이 더 커져야 함)
  }
}

console.log(answer);

// 투 포인터 문제로 서로 다른 양의 정수로 이루어진 배열이 주어진다.
// 왼쪽부터 탐색하는 포인터, 오른쪽부터 탐색하는 포인터가 가리키는 숫자를 이용하여, target 숫자를 만드는 쌍을 찾는다.
