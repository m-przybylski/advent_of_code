const { run, run2 } = require('./day1')

describe("day1", () => {
    const input = `1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet`
    test("should calculate sum", () => {
        expect(run(input)).toEqual(142)
    })

    test("should calculate sum", () => {
        const input = `two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen`
        expect(run2(input)).toEqual(281)
    })

    test("should replace valid", () => {
        const input = 'two3leighttvpkfmjhhonefour'

        expect(run2(input)).toEqual(24)
    })

    test("should replace valid", () => {
        const input = 'jzb1oneightqqr'

        expect(run2(input)).toEqual(18)
    })
})