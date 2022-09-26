// 1654

let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

// const input = "4 11\n802\n743\n457\n539".split("\n");

// 주어진 케이블의 갯수 : K
// 만들고자 하는 케이블의 갯수 : N (N개 이상 만들고자 함)
const [K, N] = input.shift().split(" ").map(Number);
const cables = input.map(Number).sort((a, b) => a - b);

let start = 0;
let end = cables[cables.length - 1];

while (start <= end) {
  let mid = Math.floor((start + end) / 2); // 내림
  let lineNum = cables.reduce((acc, cur) => acc + Math.floor(cur / mid), 0);
  // Q. Math.floor VS parsInt : Math.floor 연산이 더 빠르다고 한다. 이거때문에 처음에 틀렸나...?

  // Q. 차이를 뽑자면, 음수일 때의 둘의 연산이 다르다.
  // Math.floor 메서드는 소수 첫째 자리에서 양수일 때처럼 내림하는 반면
  // parseInt 메서드는 올림한다. parseInt 메서드는 소수점을 버리기 때문!
  // 근데 문제에선 양수만 주어질텐데 왜 차이가 있지 ㅠ

  if (lineNum >= N) {
    start = mid + 1;
  } else {
    end = mid - 1;
  }
}

console.log(end); // 목표인 N 개의 랜선을 만들 수 있는 경우에서, end는 가장 큰 값이 보장됨 (start 부분을 늘리기 때문)

// IDEA (이진탐색)
// 1. 정렬 (이진탐색을 활용하기 위해선 정렬 필요)
// 2. 중앙값 mid 구하기
// 3. mid 값을 기준으로 만들어지는 갯수를 구하기
// 4. 3번에서 구한 갯수가 목표인 N보다 크거나 같다면? (start = mid + 1, 더 큰 값의 범위에서 탐색해보기)
// 5. 3번에서 구한 갯수가 목표인 N보다 작다면? (end = mid - 1, 더 작은 값의 범위에서 탐색해보기)
