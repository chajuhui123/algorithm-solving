// function getPermutations(arr, selectNumber) {
//     const results = [];
//     if (selectNumber === 1) return arr.map((el) => [el]);
//     arr.forEach((fixed, index, origin) => {
//       const rest = [...origin.slice(0, index), ...origin.slice(index+1)]; // 탐색된 fixed 값을 제외한 나머지 배열
//       const permutations = getPermutations(rest, selectNumber - 1); // 위에서 구해진 나머지에 대한 순열
//       const attached = permutations.map((el) => [fixed, ...el]); // 고정값 + 구해진 순열
//       results.push(...attached);
//     });

//     return results;
// }

// function solution(n, k) {
//     const arr = Array.from({length:n}, (v, i) => i+1);
//     const permutations = getPermutations(arr, n);

//     return permutations[k-1];
// }

function solution(n, k) {
  const answer = [];
  let arr = Array.from({ length: n }, (_, i) => i + 1);
  let fac = arr.reduce((ac, v) => ac * v, 1); // 모든 수를 곱함
  k -= 1;

  while (answer.length !== n) {
    fac = fac / arr.length;
    let temp = arr[Math.floor(k / fac)];
    answer.push(temp);
    k = k % fac;
    arr = arr.filter((v) => v != temp);
  }
  return answer;
}

// IDEA
// 순열 방식은 <효율성>에서 통과할 수 없다.
// 모든 순열을 구한 후 찾는 방식이 아닌, 해당 자리에는 어떤 숫자가 오는지 찾도록 해보자
// 순열은 n!가지 경의의 수를 가진다. 앞자리 N, 두 번째 후보 n-1, ... 개의 후보군에서 각 자릿수가 결정되기 때문이다.
// 따라서 그 자리를 구하려면? 반대로 (n-1)!이 k 앞에 몇 개 있는지 확인해야한다.
