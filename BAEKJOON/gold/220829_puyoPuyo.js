// let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const input =
  `......\n......\n......\n......\n......\n......\n......\n......\n.Y....\n.YG...\nRRYG..\nRRYGG.`.split(
    "\n"
  );

let puyoArray = Array.from({ length: 6 }, () => []);

const direction = [
  [0, 1],
  [0, -1],
  [-1, 0],
  [1, 0],
];

input.map((line) =>
  line.split("").map((item, itemIndex) => {
    puyoArray[itemIndex].push(item);
  })
);

// console.log(puyoArray);

// Stack 활용한 DFS
const dfs = (start, visited, puyoItem) => {
  const stack = [start];
  let countPuyo = 1;

  while (stack.length) {
    const [x, y] = stack.pop();

    for (let i = 0; i < 4; i++) {
      const nx = x + direction[i][0];
      const ny = y + direction[i][1];

      if (nx < 0 || nx >= 6 || ny >= 12 || ny < 0) continue;
      //   console.log(x, y, puyoItem, nx, ny, puyoArray[nx][ny]);

      if (!visited[nx][ny] && puyoArray[nx][ny] === puyoItem) {
        visited[nx][ny] = true;
        puyoArray[nx][ny] = ".";
        countPuyo++;
        stack.push([nx, ny]);
      }
    }
  }

  return countPuyo >= 4 ? true : false;
};

const reArrangePuyo = (array) => {
  for (let lineIndex = 0; lineIndex < 6; lineIndex++) {
    for (let itemIndex = 11; itemIndex >= 0; itemIndex--) {
      // console.log(array[lineIndex][itemIndex], lineIndex, itemIndex, "탐색");

      if (array[lineIndex][itemIndex] !== ".") {
        break;
      } else {
        array[lineIndex].pop();
        array[lineIndex].unshift(".");
      }
    }
  }
  console.log(array);
};

while (true) {
  let count = 0; // 연쇄 횟수

  // DFS 로직으로 뿌요 묶음를 카운트
  for (let i = 0; i < 6; i++) {
    for (let j = 0; j < 12; j++) {
      const visited = [...Array(6)].map(() => Array(12).fill(false));

      if (!visited[i][j] && puyoArray[i][j] != ".") {
        visited[i][j] = true;
        console.log(i, j, "dfs 시작");
        const isPoppingPuyo = dfs([i, j], visited, puyoArray[i][j]);

        if (isPoppingPuyo) count++;

        // 뿌요 그래프 재정렬
        console.log("정렬 전", puyoArray);
        reArrangePuyo(puyoArray);
        console.log("정렬 후", puyoArray);
      }
    }
  }

  console.log(count);
  break;
}
