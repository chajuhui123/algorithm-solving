function solution(k, tangerine) {
  let answer = 0;

  // 주어진 귤의 각 종류 별로 몇 개 존재하는지 저장
  const countTangerine = {};
  tangerine.map((item) => {
    countTangerine[item] ? countTangerine[item]++ : (countTangerine[item] = 1);
  });

  // sortedCounts 귤의 갯수 별로 내림차순 정렬
  // Object Key 값은 문제 풀이에서 사용되지 않기 때문에 Object.values 메서드 활용 가능
  const sortedCounts = Object.values(countTangerine)
    .map(Number)
    .sort((a, b) => b - a);

  for (let i = 0; i < sortedCounts.length; i++) {
    // 가장 많은 귤부터 담으며, 새로운 종류 담길때마다 answer +1
    k -= sortedCounts[answer];
    answer++;
    if (k <= 0) break; // 상자 꽉 찬 상태
  }

  return answer;
}
