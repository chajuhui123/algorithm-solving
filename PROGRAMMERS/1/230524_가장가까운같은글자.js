function solution(s) {
  const answer = [];
  const map = new Map();

  for (let i = 0; i < s.length; i++) {
    // 동일한 글자가 있다면, 두 글자의 위치 차이(현재 위치 - 이전 위치)를 answer에 담음
    if (map.has(s[i])) answer.push(i - map.get(s[i]));
    // 없다면, -1 (초기값)
    else answer.push(-1);

    // 현재 탐색 중인 글자, 위치 저장
    map.set(s[i], i);
  }

  return answer;
}

// 아래는 접근 방식은 비슷하나, 숏코딩! 그리고 {key : value} Object 형태로 값과 위치 값을 다루고 있다.
// function solution(s) {
//   const hash = {};

//   return [...s].map((v, i) => {
//     let result = hash[v] !== undefined ? i - hash[v] : -1;
//     hash[v] = i;
//     return result;
//   });
// }
