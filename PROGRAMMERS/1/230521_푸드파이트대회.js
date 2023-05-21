// food[0] 은 항상 1
// Math.floor(3 / 2) => 1 따라서 1
// Math.floor(4 / 2) => 2 따라서 22
// Math.floor(6 / 2) => 3 따라서 333
// 122333 해당 값을 뒤집으면 333221, 따라서 12233303332221

function solution(food) {
  if (food.length === 1) return "0";

  let leftHalf = "";

  for (let i = 1; i < food.length; i++) {
    const countItem = Math.floor(food[i] / 2);
    const eatItem = `${i}`.repeat(countItem);
    leftHalf += eatItem;
  }

  const rightHalf = leftHalf.split("").reverse().join("");

  return leftHalf + "0" + rightHalf;
}
