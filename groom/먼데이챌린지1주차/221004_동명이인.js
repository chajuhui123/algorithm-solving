// Run by Node.js
const readline = require("readline");

(async () => {
  let rl = readline.createInterface({ input: process.stdin });

  const input = [];
  let answer = 0;

  for await (const line of rl) input.push(line);

  const solution = () => {
    const [N, targetName] = input.shift().split(" ");

    for (let name of input) {
      if (name.includes(targetName)) answer++;
    }

    console.log(answer);
  };

  solution();
  process.exit();
})();
