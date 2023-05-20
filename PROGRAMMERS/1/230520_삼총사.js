function solution(number) {
  let count = 0;

  // 3명의 합이 0인 경우 삼총사, 가능한 케이스를 모두 따져본다 (3중 for문)
  for (let i = 0; i < number.length; i++) {
    for (let j = i + 1; j < number.length; j++) {
      for (let k = j + 1; k < number.length; k++) {
        if (number[i] + number[j] + number[k] === 0) count++;
      }
    }
  }

  return count;
}
