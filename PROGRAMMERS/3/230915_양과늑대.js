// 유형 : 구현, DFS
// https://school.programmers.co.kr/learn/courses/30/lessons/92343

// info => 양 (0) 또는 늑대(1)에 대한 정보
// edges => 2진 트리 관계
function solution(info, edges) {
  const answer = [];

  let visited = Array.from({ length: info.length }, () => false);

  const dfs = (sheep, wolf) => {
    // 1. 양이 늑대보다 많아야 함.
    // 1-1. 양이 더 많은 경우 정답 후보가 될 수 있음
    // 1-2. 늑대가 더 많거나 같다면 탐색 종료 (양이 잡아먹히는 상황)
    if (sheep > wolf) answer.push(sheep);
    else return;

    // 2. DFS 로직으로 노드 탐색
    for (let edge of edges) {
      const [parent, children] = edge;
      // 2-1.부모 노드는 거쳐야 하고 (방문) 진행할 다음 자식 노드는 방문하지 않았어야 함 (미방문)
      if (visited[parent] && !visited[children]) {
        visited[children] = true;

        if (info[children] === 0) dfs(sheep + 1, wolf);
        else dfs(sheep, wolf + 1);

        visited[children] = false;
      }
    }
  };

  // 3. 0번 노드(루트 노드)에는 항상 양이 있다는 조건 처리
  visited[0] = true;
  dfs(1, 0, visited, answer);

  return Math.max(...answer);
}
