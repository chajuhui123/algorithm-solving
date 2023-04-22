// const DiaPick = {
//   diamond: 1,
//   iron: 1,
//   stone: 1,
// };

// const ironPick = {
//   diamond: 5,
//   iron: 1,
//   stone: 1,
// };

// const stonePick = {
//   diamond: 25,
//   iron: 5,
//   stone: 1,
// };

// function solution(picks, minerals) {
//   const fatigueBySection = {};
//   let totalFatigue = 0; // result

//   // 1. 탐색 가능한 minerals 구하기
//   let maxPick = picks.reduce((a, b) => a + b); // 총 곡괭이 갯수
//   if (maxPick === 0) return 0;
//   minerals = minerals.splice(0, maxPick * 5); // 주어진 곡괭이 갯수로 탐색 가능한 minerals

//   // 5개 구간씩 끊어, 최악의 상황의 피로도 구하기 (돌 곡괭이)
//   for (let i = 0; i < minerals.length; i += 5) {
//     const tempMineral = minerals.slice(i, i + 5);
//     let tempFatigue = 0;

//     for (let mineralItem of tempMineral) {
//       tempFatigue += stonePick[mineralItem];
//     }

//     fatigueBySection[tempFatigue] = tempMineral;
//   }

//   // 피로도가 많이 소비되는 구간을 기준으로 다이아몬드>철>돌 곡괭이 순으로 사용
//   const fatigues = Object.keys(fatigueBySection)
//     .map(Number)
//     .sort((a, b) => b - a); // 내림차순

//   for (let fatigueItem of fatigues) {
//     let selectedPick = {};

//     if (picks[0] === 0 && picks[1] === 0 && picks[2] === 0) break;

//     if (picks[0] >= 1) {
//       selectedPick = { ...DiaPick };
//       picks[0]--;
//     } else if (picks[1] >= 1) {
//       selectedPick = { ...ironPick };
//       picks[1]--;
//     } else {
//       selectedPick = { ...stonePick };
//       picks[2]--;
//     }

//     // 구간 피로도 순서에 따라 선택된 곡괭이로 피로도 계산
//     for (let sectionItem of fatigueBySection[fatigueItem]) {
//       totalFatigue += selectedPick[sectionItem];
//     }
//   }

//   return totalFatigue;
// }

function solution(picks, minerals) {
  let fatiguesByPick = [];
  let totalFatigue = 0; // result

  // 1. 탐색 가능한 minerals 구하기
  let maxPick = picks.reduce((a, b) => a + b); // 총 곡괭이 갯수
  if (maxPick === 0) return 0;
  minerals = minerals.splice(0, maxPick * 5); // 주어진 곡괭이 갯수로 탐색 가능한 minerals

  let sectionCount = Math.ceil(minerals.length / 5);

  for (let i = 0; i < sectionCount; i++) {
    let mineralCounts = { diamond: 0, iron: 0, stone: 0 };
    // 2. minerals 5개씩 자른후 배열을 순회하며, 갯수를 count
    minerals.splice(0, 5).map((mineralItem) => mineralCounts[mineralItem]++);

    // 3. 각 곡괭이로 광석을 캘 때 소모되는 피로도를 저장 (다이아, 철, 돌 곡괭이 순서로)
    fatiguesByPick.push([
      mineralCounts.diamond + mineralCounts.iron + mineralCounts.stone, // 다이아몬드 곡괭이
      mineralCounts.diamond * 5 + mineralCounts.iron + mineralCounts.stone, // 철 곡괭이
      mineralCounts.diamond * 25 + mineralCounts.iron * 5 + mineralCounts.stone, // 돌 곡괭이
    ]);
  }

  // 4. 돌곡괭이로 캤을 때의 피로도를 기준으로 내림차순 정렬 (가장 피로도가 많이 소모되는 구간을 우선으로 하기 위해)
  // (피로도가 가장 낮게 광물 캐기 === 가장 피로도가 많이 나오는 구간에서 좋은 곡괭이를 사용하기)
  // (돌 곡괭이로 캤을 때 피로도 가장 큰 값인 구간 == 가장 피로도가 많이 나오는 구간)

  fatiguesByPick
    .sort((a, b) => b[2] - a[2])
    .map((v) => {
      if (picks[0] > 0) picks[0]--, (totalFatigue += v[0]);
      else if (picks[1] > 0) picks[1]--, (totalFatigue += v[1]);
      else if (picks[2] > 0) picks[2]--, (totalFatigue += v[2]);
    });

  return totalFatigue;
}

// 1. 하나의 곡괭이로 연속 구간을 사용해야하기에 minerals 5개씩 끊기
// 1-1. (놓쳤던 부분) 주어진 minerals의 길이가 총 곡괭이 갯수 * 5 보다 작은 경우, 곡괭이 갯수 * 5 개의 미네랄만 캘 수 있다는 점...!

// 2. 피로도가 가장 낮게 광물 캐기 === 가장 피로도가 많이 나오는 구간에서 좋은 곡괭이를 사용하기
// 피로도가 가장 높은 구간을 어떻게 찾지?
// 2-1. 각각의 광물 갯수를 세어야 할까? n개의 object로 저장될 것이기 때문에 각각의 object 를 비교하기 까다로움... 뭔가 Number(int) 등의 값으로 비교하고 싶음
// 2-2. 가장 피로도가 많이 드는 '돌 곡괭이'를 기준으로 연산하면, Number 값으로 피로도가 가장 많이 나오는 구간을 비교할 수 있음

// 3. '돌 곡괭이'를 기준으로 피로도가 많이 나오는 구간 정렬하기
