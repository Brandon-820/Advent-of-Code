import re

INPUT = "D4P1\data.txt"

with open(INPUT, "r") as dataFile:
    data = dataFile.read()

dataSet = {}

for m in re.finditer(r"(Card\s+(\d+):(((\s+\d+)+ \|)(\s+\d+)+))", data):
    card_num = int(m.group(2))
    numbers = [[int(num) for num in re.findall(r"\d+", part)]
               for part in m.group(3).split('|')]
    dataSet[card_num] = numbers

total_points = 0

for card in dataSet.values():
    counter = 0
    for num in card[1]:
        if num in card[0]:
            counter += 1
    if counter > 0:
        total_points += 2 ** (counter - 1)

print(total_points)

