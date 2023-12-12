# INPUT = "D9P1\example.txt"  # Output： 114
INPUT = "D9P1\data.txt"  # Output： 2101499000

with open(INPUT, "r") as dataFile:
    data = dataFile.read()
    histories = []
    for line in data.splitlines():
        histories.append([int(num) for num in line.split()])
    print(histories)


def extrapolate_and_sum(histories):
    total = 0
    for history in histories:
        lastNum = []
        while True:
            differences = [history[i+1] - history[i] for i in range(len(history)-1)]
            lastNum.append(history[-1])
            if all(d == 0 for d in differences):
                break
            else:
                history = differences
        total += sum(lastNum)
    return total

print(extrapolate_and_sum(histories))  # Output: 114
