const fs = require("fs");
content = fs.readFileSync("day12", "utf-8");
const a = JSON.parse(content);

count = 0;

function sumAllNumbers(obj) {
  if (typeof obj == "number") {
    return obj;
  }
  let sum = 0;
  const keys = Object.keys(obj);
  keys.forEach((key) => {
    if (typeof obj[key] === "number") {
      sum += obj[key];
    }

    if (typeof obj[key] === "object") {
      if (Array.isArray(obj[key])) {
        obj[key].forEach((x) => {
          sum += sumAllNumbers(x);
        });
      } else {
        sum += sumAllNumbers(obj[key]);
      }
    }
  });

  return sum;
}

console.log(sumAllNumbers(a));

function sumAllButNotRed(obj) {
  if (typeof obj == "number") {
    return obj;
  }
  let sum = 0;
  const keys = Object.keys(obj);
  if (!Array.isArray(obj)) {
    for (let i = 0; i < keys.length; i++) {
      if (obj[keys[i]] == "red") {
        return 0;
      }
    }
  }
  keys.forEach((key) => {
    if (typeof obj[key] === "number") {
      sum += obj[key];
    }

    if (typeof obj[key] === "object") {
      if (Array.isArray(obj[key])) {
        obj[key].forEach((x) => {
          sum += sumAllButNotRed(x);
        });
      } else {
        sum += sumAllButNotRed(obj[key]);
      }
    }
  });

  return sum;
}

console.log(sumAllButNotRed(a));
