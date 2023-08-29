// 동적 계획법 (Dynamic Programming)
// https://leetcode.com/problems/word-break/description/

let memo = {};

/**
 * 주어진 wordDict에 포함된 단어들을 조합하여, s를 완성시킬 수 있는지 여부를 리턴하는 함수
 *
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
const wordBreak = (s, wordDict) => {
  // 1. DP 에서 활용 가능한 wordDict가 없는 경우 false
  if (wordDict == null || wordDict.length === 0) return false;

  // 2. 문제에서 wordDict 내부 단어는 중복 사용이 가능하다고 함.
  // 2-1. visited 등의 사용 여부를 체크하지 않아도 되며, 중복 제거하여 아래 로직에서 한 번만 체크하도록 함
  const set = new Set(wordDict);
  const dp = Array(s.length + 1).fill(false);
  dp[0] = true;

  for (let end = 1; end <= s.length; end++) {
    for (let start = 0; start < end; start++) {
      const w = s.slice(start, end);
      if (dp[start] === true && set.has(w)) {
        dp[end] = true;
        break; // 이번 start에 대한 탐색 마침
      }
    }
  }
  return dp[s.length];
};

// 후기

// 문제 이해하기
// 주어진 wordDict에 포함된 단어들을 조합하여, s를 완성시킬 수 있는지 여부를 리턴하는 함수를 작성하기
// wordDict 에 주어진 단어를 재사용하여도 괜찮다.

// 해결 방안

// 'leetcode', ['leet', 'code'] 가 주어진 경우 예를 들어보자.

// i => 1부터 s.length-1 탐색하며, 가능한 조합인지 DP 를 통해 풀어나간다.
// i 를 기준점으로하고 0~i 까지 단어를 슬라이싱하여, wordDict에 존재하는 조합인 경우를 구한다.

// i = 1 j = 0 l
// dp = [true, false, false, false, false, false, false, false, false]

// i = 2 j = 0 le
// i = 2 j = 1  e
// dp = [true, false, false, false, false, false, false, false, false]
// i = 3 j = 0 lee
// i = 3 j = 1  ee
// i = 3 j = 2   e
// dp = [true, false, false, false, false, false, false, false, false]
// i = 4 j = 0 leet
// match
// dp = [true, false, false, false, true, false, false, false, false]
//
// i = 5 j = 0 leetc
// i = 5 j = 1  eetc
// i = 5 j = 2   etc
// i = 5 j = 3    tc
// i = 5 j = 4     c
// dp = [true, false, false, false, true, false, false, false, false]
// i = 6 j = 0 leetco
// i = 6 j = 1  eetco
// i = 6 j = 2   etco
// i = 6 j = 3    tco
// i = 6 j = 4     co
// i = 6 j = 5      o
// dp = [true, false, false, false, true, false, false, false, false]
// i = 7 j = 0 leetcod
// i = 7 j = 1  eetcod
// i = 7 j = 2   etcod
// i = 7 j = 3    tcod
// i = 7 j = 4     cod
// i = 7 j = 5      od
// i = 7 j = 6       d
// dp = [true, false, false, false, true, false, false, false, false]
// i = 8 j = 0 leetcode
// i = 8 j = 1  eetcode
// i = 8 j = 2   etcode
// i = 8 j = 3    tcode
// i = 8 j = 4     code
// match
// dp = [true, false, false, false, true, false, false, false, true]

// 결론

// 추가로 BFS 풀이 방식도 존재한다고 한다.
