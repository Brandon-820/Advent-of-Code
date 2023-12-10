import sys
import re

# INPUT = "D6P1\example.txt"
INPUT = "D6P1\data.txt"

with open(INPUT, "r") as dataFile:
    data = dataFile.read()

dataSet = []

for m in re.finditer(r"\w+:(\s+\d+)+", data):
    dataSet.append([int(num) for num in re.findall(r"\d+", m.group(0))])

# dataSet[0] is Maximum Time to Win for each game
# dataSet[1] is Minimum Distance to Win for each game
# Speed = Spent-Time * 1
# Traveled Time = Maximum Time to Win - Spent-Time
# Traveled Time * Speed = Traveled Distance
# len(dataSet[0]) is the number of games
# Winning conditions are: (Spent-Time + Travel Time) < Maximum Time to Win and Traveled Distance > Minimum Distance to Win
# Output: number of ways to win each game
def waysToWin(dataSet):
    ways = []
    for i in range(len(dataSet[0])): # for each game
        ways.append(0)
        for spent_time in range(dataSet[0][i] + 1):  # for each spent-time # j is the spent-time
            if ((spent_time * 1) * (dataSet[0][i] - spent_time)) > dataSet[1][i]: # dataSet[1][i] is the minimum distance to win
                ways[i] += 1
    return ways

ways = waysToWin(dataSet)

from functools import reduce
numberOfWays = reduce(lambda x, y: x * y, ways)

print(dataSet)
print(waysToWin(dataSet))
print(numberOfWays)
