// https://leetcode.com/problems/01-matrix/description/

/**
 * @param {number[][]} mat
 * @return {number[][]}
 */
let updateMatrix = function (mat) {
  // 각 셀마다 가장 가까운 0부터의 거리를 구하는 문제

  // row, col 길이
  const row = mat.length;
  const col = mat[0].length;

  // 방향 정의
  const direction = [
    [0, 1],
    [0, -1],
    [-1, 0],
    [1, 0],
  ];

  const dq = [];

  let visited = Array.from({ length: row }, () =>
    Array.from({ length: col }, () => -1)
  );

  for (let i = 0; i < row; i++) {
    for (let j = 0; j < col; j++) {
      if (mat[i][j] === 0) {
        // 1. 0을 기준으로 탐색 준비
        dq.push([i, j]);
        visited[i][j] = 0;
      }
    }
  }

  while (dq.length) {
    const [x, y] = dq.shift();

    for (let cnt = 0; cnt < 4; cnt++) {
      // 2. 시작점인 0을 기준으로 다음 탐색할 칸의 index 지정
      const nextX = x + direction[cnt][0];
      const nextY = y + direction[cnt][1];

      // 3. 문제 조건에 맞는 칸이라면 계속 진행
      // 3-1. 범위를 벗어나지 않고, 아직 방문하지 않은 칸이며 0이 아닌 칸 (visited[nextX][nextY] == -1) 이라면 진행 가능
      if (
        0 <= nextX &&
        nextX < row &&
        0 <= nextY &&
        nextY < col &&
        visited[nextX][nextY] == -1
      ) {
        // 4. 다음으로 진행할 칸에 진행된 횟수 누적시켜줌, queue에 추가하여 계속 진행
        dq.push([nextX, nextY]);
        visited[nextX][nextY] = visited[x][y] + 1;
      }
    }
  }

  return visited;
};
