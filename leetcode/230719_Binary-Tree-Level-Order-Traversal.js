/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var levelOrder = function (root) {
  if (!root) return [];

  const answer = [];
  const queue = [root];

  while (queue.length) {
    const values = [];
    const queueLength = queue.length;

    for (let i = 0; i < queueLength; i++) {
      const n = queue.shift(); // 각 트리 층에 첫 값만 저장하면 되기에
      values.push(n.val);

      if (n.left) queue.push(n.left);
      if (n.right) queue.push(n.right);
    }

    answer.push([...values]);
  }
  return answer;
};

// 후기

// 문제 이해하기
// 트리이 각 층에 어떤 노드가 존재하는지 배열 형태로 리턴하는 문제
// 예시로 아래 같은 트리 구조라면 [[3], [9,10], [1,2,15,7], [11,12,13,14]] 를 리턴
//     3
//  9      10
// 1 2   15    7
//     11 12  13 14

// 해결 방안
// 우선 주어지는 root 의 구조에 대해 이해해야한다.
// root 의 가장 처음에 오는 각 노드들을 검사하며 left, right 트리 구조를 탐색한다.
// 각 트리 층에서 가장 첫 값을 저장하는 방식으로 해결할 수 있다.
// 팁은  queue.length 를 const 상수로 미리 선언해야 queue 값 변경에서 영향을 받지  않는다.

// 결론
