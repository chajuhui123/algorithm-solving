// https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
// 31 M 소요

/**
 * @param {string[]} tokens
 * @return {number}
 */
const evalRPN = function (tokens) {
  const operators = ["+", "-", "*", "/"];

  for (let i = 0; i < tokens.length; i++) {
    const token = tokens[i];
    if (operators.includes(token)) {
      const num1 = +tokens[i - 2];
      const num2 = +tokens[i - 1];
      const calcResult = parseInt(eval(`${num1} ${token} ${num2}`));
      tokens.splice(i - 2, 3, calcResult);
      i -= 2;
    }
  }
  return tokens[0];
};

// 후기
// Reverse Polish Notation 에 따른 계산 결과를 리턴하자.
// 예제로 문제를 파악하였을 때 배열 tokens 가 주어지는데 배열을 순차적으로 탐색하였을 때 operator를 마주치면 이전 2값에 대해 해당 연산자 계산을 진행한다!

// 문제 이해하기

// 해결 방안
// 문제를 파악하였을 때 스택 구조로 연산자를 만나면 이전 2개의 숫자를 pop 하는 식으로 문제를 풀어볼까 하였다. 하지만 순환하는 tokens 배열의 길이, 검사하는 아이템 인덱스가 꼬이는 일이 발생할 것 같아 다른 방안을 떠올렸다.
// 연산자를 만나면 JS splice 메서드를 활용해, 총 3개의 아이템을 제거하고 (숫자2개, 연산자) 그 위치에 계산 결과를 넣어줌으로써 순차적으로 연산을 진행하는 방식으로 하였다.
// 다시 순환을 시작할 땐 계산 결과부터 순환하기 때문에 index 를 -2 해주었다.
// 해당 로직을 적용할 수 있었던 것은 <처음 마주친 연산자에 대해 먼저 계산을 하기 때문에> 이다.

// 결론
// 인덱스 순서, 자료형 같은 자잘한 실수 때문에 풀이 시간이 조금 소요 됐다. 꼼꼼하게 코드를 검토하자.
// (ex. num1 / num2 에서 인덱스 순서를 거꾸로 연산 하였음. Number 타입 변환하지 않고 연산을 진행함 등...)
// 이번 문제에선 빠르게 이슈 부분을 파악하였지만, 이런 종류의 실수는 문제 풀이 설계의 원점으로 돌아가게 할 수도 있어 위험하다~!
