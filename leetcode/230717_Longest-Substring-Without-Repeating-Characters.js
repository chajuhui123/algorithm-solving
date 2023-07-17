// https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
// 소요 시간 : 4M

/**
 * @param {string} s
 * @return {number}
 */
let lengthOfLongestSubstring = function (s) {
  const N = s.length;
  let max = 0;

  // 1. 0~n-1 인덱스를 시작점으로 잡고 차례로 연속된 문자열 만들기
  for (let i = 0; i < N; i++) {
    let subStr = s[i];

    // 2. 중복된 str이 없다면 순환을 이어가고, 중복된 Str이 존재한다면 멈추기
    for (let j = i + 1; j < N; j++) {
      if (!subStr.includes(s[j])) {
        subStr += s[j];
      } else {
        break;
      }
    }

    // 3. max length 갱신
    max = Math.max(max, subStr.length);
  }

  return max;
};
