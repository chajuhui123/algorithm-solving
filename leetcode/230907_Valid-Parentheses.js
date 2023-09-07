/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  const stack = [];

  for (let i = 0; i < s.length; i++) {
    let c = s.charAt(i);

    // 1.  왼쪽 괄호 아이템 ("(", "[", "{" ) 의 경우 stack 에 저장해준다.
    switch (c) {
      case "(":
        stack.push(")");
        break;
      case "[":
        stack.push("]");
        break;
      case "{":
        stack.push("}");
        break;
      // 2.  오른쪽 괄호 아이템 (")", "]", "}" ) 의 경우 스택에 가장 마지막 아이템과 비교한다, 만약 다르다면 짝이 맞지 않는 것이다.
      default:
        if (c !== stack.pop()) {
          return false;
        }
    }
  }

  // 3. stack 이 비지 않은 경우도 짝이 맞지 않는 경우이다.
  return stack.length === 0;
};

// 후기

// 1️⃣ 문제 이해하기
// '(', ')', '{', '}', '[', ']' 로 구성된 문자열이 주어질때, 짝이 맞는지 체크하여 리턴하는 함수를 작성하는 문제이다.

// 2️⃣ 해결 방안
// stack 자료구조와 switch case 문을 통해 해결할 수 있다.
// 왼쪽 괄호인 경우에는 스택에 넣어주고
// 오른족 괄호인 경우에는 스택 마지막에 들어가있는 왼쪽 괄호와 짝이 맞는지 비교한다
// 스택이 비지 않거나, 짝이 맞지 않는 경우 valid 한 괄호 문자열이 아니다!
