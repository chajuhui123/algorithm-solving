// 구현
// https://leetcode.com/problems/valid-anagram/description/

/**
 * 애너그램 여부를 판단하는 함수
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
const isAnagram = function (s, t) {
  if (s.length != t.length) return false;

  const sArr = s.split("");

  for (let char of sArr) {
    const location = t.indexOf(char);
    if (location === -1) return false;

    t = t.replace(char, "");
  }

  return true;
};

// 후기

// 1️⃣ 문제 이해하기

// 애너그램(Anagram)은 다른 단어나 구의 글자들을 재배열하여 형성된 단어나 구로서, 일반적으로 모든 원래의 글자들을 '정확히 한 번 사용'합니다.

// 2️⃣ 해결 방안
// 문제가 요구하는 조건대로 '구현'을 진행하였다.
// 내가 떠올린 방식은 s에 포함된 문자들을 하나씩 순환하며, t에 딱 한 번씩 포함되어 있는지 체크하는 것이었다.
// 따라서 포함여부를 체크하기 위해 `indexOf`, 한 번만 사용한 것을 체크하기 위해 `replace` 를 사용하였다.
// 놓친 부분은 애너그램이 '다른 단어나 구의 글자들을 한 번씩 사용하여 재배열했을 때' 동일한 문자열이여야 하는 것이다.
// 따라서 길이가 다르다면 애초에 애너그램의 조건에 성립할 수가 없었다. 로직 시작 전에 길이 체크를 먼저 해주는 로직을 추가해주었다.

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
const isAnagramOneLine = function (s, t) {
  return s.split("").sort().join("") === t.split("").sort().join("");
};

// 위 풀이는 한 줄로 풀이를 한 것이다.
// 애너그램 자체가 재배열하였을 때 동일한 문자열 이라는 것이니 해당 로직은 완벽히 성립한다 😂
// 좀 더 연습해야겠다!
