const input = [];

require("readline")
  .createInterface(process.stdin, process.stdout)
  .on("line", function (line) {
    input.push(line.trim());
  })
  .on("close", function () {
    // 하위에 로직 작성

    const N = Number(input[0]);
    const inOrder = input[1].split(" ").map(Number); // 중위 순회 (왼쪽 -> 본인 -> 오른쪽)
    const postOrder = input[2].split(" ").map(Number); // 후위 순회 (왼쪽 -> 오른쪽 -> 본인)
    const preOrder = []; // 전위 순회 (본인 -> 왼쪽 -> 오른쪽)

    const callStack = [[0, N - 1, 0, N - 1]];

    // postOrder의 끝이 preOrder의 시작점 (루트)
    // inOrder 의 중심에는 Root 노드, Root 노드의 오른쪽, 왼쪽 자식들이 inOrder의 왼쪽 오른쪽에 위치

    while (callStack.length) {
      const [inStart, inEnd, postStart, postEnd] = callStack.pop();
      if (inStart > inEnd || postStart > postEnd) {
        continue;
      }
      const root = postOrder[postEnd];
      preOrder.push(root);
      let inRootIndex;
      for (let i = inStart; i <= inEnd; i++) {
        if (inOrder[i] === root) {
          inRootIndex = i;
          break;
        }
      }
      const postLeftEnd = postStart + (inRootIndex - 1 - inStart);
      callStack.push([inRootIndex + 1, inEnd, postLeftEnd + 1, postEnd - 1]);
      callStack.push([inStart, inRootIndex - 1, postStart, postLeftEnd]);
    }

    console.log(preOrder.join(" "));
  });

// IDEA
// 1. 런타임 에러 (StackSizeExceeded)
// JS로 재귀 호출 방식으로 구현하게 되면, 호출 스택이 넘쳐 런타임 에러가 발생할 수 있다.
// 노드의 개수가 10만 개이고 이진 트리의 리프를 제외한 모든 노드가 하나의 자식을 가지고 있어서 직선 형태의 트리라면, 함수가 최대 10만 번 호출 될 수 있다.
// NodeJS의 call stack 최대 사이즈는 약 1만이므로 런타임 에러(Call Stack Size Exceed)가 발생한다.
// 따라서 반복문을 이용해 재귀 호출 방식처럼 동작하게 구현해야 한다! (함수를 통한 재귀는 에러 발생 ㅠ)
// 2. 전위 순회, 중위 순회, 후위 순회의 특징과 연결 관계를 이해해야한다.
