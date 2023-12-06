const redCount = 12
const greenCount = 13
const blueCount = 14

function run(gameLog) {
    let sum = 0;
    gameLog.split("\n").map(game => {
        const split = game.split(": ")
        const gameId = +split[0].split(" ")[1]
        const games = split[1].split("; ").map(drawResult => {
            const cubes = drawResult.split(", ")
            return cubes.map(cube => cube.split(" ")).reduce((acc, cur) => {
                acc[cur[1]] = cur[0]
                return acc
            }, {
                red: 0,
                green: 0,
                blue: 0
            })
        })
        if (games.every(game => {
            return (
                game.red <= redCount && 
                game.blue <= blueCount && 
                game.green <= greenCount
            )
        })) {
            sum += gameId
        }
    })

    return sum;
}

function run2(gameLog) {
    let sum = 0;
    gameLog.split("\n").map(game => {
        const split = game.split(": ")
        const gameId = +split[0].split(" ")[1]
        const games = split[1].split("; ").map(drawResult => {
            const cubes = drawResult.split(", ")
            return cubes.map(cube => cube.split(" ")).reduce((acc, cur) => {
                acc[cur[1]] = cur[0]
                return acc
            }, {
                red: 0,
                green: 0,
                blue: 0
            })
        })
        const min = games.reduce((acc, cur) => {
            acc.red = Math.max(acc.red, cur.red)
            acc.blue = Math.max(acc.blue, cur.blue)
            acc.green = Math.max(acc.green, cur.green)
            return acc
        })

        sum += min.red * min.blue * min.green
    })

    return sum;
}

module.exports = {
    run, run2
}