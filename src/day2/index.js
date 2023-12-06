const fs = require("fs")
const path = require("path")
const { run2 } = require("./day2")
const contents = fs.readFileSync(path.join("input", "day2"), "utf8")

const result = run2(contents)
console.log(result);``