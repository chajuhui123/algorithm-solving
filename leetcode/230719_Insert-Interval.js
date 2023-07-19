/**
 * @param {number[][]} intervals
 * @param {number[]} newInterval
 * @return {number[][]}
 */
const insert = function (intervals, newInterval) {
  let [start, end] = newInterval;
  const left = [];
  const right = [];

  for (const interval of intervals) {
    const [first, last] = interval;

    // 기존의 인터벌 시작시간이 새로 들어오는 인터벌의 사이에 있을 떄 변경 (오버랩)
    if (last < start) left.push(interval);
    else if (first > end) right.push(interval);
    else {
      start = Math.min(start, first);
      end = Math.max(end, last);
    }
  }

  return [...left, [start, end], ...right];
};

// 후기

// 문제 이해하기
// 1차원 배열 newInterval을 intervals 배열에 넣으려고 할때 시간이 겹쳐지지 않도록 겹쳐지는 부분을 합병해서 변경된 intervals 배열을 리턴하는게 문제이다.
// 다른 풀이에서 '시간으로 생각하면 이해'하기 쉽다는 포인트를 알게 되었다. 예를 들어 [[1,3],[6,9]] 는 1시~3시까진데 중간에 [2,5] 2~5시 인터벌이 들어와 1시~5까지가 되었다.

// 해결 방안

// 결론
