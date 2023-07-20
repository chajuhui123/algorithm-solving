// https://leetcode.com/problems/reverse-integer/description/

/**
 * @param {number} x
 * @return {number}
 */
const reverse = function (x) {
  const isNegative = x < 0;
  let reversedX = +Math.abs(x).toString().split("").reverse().join("");
  reversedX = isNegative ? -reversedX : reversedX;

  const isOutOfRange = -(2 ** 31) >= reversedX || reversedX >= 2 ** 31 - 1;

  return isOutOfRange ? 0 : reversedX;
};

// 후기

// 문제 이해하기
// x가 주어졌을 때, 거꾸로 뒤집은 숫자를 구하는 문제이다.
// 단 음수인 경우 음수 그대로 유지되어야 하고,
// 예를 들어 120 이 뒤집어 지면 021 인데 양수인 21을 리턴해야 한다.
// 또한 범위 [-31^2, 31^2 - 1] 를 벗어나면, 0을 리턴한다.

// 해결 방안
// JS는 문자열 다루기가 특화된 언어이다. 따라서 JS 내장 메서드를 사용하여 문제를 해결할 수 있었다.
// 주어진 x 를 절대값으로 변경 -> 문자열로 변경 -> reverse 사용을 위해 배열로 변환 -> reverse 한 후 다시 string 타입으로 변환 -> Number 타입으로 변환 -> x가 음수였던 수인 경우 다시 음수로
// 음수 여부(isNegative)와, 문제에 지정된 범위를 벗어나는지 체크(isOutOfRange)하는 Boolean 타입의 변수를 설정해주었다.
