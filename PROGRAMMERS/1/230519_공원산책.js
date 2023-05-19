// 사용자 방향 딕셔너리
const dict = {
  E: [0, 1],
  W: [0, -1],
  S: [1, 0],
  N: [-1, 0],
};

function solution(park, routes) {
  // 이전 위치
  let prev = [0, 0];

  const map = [];
  park.forEach((row, idx) => {
    const position = row.indexOf("S");
    if (position >= 0) {
      prev = [idx, position];
    }
    map.push([...row]);
  });

  routes.forEach((route) => {
    const [pos, range] = route.split(" ");

    let current = [...prev];
    let isBreak = true;

    // range 거리만큼
    for (let i = 0; i < range; i++) {
      current[0] += dict[pos][0];
      current[1] += dict[pos][1];

      // 장애물 판별 || 공원을 벗어났는지 판별
      if (
        current[0] > map.length - 1 ||
        current[0] < 0 ||
        current[1] > map[0].length - 1 ||
        current[1] < 0
      ) {
        isBreak = false;
        break;
      }

      if (map[current[0]][current[1]] === "X") {
        isBreak = false;
        break;
      }
    }

    if (isBreak) prev = current;
  });

  return prev;
}
