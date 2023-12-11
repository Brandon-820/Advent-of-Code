# INPUT = "D8P1\example.txt"
# INPUT = "D8P1\example2.txt"
INPUT = "D8P1\data.txt"

'''
dataFile = """
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""

instruction = "RL"
network = {'AAA': ()'BBB', 'CCC'), 'BBB': ('DDD', 'EEE'), 'CCC': ('ZZZ', 'GGG'), 'DDD': ('DDD', 'DDD'), 'EEE': ('EEE', 'EEE'), 'GGG': ('GGG', 'GGG'), 'ZZZ': ('ZZZ', 'ZZZ')}
'''
with open(INPUT, "r") as dataFile:
    data = dataFile.read()
    instructions = data.splitlines()[0]
    network = {}
    for line in data.splitlines()[2:]:
        node, children = line.split(' = ')
        network[node] = tuple(children[1:-1].split(', ')) # children[1:-1] removes the parentheses from the children

# iterate instructions and starting from network['AAA'].
# if instruction is R, go to the right child. if instruction is L, go to the left child.
#

def follow_instructions(instructions, network):
    node = 'AAA'
    steps = 0
    while node != 'ZZZ': # while node is not the exit node
        for instruction in instructions:
            if instruction == 'R':
                node = network[node][1]
            elif instruction == 'L':
                node = network[node][0]
            steps += 1

    return steps

print(follow_instructions(instructions, network))


