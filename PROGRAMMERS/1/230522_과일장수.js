function solution(k, m, score) {
  let total = 0;

  // 최대 이익을 얻기 위해선? (최저 사과 점수 * 한 상자에 담는 사과 수)
  // 점수가 높은 사과 순서대로 포장하기 (최저 점수도 최대한 높게 하기 위해서)
  const ableCount = Math.floor(score.length / m); // 총 포장 상자 갯수

  // 점수가 큰 사과 순서대로 정렬 후, 점수를 계산
  const sortedScore = score.sort((a, b) => b - a);

  for (let cnt = 0; cnt < ableCount; cnt++) {
    const nowArea = sortedScore.slice(cnt * m, cnt * m + m);
    total += Math.min(...nowArea) * m;
  }

  return total;
}
