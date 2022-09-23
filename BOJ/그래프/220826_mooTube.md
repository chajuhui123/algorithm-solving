```js
// let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const input = "4 3\n1 2 3\n2 3 2\n2 4 4\n1 2\n4 1\n3 1".split("\n");

// [영상번호1, 영상번호2, 유사도] 정점간 유사도 배열 초기화
// [영상번호, 유사도 조건] 질문 배열 초기화
const [N, Q] = input.shift().split(" ").map(Number);
const USADOList = input
  .slice(0, N - 1)
  .map((list) => list.split(" ").map(Number));
const questions = input
  .slice(N - 1, input.length)
  .map((list) => list.split(" ").map(Number));

// 영상간 유사도 연결 관계 graph에 초기화
const graph = Array.from({ length: N + 1 }, () => []);

USADOList.map((item) => {
  const [video1, video2, usado] = item;

  graph[video1].push([video2, usado]);
  graph[video2].push([video1, usado]);
});

const answer = [];

// 각 질문에 대한 답변을 구하는 로직
questions.map((question) => {
  const queue = [];

  const [k, v] = question;

  // 첫 정점 추가 유사도는 임시로 100000000
  queue.push([v, 100000000]);
  let visited = Array.from({ length: N + 1 }, () => false);
  visited[v] = true;

  let result = 0;

  // 연결된 비디오 BFS 탐색
  while (queue.length) {
    const [v, usado] = queue.shift();

    graph[v].map((video) => {
      let [nextVideo, nextUsado] = video;
      nextUsado = Math.min(usado, nextUsado); // 둘 중 작은 값이 해당 비디오의 유사도

      // 유사도가 K 이상이고, 방문하지 않은 정점이라면 질문의 답변이 될 수 있음
      if (nextUsado >= k && !visited[nextVideo]) {
        result++;
        queue.push([nextVideo, nextUsado]);
        visited[nextVideo] = true;
      }
    });
  }
  answer.push(result);
});

console.log(answer.join("\n"));
```

- 문제를 이해하기 까다로웠다! 각 영상간의 유사도가 주어지고,
- 각 영상간의 유사도를 graph에 저장하고
- 질문에 주어진 특정 영상과 연관있는 영상 중, 특정 유사도 이상인 영상의 갯수를 리턴하면 된다. (내가 적어놓고도 혼란스럽군)
