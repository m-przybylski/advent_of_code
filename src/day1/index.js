const fs = require("fs")
const path = require("path")
const { run2 } = require("./day1")
const contents = fs.readFileSync(path.join("input", "day1"), "utf8")

const result = run2(contents)
console.log(result);