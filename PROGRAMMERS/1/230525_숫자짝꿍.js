function solution(X, Y) {
  let answer = "";

  // 0~9 를 탐색하며, X와 Y 각각에 해당 숫자가 얼마나 포함되어있는지 Count
  for (let i = 0; i < 10; i++) {
    const curX = X.split("").filter((a) => Number(a) === i).length;
    const curY = Y.split("").filter((a) => Number(a) === i).length;
    answer += String(i).repeat(Math.min(curX, curY)); // 겹치는 만큼 반복해서 더해줌
  }

  if (answer === "") return "-1"; // 겹치는 게 없다면 -1 리턴
  if (Number(answer) === 0) return "0"; // 0이면 0 리턴

  // 구해진 answer로 최댓값 만들기
  return answer
    .split("")
    .sort((a, b) => Number(b) - Number(a))
    .join("");
}
