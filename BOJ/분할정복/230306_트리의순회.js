let fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "BAEKJOON/example.txt";

// const input = require("fs")
//   .readFileSync(filePath)
//   .toString()
//   .trim()
//   .split("\n");

const input = ["3", "1 2 3", "1 3 2"];

n = Number(input[0]);
inOrder = input[1].split().map((item) => Number(item)); // 중위 순회 (왼쪽 -> 본인 -> 오른쪽)
postOrder = input[2].split().map((item) => Number(item)); // 후위 순회 (왼쪽 -> 오른쪽 -> 본인)
preOrder = []; // 전위 순회 (본인 -> 왼쪽 -> 오른쪽)

// postOrder의 끝이 preOrder의 시작점 (루트)
// inOrder 의 중심에는 Root 노드, Root 노드의 오른쪽, 왼쪽 자식들이 inOrder의 왼쪽 오른쪽에 위치

const searchNode = (inOrderStart, postOrderStart, length) => {
  if (length === 1) {
    preOrder.push(postOrder[postOrderStart]);
    return;
  }

  const root = postOrder[postOrderStart + length - 1]; // postOrder의 끝이 Root Node임
  preOrder.push(root);

  const rootIndex = inOrder.indexOf(root); // inOrder의 중심에는 Root 노드 존재. 양 옆으로 왼쪽 자식 노드, 오른쪽 자식 노드로 분리 가능

  const letInOrderStart = inOrderStart;
  const letPostOrderStart = postOrderStart;
  const leftLength = rootIndex - inOrderStart;

  const rightInOrderStart = rootIndex + 1;
  const rightPostOrderStart = postOrderStart + leftLength;
  const rightLength = length - leftLength - 1;

  if (leftLength > 0)
    searchNode(letInOrderStart, letPostOrderStart, leftLength);
  if (rightLength > 0)
    searchNode(rightInOrderStart, rightPostOrderStart, rightLength);
};

searchNode(0, 0, n);

for (let line of preOrder) {
  console.log(line.join(" "));
}
