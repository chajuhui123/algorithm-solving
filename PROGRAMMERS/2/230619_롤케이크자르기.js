function solution(topping) {
  const mine = new Set();
  const yours = {};

  let answer = 0;
  let check = 0;

  for (let i = 0; i < topping.length; i++) {
    if (yours[topping[i]]) {
      yours[topping[i]]++;
    } else {
      yours[topping[i]] = 1;
      check++;
    }
  }

  for (let i = 0; i < topping.length; i++) {
    mine.add(topping[i]);
    yours[topping[i]]--;

    if (!yours[topping[i]]) check--;
    if (mine.size === check) answer++;
  }

  return answer;
}
