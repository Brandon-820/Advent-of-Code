# reference: https://www.reddit.com/r/adventofcode/comments/18df7px/comment/kcqkq3c/?utm_source=reddit&utm_medium=web2x&context=3
# INPUT = "D8P2\example.txt"
# INPUT = "D8P2\example2.txt"
INPUT = "D8P2\data.txt"

with open(INPUT, "r") as dataFile:
    data = dataFile.read()
    instructions = data.splitlines()[0]
    network = {}
    for line in data.splitlines()[2:]:
        node, children = line.split(' = ')
        network[node] = tuple(children[1:-1].split(', ')) # children[1:-1] removes the parentheses from the children



def get_steps(node):
    steps = 0
    while not(node[2] == 'Z'): # while node is not the exit node
        for instruction in instructions:
            if instruction == 'R':
                node = network[node][1]
            elif instruction == 'L':
                node = network[node][0]
            steps += 1

    return steps

initalNode = [node for node in network if node[2] == 'A']

import math
print(math.lcm(*[get_steps(node) for node in initalNode]))




