// 두 번째 시도

function getSum(arr) {
  return arr.reduce((a, b) => a + b, 0);
}

function solution1(queue1, queue2) {
  let sumOfQueue1 = getSum(queue1);
  let sumOfQueue2 = getSum(queue2);

  let num = 0;
  let idx1 = 0;
  let idx2 = 0;

  const maxCalCount = queue1.length * 3;

  if ((sumOfQueue1 + sumOfQueue2) % 2 === 1) {
    return -1;
  }

  for (let i = 0; i < maxCalCount; i++) {
    if (queue1.isEmpty || queue2.isEmpty) {
      return -1;
    }

    if (sumOfQueue1 > sumOfQueue2) {
      num = queue1[idx1];

      queue2.push(num);
      sumOfQueue1 -= num;
      sumOfQueue2 += num;
      idx1++;
    } else if (sumOfQueue1 < sumOfQueue2) {
      num = queue2[idx2];

      queue1.push(num);
      sumOfQueue1 += num;
      sumOfQueue2 -= num;
      idx2++;
    } else {
      return i;
    }
  }
  return -1;
}

// IDEA

// 처음 문제에 접근하였을 때, while 문을 돌 때마다, queue1과 queue2의 합을 구한 후 비교하며 단계를 진행해갔다.
// 또한 큐의 컨셉을 활용하는 문제이기에, shift, push 연산을 통해 진행하였다.
// 하지만 shift 는 O(n) 복잡도이며, sum 메서드로 reduce 를 활용하기 때문에 O(n) 으로 복잡도가 높았다.

// 따라서 이러한 메서드를 안쓰고 while 문을 돌 때마다, 특정 변수 값을 갱신하는 방식으로 진행하였다. (sumOfQueue1, sumOfQueue2)

// 사실 해당 방식으로 진행하면서도, "signal: aborted (core dumped)" 에러로 인해 해결하지 못했는데, 이는 while 문의 maxCalCount 때문이었다.
// maxCalCount 는 최악의 케이스를 찾으면 되는데 이 문제에서 최악의 케이스는 "queue1에서 queue2로 모든값을 보내고, queue2에서 하나만을 제외하고 다시 모두 queue1으로 내보내는 케이스"
// 즉 maxCalCount는 queue.length * 3 (둘의 길이는 같음!) 으로 정의할 수 있다.
