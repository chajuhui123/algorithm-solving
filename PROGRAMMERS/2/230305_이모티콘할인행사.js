const discount = [10, 20, 30, 40]; // 10, 20, 30, 40 할인

// 중복순열 구하기
// https://mine-it-record.tistory.com/508 참고
const getPermutations = (arr, num) => {
  const results = [];
  if (num === 1) return arr.map((v) => [v]);

  arr.forEach((fixed, index, origin) => {
    // 기준값(fixed)이 있기 때문에 선택하려는 개수에서 - 1 을 해준다.
    const permutations = getPermutations(origin, num - 1);

    // 기준값(fixed)에 순열(permutations)을 붙인다.
    const attached = permutations.map((v) => [fixed, ...v]);

    // 붙인 값을 결과 값에 넣어준다.
    results.push(...attached);
  });

  return results;
};

function solution(users, emoticons) {
  const answer = [0, 0];

  let maxPromotion = 0; // 최대 이모티콘 플러스 서비스 가입자
  let maxSell = 0; // 최대 이모티콘 판매액

  const discounts = getPermutations(discount, emoticons.length);

  discounts.map((discount) => {
    // 현재 할인율 케이스에서 총 서비스 가입자 수, 구매액 선언
    let cntPromotion = 0;
    let totalPurchase = 0;

    for (let user of users) {
      const minDiscount = user[0]; // 유저가 필요한 최소 할인율
      const minPromotion = user[1]; // 유저의 프로모션 전환을 위한 가격

      let tempPurchase = 0; // 해당 유저가 구매하는 비용

      discount.map((discountItem, idx) => {
        if (discountItem >= minDiscount) {
          const purchase = ((100 - discountItem) / 100) * emoticons[idx];
          tempPurchase += purchase;
        }
      });

      if (tempPurchase >= minPromotion) {
        cntPromotion += 1;
      } else {
        totalPurchase += tempPurchase;
      }
    }

    // 목표 1. 이모티콘 플러스 서비스 가입자를 최대한 늘리는 것.
    if (cntPromotion > answer[0]) {
      answer[0] = cntPromotion;
      answer[1] = totalPurchase;
    } else if (cntPromotion === answer[0] && totalPurchase > answer[1]) {
      // 목표 2. 이모티콘 판매액을 최대한 늘리는 것.
      // 플러스 서비스 가입자가 최대인 케이스가 제일 중요도가 높으나,
      // 이모티콘 플러스 서비스 가입자 수가 같은 경우, 판매액이 더 높은 케이스가 우선 순위.
      answer[1] = totalPurchase;
    }
  });

  return answer;
}
