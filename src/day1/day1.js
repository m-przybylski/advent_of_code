function run(input) {
    let sum = 0;
    const calibrationValues = input.split('\n')
    for(const calibrationValue of calibrationValues) {
        const firstDigit = new RegExp(/[0-9]/).exec(calibrationValue)[0]
        const lastDigit = new RegExp(/^.*([0-9]).*$/).exec(calibrationValue)[1]
        const dig = +`${firstDigit}${lastDigit}`;
        sum += dig;
    }

    return sum;
}

function run2(input) {
    function isDigit(char) {
        return /^\d$/.test(char);
      }

    const map = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    let sum = 0;
    const calibrationValues = input.split('\n')
    
    for(const calibrationValue of calibrationValues) {
        let num = []

        const textDigits = Object.keys(map);
        const reg = textDigits.join("|")
        const firstReplaceData = new RegExp(`(${reg})|([0-9])`).exec(calibrationValue)

        const firstFoundDigit = firstReplaceData[0];

        if (isDigit(firstFoundDigit)) {
            num.push(firstFoundDigit)
        } else {
            num.push(map[firstFoundDigit]);
        }

        const reverseReg = textDigits.map(key => key.split("").reverse().join("")).join("|")
        const reversedCalibrationValue = calibrationValue.split("").reverse().join("")
        const lastReplacedData = new RegExp(`(${reverseReg})|([0-9])`).exec(reversedCalibrationValue)
        const lastFoundDigit = lastReplacedData[0];
        
        if (isDigit(lastFoundDigit)) {
            num.push(lastFoundDigit)
        } else {
            num.push(map[lastFoundDigit.split("").reverse().join("")]);
        }
        
        sum += +num.join("");
    }

    return sum
}

module.exports = {
    run, run2
}