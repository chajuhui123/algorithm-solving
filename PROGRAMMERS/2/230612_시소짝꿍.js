function solution(weights) {
  let answer = 0;
  const store = {};
  const cases = [1, 3 / 2, 2, 4 / 3]; //경우의 수 (1,1), (2,3), (2,4), (3,4)

  weights
    .sort((a, b) => b - a) //내림차순 정렬 후, 탐색
    .forEach((weight) => {
      cases.forEach((i) => {
        let s = weight * i; // (탑승자 무게 * 시소 축과 좌석 간의 거리)
        if (store[s]) answer += store[s];
      });
      if (!store[weight]) store[weight] = 1;
      else store[weight]++;
    });

  return answer;
}
