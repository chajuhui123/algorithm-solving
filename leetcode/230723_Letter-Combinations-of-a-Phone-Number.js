// https://leetcode.com/problems/letter-combinations-of-a-phone-number

/**
 * @param {string} digits
 * @return {string[]}
 */
const letterCombinations = function (digits) {
  if (!digits.length) return [];

  const map = {
    2: ["a", "b", "c"],
    3: ["d", "e", "f"],
    4: ["g", "h", "i"],
    5: ["j", "k", "l"],
    6: ["m", "n", "o"],
    7: ["p", "q", "r", "s"],
    8: ["t", "u", "v"],
    9: ["w", "x", "y", "z"],
  };

  let result = [];

  function permute(string, index) {
    if (index === digits.length) {
      result.push(string);
      return;
    }

    for (let x of map[digits[index]]) {
      permute(string + x, index + 1);
    }
  }

  permute("", 0);
  return result;
};

// 후기

// 문제 이해하기
//  2~9 사이의 숫자를 랜덤으로 갖는 문자열을 주고 그 숫자 조합으로 만들 수 있는 알파벳 조합을 리턴하는 문제이다.
// 백트래킹 순열 알고리즘을 활용하여 문제를 해결할 수 있다.

// 해결 방안
// '' 문자열부터 시작해서 주어진 digits의 첫 번째 char를 먼저 string에 이어붙인다.
// 이어붙여진 string 은 permute 함수를 돌게 된다. 이 때 index를 증가시키게되는데, index가 digits.length와 같다면 하나의 조합을 만드는데 성공한 것이므로 result 배열에 추가한다.
