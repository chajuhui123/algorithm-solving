/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */

var canFinish = function (numCourses, prerequisites) {
  const inDegree = new Array(numCourses).fill(0);

  // 선수강 제한이 존재하는 과목 저장
  for (const pre of prerequisites) {
    inDegree[pre[0]]++;
  }

  // 수강 제한이 없는 과목 저장
  const zeroDegree = [];
  for (let i = 0; i < numCourses; i++) {
    if (inDegree[i] === 0) zeroDegree.push(i);
  }

  // 수강 제한 없는 과목 존재 하지 않음 === 사이클 있음
  if (zeroDegree.length === 0) return false;

  // 제한 없는 과목 검사하며
  while (zeroDegree.length) {
    const course = zeroDegree.pop();

    for (const pre of prerequisites) {
      // 해당 과목이 선수강 과목으로 존재하는 경우에 선수강 제한이 존재하는 과목(inDegree) value 줄여줌
      if (course === pre[1]) {
        inDegree[pre[0]]--;

        // 0이 되면 해당 과목 또한 제한 없는 과목이 되므로 zeroDegree에 추가
        if (inDegree[pre[0]] === 0) {
          zeroDegree.push(pre[0]);
        }
      }
    }
  }

  // 모든 값이 0일 때 문제 조건에 맞음
  for (const num of inDegree) {
    if (num !== 0) return false;
  }
  return true;
};

// 후기

// 문제 이해하기
// prequisites 배열에는 [듣고픈 과목, 선수강 과목] 이 주어진다. 선수강이 된다면 해당 과목을 들을 수 있는 것으로 판단한다.
// 0 ~ numCourses-1 수업을 모두 수강할 수 있다면 true를 리턴하고 아니라면 false를 리턴하면 된다.

// 해결 방안
// 1. 선수강 제한이 존재하는 과목의 개수를 카운트하는 배열을 초기화
// 1-1. 해당 과목을 수강하기 전에 다른 과정을 수강해야 한다는 것을 의미한다.
// 1-2. 그래프로 정리해보면, 다른 꼭짓점들이 해당 과목 꼭짓점을 가리키는 엣지의 갯수라고 할 수 있다.
// 2. 전제 조건이 없는 과목 배열을 초기화. prequisites 배열의 [1]에 해당
// 2-1. 그래프로 정리하면, 해당 꼭짓점을 가리키는 엣지는 존재하지 않는다.
// 3. 2에서 초기화한 전제 조건 없는 과목 배열이 비어 있으면 과목을 수강할 수 없다. (선수강하지 않고 과목을 수강할 수 없기 때문)

// 결론
// 위 알고리즘은 위상정렬 Kahn's algorithm 이라고 한다고 한다.
// 순서가 존재하는 그래프를 다룰 때 활용할 수 있는 알고리즘이다.
// 그래프 문제를 연습하자!
