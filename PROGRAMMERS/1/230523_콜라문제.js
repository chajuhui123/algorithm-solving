function solution(a, b, n) {
  let changeCount = 0;

  // 교환 불가할 때까지 반복
  while (n >= a) {
    changeCount += Math.floor(n / a) * b;
    n = Math.floor(n / a) * b + (n % a);
  }

  return changeCount;
}
