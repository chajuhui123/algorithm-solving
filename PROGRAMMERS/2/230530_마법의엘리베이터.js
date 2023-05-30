// function solution(storey) {
//     let answer = 0;
//     const storeyArray = Array.from(storey.toString());

//     storeyArray.map((str, idx) => {
//         let elevateNum = Number(str);

//         if (idx === storeyArray.length - 1 && elevateNum >= 5) {
//             answer += (10 - elevateNum + 1);
//             return;
//         }

//         answer += elevateNum;
//     })

//     return answer;
// }

function solution(storey) {
  let result = 0;

  while (storey) {
    let current = storey % 10; // 현재 자리수
    let next = (storey / 10) % 10; // 다음 자리수

    if (current > 5) {
      // 5보다 큰 경우
      result += 10 - current;
      storey += 10; // 다음 자리수 +1
    } else if (current === 5) {
      // 5와 같은 경우
      result += current;
      storey += next >= 5 ? 10 : 0; // 다음 자리수가 5보다 크면 +1 // 해당 부분을 놓침
    } else {
      // 5보다 작은 경우
      result += current;
    }

    storey = parseInt(storey / 10); // 자리수를 변경
  }

  return result;
}

// IDEA
// 첫 번째 풀이 방식에서는 자리 수 변경을 고려하지 않았음. (예제만 참고 ㅠㅠ)
// 두 번째 풀이 방식에서는 자리 수 변경 케이스를 고려하여, 3가지 조건문을 선언하여 자리수 변경하며 케이스를 따짐. 5보다 큰 경우엔, 10-current 를 해주는 것이 이득
