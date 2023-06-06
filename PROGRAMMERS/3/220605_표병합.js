/* 위치 기반 업데이트 **/
const updateLocation = (graph, r, c, value, mergeGroup) => {
  if (checkIsInMergeGroup(r, c, mergeGroup)) {
    mergeGroup.map((group) => {
      if (group.includes(`${r} ${c}`)) {
        group.map((item) => {
          const [targetR, targetC] = item.split(" ");
          graph[targetR][targetC] = value;
        });
      }
    });
  } else {
    graph[r][c] = value;
  }
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

/* 칸 합치기 **/
const merge = (graph, fromR, fromC, toR, toC, mergeGroup) => {
  if (fromR === toR && fromC === toC) return; // 같은 경우 아무 일도 안일어남

  const value = graph[fromR][fromC];
  graph[toR][toC] = value;

  const isFromMerge = checkIsInMergeGroup(fromR, fromC, mergeGroup);
  const isToMerge = checkIsInMergeGroup(toR, toC, mergeGroup);

  if (!isFromMerge && !isToMerge) {
    // 1. 둘다 머지가 되어 있지 않은 상태
    mergeGroup.push([`${fromR} ${fromC}`, `${toR} ${toC}`]);
  } else if (isFromMerge && isToMerge) {
    // 2. 둘다 머지가 되어 있는 상태인 경우 (r1, c1 머지 그룹과 r2, c2 머지 그룹을 합침)
    // r2, c2 가 포함된 그룹을
    // r1, c1 이 포함되어있는 그룹으로 옮긴 후
    // 해당 그룹에 모든 값을 value 로 바꿔줘야 함

    // r2, c2 저장한 후, 제거 로직
    let backupRC = [];
    mergeGroup.map((group, idx) => {
      if (group.includes(`${toR} ${toC}`)) {
        backupRC = group;
        mergeGroup.splice(idx, 1);
      }
    });

    // 해당 그룹에 모든 값을 value 로 바꿈
    backupRC.map((item) => {
      const [itemR, itemC] = item.split(" ");
      graph[itemR][itemC] = value;
    });

    // 머지
    mergeGroup.map((group, idx) => {
      if (group.includes(`${fromR} ${fromC}`)) {
        group.push(...backupRC);
      }
    });
  } else if (isFromMerge) {
    // 3. r1, c1가 머지된 상태인 경우  (r2, c2 를 기존 그룹에 추가)
    mergeGroup.map((group) => {
      if (group.includes(`${fromR} ${fromC}`)) {
        group.push(`${toR} ${toC}`);
        // console.log(graph)
        return;
      }
    });
  } else if (isToMerge) {
    // 4. r2, c2가 머지된 상태인 경우  (r1, c1 을 기존 그룹에 추가)
    mergeGroup.map((group) => {
      if (group.includes(`${toR} ${toC}`)) {
        group.push(`${fromR} ${fromC}`);
        return;
      }
    });
  }
};

const unmerge = (graph, r, c, mergeGroup) => {
  // 머지된 칸인지 확인하기
  // 머지된 그룹 찾기. r,c 제외하고 grpah null 값으로 변경
  // mergeGroup 에서 해당 그룹 제거
  if (!checkIsInMergeGroup(r, c, mergeGroup)) return;
  mergeGroup.map((group, idx) => {
    if (group.includes(`${r} ${c}`)) {
      group.map((item) => {
        if (item != `${r} ${c}`) {
          const [targetR, targetC] = item.split(" ");
          graph[targetR][targetC] = null;
        }
      });
      mergeGroup.splice(idx, 1);
    }
  });
};

/* 머지된 칸인지 확인하기 **/
const checkIsInMergeGroup = (r, c, mergeGroup) => {
  let isMerge = false;
  mergeGroup.map((group) => {
    if (group.includes(`${r} ${c}`)) {
      isMerge = true;
      return;
    }
  });
  return isMerge;
};

function solution(commands) {
  let graph = Array.from(Array(51), () => Array(51).fill(null));
  let mergeGroup = [];

  const result = [];

  commands.forEach((item) => {
    const command = item.split(" ");
    const [commandType, ...param] = command;

    switch (commandType) {
      case "UPDATE":
        const isUpdateValue = command.length === 3; // 해당하는 값을 변경시키는 update 문인지 검사

        if (isUpdateValue) {
          // 값 기준 업데이트
          const [fromValue, toValue] = param;
          updateValue(graph, fromValue, toValue);
        } else {
          // r,c 위치 기반 업데이트
          const [updateR, updateC, value] = param;
          updateLocation(graph, updateR, updateC, value, mergeGroup);
        }
        break;

      case "MERGE":
        // 머지의 참조 칸을 어떻게 구현할지 고민 중
        // 머지 로직에 영향을 받는 값들
        // 1. merge
        // 2. 위치 기반 UPDATE
        // 3. unmerge
        const [fromR, fromC, toR, toC] = param;
        merge(graph, fromR, fromC, toR, toC, mergeGroup);

        // console.log(mergeGroup)
        // console.log(graph)

        break;

      case "UNMERGE":
        const [unmergeR, unmergeC] = param;
        unmerge(graph, unmergeR, unmergeC, mergeGroup);
        // console.log(mergeGroup)
        // console.log(graph)
        break;

      case "PRINT":
        const [printR, printC] = param;
        result.push(graph[printR][printC] ?? "EMPTY");
        break;
    }
  });

  return result;
}
