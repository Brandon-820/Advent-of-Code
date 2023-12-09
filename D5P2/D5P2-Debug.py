import re

# INPUT = "D5P1\example.txt"
INPUT = "D5P1\data.txt"

with open(INPUT, "r") as dataFile:
    data = dataFile.read()

data_dict = {}
key = None
for line in data.split('\n'):
    match = re.match(r'([\w\s-]+):', line)
    if not line.strip():
        key = None
        continue
    if match:
        key = match.group(1)
        data_dict[key] = []
        numbers = list(map(int, re.findall(r'\d+', line)))
        if numbers:
            data_dict[key].append(numbers)
    elif key and line.strip():
        numbers = list(map(int, re.findall(r'\d+', line)))
        if numbers:
            data_dict[key].append(numbers)

def getValueFromRange(lookUp, rangeMap):
    for input in rangeMap:
        destStart, sourceStart, rangeLen = input[0], input[1], input[2]
        if lookUp in range(sourceStart, sourceStart + rangeLen):
            return destStart + (lookUp - sourceStart)
    return lookUp

def getSeedMinLocation(seed, inputMap):
    soil = getValueFromRange(seed, inputMap["seed-to-soil map"])
    fertilizer = getValueFromRange(soil, inputMap["soil-to-fertilizer map"])
    water = getValueFromRange(fertilizer, inputMap["fertilizer-to-water map"])
    light = getValueFromRange(water, inputMap["water-to-light map"])
    temp = getValueFromRange(light, inputMap["light-to-temperature map"])
    humidity = getValueFromRange(temp, inputMap["temperature-to-humidity map"])
    loc	= getValueFromRange(humidity, inputMap["humidity-to-location map"])
    return	loc

minLoc = -1
seedsValue = iter(data_dict["seeds"][0])
for seedStart in seedsValue:
    seedLen = next(seedsValue)
    for seed in range(seedStart, seedStart + seedLen):
        loc = getSeedMinLocation(seed, data_dict)
        print(seed, loc)
        if minLoc == -1 or loc < minLoc:
            minLoc = loc

print(minLoc)
