const solution = (wallpaper) => {
  let answer = [0, 0, 0, 0];
  let idx = [];

  wallpaper = wallpaper
    .map((v, i) => {
      const index = v.indexOf("#");
      const lastIndex = v.lastIndexOf("#") + 1;
      const check = v.includes("#");

      if (check) idx.push(index, lastIndex);

      return check && i;
    })
    .filter((v) => v !== false);

  answer[0] = Math.min(...wallpaper);
  answer[2] = Math.max(...wallpaper) + 1;
  answer[1] = Math.min(...idx);
  answer[3] = Math.max(...idx);

  return answer;
};
