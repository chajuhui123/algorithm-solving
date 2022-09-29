//3036

let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

// const input = "3\n8 4 2".split("\n");
// const input = "4\n12 3 8 4".split("\n");
// const input = "4\n300 1 1 300".split("\n");

const N = +input[0];

const rings = input[1].split(" ").map(Number);
const firstRing = rings.shift();

const answer = [];

// 유클리드 호제법을 활용한, 최대 공약수 (a>b)
const gcd = (a, b) => {
  if (b === 0) return a; // 나누어지면 a 리턴
  return gcd(b, a % b); // 나누어지지 않는다면 b와 a % b를 다시 나누기
};

for (let ring of rings) {
  const divisor = gcd(firstRing, ring);
  answer.push(`${firstRing / divisor}/${ring / divisor}`);
}

console.log(answer.join("\n"));

// IDEA
// 1. 유클리드 호제법을 사용하여 최대 공약수를 만들 수 있다.
// 2. 참고로 최소 공배수는 `(a*b)*최대공약수`로 구할 수 있다.
