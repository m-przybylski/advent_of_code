const { run, run2 } = require("./day6")

describe("Day 5", () => {
const input = `Time:      7  15   30
Distance:  9  40  200`
    test("should pass part 1", () => {
        const result = run(input)
        expect(result).toEqual(288)
    })

    test("should pass part 2", () => {
        const result = run2(input)
        expect(result).toEqual(71503)
    })

})