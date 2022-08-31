// let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const input = "8 3\n1 5 4 6 2 1 3 7".split("\n");

// N : N개의 수로 이루어진 1차원 배열이 주어짐
// M : M개 이하의 구간으로 나누기
const [N, M] = input[0].split(" ").map(Number);
const array = input[1].split(" ").map(Number);

const divide = (x) => {
  let maxX = array[0];
  let minX = array[0];
  let count = 1;

  for (let i = 1; i < N; i++) {
    maxX = Math.max(maxX, array[i]);
    minX = Math.max(minX, array[i]);

    if (maxX - minX > x) {
      count++;
      maxX = array[i];
      minX = array[i];
    }
  }

  return count;
};

let result = 0;

let start = 0;
let end = Math.max(...array);

while (start <= end) {
  let mid = parseInt((start + end) / 2);
  console.log(mid);

  if (divide(mid) <= M) {
    end = mid - 1;
    result = mid;
    console.log(result);
  } else {
    start = mid + 1;
  }
}

console.log(result);
