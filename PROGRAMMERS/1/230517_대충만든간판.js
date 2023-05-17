function solution(keymap, targets) {
  let answer = [];
  let pressKey = 0;

  targets.forEach((x) => {
    for (let i = 0; i < x.length; i++) {
      let count = Infinity;

      //   조이스틱으로 알파벳 A 부터 숫자까지 고를수 있는데
      // 이와 같이 자판이 주어지고 버튼 한번씩 누를때마다 주어진 자판에 맞춰 키가 바뀐다
      //   이중 타겟에 맞는 언어를 최소 언어로 누른 개수를 리턴하면 된다.
      keymap.forEach((target) => {
        let idx = target.indexOf(x[i]);
        if (idx > -1) count = Math.min(count, idx + 1);
      });

      pressKey += count;
    }
    answer.push(pressKey);
    pressKey = 0;
  });

  answer = answer.map((x) => {
    if (x == Infinity) {
      x = -1;
    }
    return x;
  });
  return answer;
}
