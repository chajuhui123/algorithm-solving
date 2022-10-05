// Run by Node.js
const readline = require("readline");

(async () => {
  let rl = readline.createInterface({ input: process.stdin });

  const input = [];
  let answer = 0;

  for await (const line of rl) input.push(line);

  // 소수 판별 isPrime
  const isPrime = (num) => {
    // 소수는 1과 자기 자신만으로만 나누어 떨어지는 수, num > i
    for (let i = 2; num > i; i++) {
      // 이 로직에서 num이 다른 수로 나눠떨어진다면, 소수가 아님
      if (num % i === 0) return false;
    }
    // 소수는 1보다 큰 정수임으로 1보다 작으면 false를 리턴
    return num > 1;
  };

  const solution = () => {
    const N = +input[0];
    const nums = input[1].split(" ").map(Number);

    for (let i = 0; i < N; i++) {
      if (isPrime(i + 1)) {
        // index 1부터 세짐
        answer += nums[i];
      }
    }

    console.log(answer);
  };

  solution();
  process.exit();
})();
