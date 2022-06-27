const solution = (input) => {
  const stringArr = [];
  let numSum = 0;
  input
    .split("")
    .map((item) =>
      parseInt(item) ? (numSum += parseInt(item)) : stringArr.push(item)
    );
  stringArr.sort();
  return stringArr.join("") + numSum;
};

console.log(solution("K1KA5CB7"));
console.log(solution("AJKDLSI412K4JSJ9D"));
