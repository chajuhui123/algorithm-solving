// function solution(numbers) {
//   const result = [];

//   for (let cur = 0; cur < numbers.length; cur++) {
//     const currentNum = numbers[cur];
//     let biggestNum = currentNum;

//     for (let back = cur + 1; back < numbers.length; back++) {
//       let backNum = numbers[back];
//       if (backNum > currentNum) {
//         biggestNum = backNum;
//         break;
//       }
//     }
//     result.push(biggestNum === currentNum ? -1 : biggestNum);
//   }

//   return result;
// }

function solution(numbers) {
  let answer = new Array(numbers.length).fill(-1); // index 미갱신시, -1 리턴
  let stack = [];

  for (var i = 0; i < numbers.length; i++) {
    // 인덱스가 존재하고 해당 존재하는 인덱스 순서의 숫자가 현재 수 보다 낮을경우
    while (stack && numbers[stack.at(-1)] < numbers[i]) {
      answer[stack.pop()] = numbers[i];
    }
    stack.push(i);
  }
  return answer;
}

// IDEA
// 1. 위 코드는 완전 탐색 방식으로 복잡도 O(n^2) 으로 시간 초과
// 2. 아래는 스택 방식으로 O(n) 따라서 문제 해결 가능
