function solution(commands) {
  const result = [];

  let graph = Array.from(Array(51), () => Array(51).fill(null));
  let mergeParent = Array(51)
    .fill()
    .map((_, i) =>
      Array(51)
        .fill()
        .map((_, j) => [i, j])
    );

  commands.forEach((item) => {
    const command = item.split(" ");
    const [commandType, ...valueParam] = command;

    switch (commandType) {
      case "UPDATE":
        const isUpdateValue = valueParam.length === 2; // 값 기준 업데이트인 경우
        if (isUpdateValue) updateValue(valueParam);
        else updateLocation(valueParam);
        break;

      case "MERGE":
        merge(valueParam);
        break;

      case "UNMERGE":
        unmerge(valueParam);
        break;

      case "PRINT":
        const printValue = print(valueParam);
        result.push(printValue);
        break;
    }
  });

  return result;

  function updateValue(valueParam) {
    const [value1, value2] = valueParam;

    graph.map((line, rIdx) => {
      line.map((itemValue, cIdx) => {
        if (itemValue === value1) graph[rIdx][cIdx] = value2;
      });
    });
  }

  function updateLocation(valueParam) {
    const [r, c, value] = valueParam;
    const target = find([r, c]);

    graph.map((line, rIdx) => {
      line.map((_, cIdx) => {
        if (mergeParent[rIdx][cIdx].toString() === target.toString())
          graph[r][c] = value;
      });
    });
  }

  function merge(valueParam) {
    const [r1, c1, r2, c2] = valueParam;
    if (r1 === r2 && c1 === c2) return; // 1. 선택한 두 위치의 셀이 같은 셀일 경우 무시

    // value 에 대한 조건
    // 1. 두 셀 중 한 셀이 값을 가지고 있을 경우, 병합된 셀은 해당 값을 가지게 됨
    // 2. 두 셀 모두 값을 가지고 있을 경우 병합된 셀은 (r1, c1) 위치의 셀 값을 가지게 됨
    const value = graph[r1][c1] ?? graph[r2][c2];

    const mergeParent1 = find([r1, c1]);
    const mergeParent2 = find([r2, c2]);

    if (mergeParent1.toString() !== mergeParent2.toString())
      mergeParent[r2][c2] = mergeParent1; // r1, c1 이 부모가 되도록 병합

    graph.map((line, rIdx) => {
      line.map((itemValue, cIdx) => {
        // 이전에 (r2, c2) 가 부모로 연결되어 있던 값들을 r1, c1 의 부모와 연결되게 해주기
        if (mergeParent[rIdx][cIdx].toString() === mergeParent2.toString()) {
          mergeParent[rIdx][cIdx] = mergeParent1;
        }
        // (r1, c1)가 부모로 연결되어 있는 값들 === 머지 된 값을 머지 이후 값으로 변경해주기
        if (mergeParent[rIdx][cIdx].toString() === mergeParent1.toString()) {
          graph[rIdx][cIdx] = value;
        }
      });
    });
  }

  function unmerge(valueParam) {
    const [r, c] = valueParam;
    const value = graph[r][c];
    const target = find([r, c]);

    graph.map((line, rIdx) => {
      line.map((_, cIdx) => {
        if (mergeParent[rIdx][cIdx].toString() === target.toString()) {
          graph[rIdx][cIdx] = null;
          mergeParent[rIdx][cIdx] = [rIdx, cIdx];
        }
      });
    });

    graph[r][c] = value;
  }

  function print(valueParam) {
    const [r, c] = valueParam;
    return graph[r][c] ?? "EMPTY";
  }

  function find(location) {
    const [r, c] = location;
    // 1. merge 그룹 중 가장 상위 부모를 찾은 경우 return
    if ([r, c].toString() === mergeParent[r][c].toString()) {
      return [Number(r), Number(c)];
    }
    // 2. 재귀적으로 merge 그룹에서의 부모 r, c 를 찾음
    mergeParent[r][c] = find(mergeParent[r][c]);
    return mergeParent[r][c];
  }
}

// IDEA
// 해당 구현 문제에 포인트는 Merge / UnMerge 로직이라고 생각했음
// Merge 로직에 의해 영향을 받는 값들이 값들이 다양한데 (위치 기반 Update, unmerge, merge ...)
// merge 된 칸들을 저장하고, 활용할 방안에 대해 고민이 필요함!
// 그리고 각 로직에서 참고해야하는 예외 케이스들을 코드로 잘 구현할 수 있어야 함.
