# INPUT = "D9P2\example.txt"  # Output：2
INPUT = "D9P2\data.txt" # Output： 1089

with open(INPUT, "r") as dataFile:
    data = dataFile.read()
    histories = []
    for line in data.splitlines():
        histories.append([int(num) for num in line.split()])
    # print(histories)


def extrapolate_and_sum(histories):
    total = 0
    for history in histories:
        historyTriangulation = []
        historyTriangulation.append(history)
        while True:
            differences = [history[i+1] - history[i] for i in range(len(history)-1)]
            if all(d == 0 for d in differences):
                historyTriangulation.append(differences)
                break
            else:
                history = differences
                historyTriangulation.append(differences)

        row = len(historyTriangulation) - 1
        historyTriangulation[row].insert(0, 0)
        for r in range(row, 0, -1):
            historyTriangulation[r-1].insert(0, historyTriangulation[r-1][0] - historyTriangulation[r][0])

        total += historyTriangulation[0][0]

    return total

print(extrapolate_and_sum(histories))  # Output: 114
