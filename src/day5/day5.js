function parseData(input) {
    const data = input.split("\n\n")
    const seeds = data.shift().split(" ").reduce((acc, cur) => { 
        if (cur.includes("seed")) {
            return acc
        }
        acc.push(Number.parseInt(cur))
        return acc
    }, [])

    const map = data.map(map => {
        const elements = map.split("\n")
        const [from, _, to] = elements.shift().replace(" map:", "").split("-")
        const maps = elements.filter(ranges => ranges).map(ranges => {
            const [dest, source, range] = ranges.split(" ").map(a => Number.parseInt(a, 10));
            return { source, dest, range }
        })
        
        return {
            from,
            to,
            maps
        }
    }).reduce((acc, cur) => {
        acc[cur.from] = cur
        return acc
    }, {})

    return {
        seeds,
        map
    }
}

function parseRangeData(input) {
    const data = input.split("\n\n")
    const seeds = data.shift().split(" ").filter((x) => !x.includes("seed")).reduce((acc, _, index, all) => {
        if (index % 2 == 0) {
            acc.push([ +all[index], +all[index + 1] ])
        }
        return acc
    }, [])

    const map = data.map(map => {
        const elements = map.split("\n")
        const [from, _, to] = elements.shift().replace(" map:", "").split("-")
        const maps = elements.filter(ranges => ranges).map(ranges => {
            const [dest, source, range] = ranges.split(" ").map(a => Number.parseInt(a, 10));
            return { source, dest, range }
        })
        
        return {
            from,
            to,
            maps
        }
    }).reduce((acc, cur) => {
        acc[cur.from] = cur
        return acc
    }, {})

    return {
        seeds,
        map
    }
}

function walk(source, type, maps) {
    const currentMap = maps[type];
    if (!currentMap) {
        return source;
    }
    
    const newType = currentMap.to;
    const mapToFollow = currentMap.maps.find(map => {
        return map.source <= source && map.source + map.range >= source
    })

    const newSource = mapToFollow === undefined ? source : mapToFollow.dest + (source - mapToFollow.source);
    
    return walk(newSource, newType, maps)
}

function run(input) {
    const { seeds, map } = parseData(input);

    let min = Infinity;
    seeds.forEach(seed => {
        const result = walk(seed, "seed", map);

        min = result > min ? min : result
    })

    return min
}

function run2(input) {
    const { seeds, map } = parseRangeData(input);

    let min = Infinity;
    seeds.forEach(seed => {
        for (let i = 0; i < seed[1]; i++) {
            const result = walk(seed[0] + i, "seed", map);
    
            min = result > min ? min : result
        }
    })

    return min
}

module.exports = {
    run, run2
}