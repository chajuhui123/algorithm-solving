```js
let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

// const input =
//   `......\n......\n......\n......\n......\n......\n......\n......\n.Y....\n.YG...\nRRYG..\nRRYGG.`.split(
//     "\n"
//   );

// const input =
//   "......\n......\n......\n......\n......\n......\n.G....\nRR....\nRY....\nRYG...\nRRY...\nRYYGG.".split(
//     "\n"
//   );

// 뿌요뿌요 array 재정렬 (row, column 을 뒤집음)
// puyoArray[index][0~11] 가 input의 index 번째 column item 으로 구성되도록
let puyoArray = Array.from({ length: 6 }, () => []);
input.map((line) =>
  line.split("").map((item, itemIndex) => {
    puyoArray[itemIndex].push(item);
  })
);

// 상하좌우 방향
const direction = [
  [0, 1],
  [0, -1],
  [-1, 0],
  [1, 0],
];

// 너비우선탐색 BFS
const bfs = (start, visited, puyoItem) => {
  const queue = [start]; // 탐색용 queue
  const deleteItems = []; // 4개 이상 묶음인 경우, 해당 배열에 포함된 아이템들의 영역을 .으로 치환
  let countPuyo = 1; // 연쇄되는 puyo item count

  while (queue.length) {
    const [x, y] = queue.shift();

    // 상하좌우 방향 순환
    for (let i = 0; i < 4; i++) {
      const nx = x + direction[i][0];
      const ny = y + direction[i][1];

      if (nx < 0 || nx >= 6 || ny >= 12 || ny < 0) continue; // 영역을 벗어남

      if (!visited[nx][ny] && puyoArray[nx][ny] === puyoItem) {
        visited[nx][ny] = true;
        countPuyo++;
        deleteItems.push([nx, ny]);
        queue.push([nx, ny]);
      }
    }
  }

  // 뿌요 아이템이 4개 이상이면 연쇄가 일어날 수 있는 상황이다.
  // 따라서 해당 영역들을 .으로 치환한다.
  if (countPuyo >= 4) {
    puyoArray[start[0]][start[1]] = "."; // 탐색 시작한 영역을 잊지 않는다.
    deleteItems.map((xy) => (puyoArray[xy[0]][xy[1]] = "."));
  }

  return countPuyo >= 4 ? true : false;
};

// 뿌요 그래프 재정렬
const reArrangePuyo = (array) => {
  const newArray = [];

  for (let lineIndex = 0; lineIndex < 6; lineIndex++) {
    const tempArray = [];
    let noneItemCount = 0;

    for (let itemIndex = 0; itemIndex < 12; itemIndex++) {
      if (array[lineIndex][itemIndex] !== ".") {
        noneItemCount++;
        tempArray.push(array[lineIndex][itemIndex]);
      }
    }

    for (let i = 0; i < 12 - noneItemCount; i++) tempArray.unshift(".");
    newArray.push(tempArray);
  }

  return newArray;
};

let count = 0; // 연쇄 횟수

while (true) {
  let isPoppingPuyo = false; // 해당 탐색에서 연쇄가 일어나는지에 대한 boolean

  for (let i = 0; i < 6; i++) {
    for (let j = 0; j < 12; j++) {
      const visited = Array.from({ length: 6 }, () =>
        Array.from({ length: 12 }, () => false)
      );

      if (!visited[i][j] && puyoArray[i][j] != ".") {
        visited[i][j] = true;
        const isMore4Popping = bfs([i, j], visited, puyoArray[i][j]);

        if (isMore4Popping) isPoppingPuyo = true;
      }
    }
  }

  // 뿌요 그래프 재정렬

  // 한 번의 탐색에서 터질 수 있는 뿌요가 여러 그룹이 있다면 동시에 터져야 하고,
  // 여러 그룹이 터지더라도 한번의 연쇄가 추가된다.
  // (= 한 번의 탐색에서 여러번 연쇄가 되더라도 1회만 count하고, 모든 행열 탐색 후에 재정렬 한다.)
  puyoArray = reArrangePuyo(puyoArray);

  if (isPoppingPuyo) {
    count++;
  } else {
    console.log(count);
    break;
  }
}
```

- 이전에 풀다가 막혀서 미뤘던 문제인데 오늘에서야 해결했다.
- 백준에 나와있는 예제 1만 충족시키고나서 왜 틀릴지 고민했는데, 문제 조건을 완벽하게 숙지하지 못해서 반례를 찾지 못하였다.
- 연쇄가 일어날 때마다 재정렬이 발생하는 것이 아닌, 한 번의 탐색이 끝난 후에 재정렬을 시켜줘야 하는 것이었다.
- 또한 재정렬을 할 때도 '아이템 빈영역 아이템 빈영역 아이템' 같은 정렬이 있을 수도 있다는 점을 간과하였다.
- 해당 반례들을 찾아 해결하고 1시간 30분만에 해결 완료 ^^ 뿌듯하다.
