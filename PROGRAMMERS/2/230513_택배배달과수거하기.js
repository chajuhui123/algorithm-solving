function solution(cap, n, deliveries, pickups) {
  let answer = 0;

  // 남은 배달수량, 현재 택배 수거 수량
  let nowDelete = deliveries.reduce((acc, cur) => acc + cur, 0);
  let nowPicked = pickups.reduce((acc, cur) => acc + cur, 0);

  while (nowDelete !== 0 || nowPicked !== 0) {
    // Greedy :  가장 먼 곳을 포함해서 움직여야 효율적이라는 규칙이 존재
    // deliveries와 pickups 배열의 끝쪽에 있는 0 제거
    for (let i = deliveries.length - 1; i >= 0; i--) {
      if (deliveries[i] === 0) deliveries.pop();
      else break;
    }

    for (let j = pickups.length - 1; j >= 0; j--) {
      if (pickups[j] === 0) pickups.pop();
      else break;
    }

    let last = Math.max(deliveries.length, pickups.length);
    answer += last * 2;

    nowDelete -= deleteItem(deliveries, cap);
    nowPicked -= deleteItem(pickups, cap);
  }
  return answer;
}

// 배열의 끝에서부터 cap개를 제거하고
// 제거된 갯수를 반환해주는 함수
const deleteItem = (arr, cap) => {
  let cnt = 0;
  for (let i = arr.length - 1; i >= 0; i--) {
    if (arr[i] >= cap) {
      arr[i] -= cap;
      cnt += cap;
      break;
    } else {
      cap -= arr[i];
      cnt += arr[i];
      arr[i] = 0;
    }
  }
  return cnt;
};
