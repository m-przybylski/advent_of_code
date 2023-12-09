function parseData(input) {
    const data = input.split("\n");
    const time = data[0].replace(/Time:(\s*)/, "").split(/\s+/)
    const distance = data[1].replace(/Distance:(\s*)/, "").split(/\s+/)
    return time.map((t, i) => {
        return { time: t, distance: distance[i] }
    })
}

function parseData2(input) {
    const data = input.split("\n");
    const time = data[0].replace(/Time:(\s*)/, "").split(/\s+/).join("")
    const distance = data[1].replace(/Distance:(\s*)/, "").split(/\s+/).join("")
    return {
        time: +time, distance: +distance
    }

}

function run (input) {
    const data = parseData(input)
    return data.map(race => {
        const raceTime = race.time
        let count = 0;
        for (let i = 0; i <= raceTime; i++) {
            const distance = i * (raceTime - i);
            if (distance > race.distance) {
                count++;
            }
            if (count && distance < race.distance) {
                break;
            }
        }
        return count;
    }).reduce((acc, cur) => {
        return acc * cur
    })
}

function run2 (input) {
    const race = parseData2(input)
    const raceTime = race.time
    let count = 0;
    for (let i = 0; i <= raceTime; i++) {
        const distance = i * (raceTime - i);
        if (distance > race.distance) {
            count++;
        }
        if (count && distance < race.distance) {
            break;
        }
    }
    return count;
}

module.exports = {
    run, run2
}