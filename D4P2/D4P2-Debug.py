import sys
import re

# INPUT = "D4P1\example.txt"
INPUT = "D4P1\data.txt"

with open(INPUT, "r") as dataFile:
    data = dataFile.read()

dataSet = {}

for m in re.finditer(r"(Card\s+(\d+):(((\s+\d+)+ \|)(\s+\d+)+))", data):
    card_num = int(m.group(2)) - 1
    numbers = [[(int(num)) for num in re.findall(r"\d+", part)]
               for part in m.group(3).split('|')]
    dataSet[card_num] = numbers

total_points = 0
copies = [1] * len(dataSet)  # position 1 is the first copy
# copies[0] = 0  # position 0 is empty
for key, card in dataSet.items():
    counter = 0
    for num in card[1]:
        if num in card[0]:
            # copies[key] += 1
            counter += 1
    if counter > 0:
        try:
            for i in range(key + 1, key + counter + 1):
                copies[i] += copies[key]
        except IndexError:
            print("Index Error", "key:", key, "   counter:",counter, "   i:", i, "  len(copies):", len(copies), "   copies[]:", copies, "\n   dataSet:", dataSet)
            sys.exit()
    total_points = sum(copies)

print(total_points)

