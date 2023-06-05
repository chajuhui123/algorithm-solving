/* 위치 기반 업데이트 **/
const updateLocation = (graph, r, c, value, mergeGroup) => {
  graph[r][c] = value;
};

/* 값 기반 업데이트 **/
const updateValue = (graph, fromValue, toValue) => {
  graph.map((line, r) => {
    line.map((item, c) => {
      if (item === fromValue) {
        graph[r][c] = toValue;
      }
    });
  });
};

const merge = (graph, r1, c1, r2, c2, mergeGroup) => {
  // 같은 경우 아무 일도 안일어남
  // r1, c1가 머지된 상태인 경우
  // r2, c2가 머지된 상태인 경우
  // 둘다 머지가 되어 있는 상태인 경우
};

function solution(commands) {
  let graph = Array.from(Array(51), () => Array(51).fill(null));
  let mergeGroup = [];

  const result = [];

  commands.forEach((item) => {
    const command = item.split(" ");
    const commandType = command[0];

    switch (commandType) {
      case "UPDATE":
        const isUpdateValue = command.length === 3; // 해당하는 값을 변경시키는 update 문인지 검사

        if (isUpdateValue) {
          // 값 기준 업데이트
          const [_, from, to] = command;
          updateValue(graph, from, to);
        } else {
          // r,c 위치 기반 업데이트
          const [_, r, c, value] = command;
          updateLocation(graph, r, c, value);
        }
        break;

      case "MERGE":
        // 머지의 참조 칸을 어떻게 구현할지 고민 중
        // 머지 로직에 영향을 받는 값들
        // 1. merge
        // 2. 위치 기반 UPDATE
        // 3. unmerge
        break;

      case "UNMERGE":
        break;

      case "PRINT":
        const [_, r, c] = command;
        result.unshift(graph[r][c] ?? "EMPTY");
        break;
    }
  });

  return result;
}
