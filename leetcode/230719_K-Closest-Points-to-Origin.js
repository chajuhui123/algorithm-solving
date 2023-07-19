// https://leetcode.com/problems/k-closest-points-to-origin/submissions/
// 21 M 소요

/**
 * @param {number[][]} points
 * @param {number} k
 * @return {number[][]}
 */
var kClosest = function (points, k) {
  const result = [];
  const distances = [];

  points.forEach(([x, y]) => {
    const distance = Math.sqrt((x - 0) ** 2 + (y - 0) ** 2);
    distances.push([[x, y], distance]);
  });

  distances.sort((a, b) => a[1] - b[1]);

  for (let i = 0; i < k; i++) result.push(distances[i][0]);

  return result;
};

// 후기

// 문제 이해하기
// 원점 (0,0) 으로부터 특정 지점까지의 거리는 Euclidean distance (i.e., √(x1 - x2)^2 + (y1 - y2)^2) 을 통해 구할 수 있을 때,
// 가까운 순으로 k개의 좌표 위치를 return 하는 문제

// 해결 방안
// 요구 사항에 따라 원점으로부터의 거리를 구하고, 해당 거리를 기준으로 좌표를 정렬할 방법을 고민해야한다.
// JS sort method는 특정 인덱스를 기준으로 정렬을 할 수 있어 쉽게 문제를 해결할 수 있었다.
// [0] 번째 인덱스에는 [x,y] 좌표를 [1] 번째 인덱스에는 Euclidean distance 를 저장한 후, 인덱스 1을 기준으로 정렬 하고 k개를 return 하도록 로직을 작성하였다.

// 결론
// 초반에는 Object 를 활용해 복잡하게 문제를 풀이할 뻔 했다.
// JS method 를 잘 활용하자.
