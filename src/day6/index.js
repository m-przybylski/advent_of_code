
const fs = require("fs")
const path = require("path")
const { run, run2 } = require("./day6")
const contents = fs.readFileSync(path.join("input", "day6"), "utf8")

// const result = run(contents)
const result = run2(contents)
console.log(result);