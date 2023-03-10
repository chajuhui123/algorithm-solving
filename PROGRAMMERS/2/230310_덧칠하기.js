function solution(n, m, section) {
  // Why 1 ? : 첫번째 요소부터 페인트를 칠한 상태로 시작하기 때문에 1로 시작
  let answer = 1;

  let a = section[0];

  // 페인트를 칠해야하는 영역 순회
  section.map((needPaint) => {
    // 페인트를 칠하기 시작하는 위치 (a) + 롤러의 길이(m) -1 (a부터 시작하기 때문에)이
    // 페인트칠해야 하는 벽의 번호 (needPaint) 보다 작다면
    if (a + m - 1 < needPaint) {
      a = needPaint;
      return answer++;
    }
  });
  return answer;
}
