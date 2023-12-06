
# read data from example.txt. Parse the data. Put the data into a hash map. Each set is separated by either ':' or ';'. The first set structure is dictionary {Game number}. The structure for the rest of sets is dictionary { blue: number, green: number, red: number}
# Data Example: Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green -> {1: [{'blue': 3, 'red': 4, 'green': 0}, {'blue': 6, 'red': 1, 'green': 2}, {'blue': 0, 'red': 0, 'green': 2}]}
# Data Example: Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue -> {2: [{'blue': 1, 'red': 0, 'green': 2}, {'blue': 4, 'red': 1, 'green': 3}, {'blue': 1, 'red': 0, 'green': 1}]}
# Code path: D2P1/test.py
# Data path: D2P1/data.txt

import re

class Solution:
    def solutionCode(self, fileName: str) -> int:
        data = {}
        with open(fileName, "r") as file:
            lines = file.read().splitlines()
            for line in lines:
                line = line.strip()
                if line.startswith("Game"):
                    game, numbers = line.split(":")
                    game_number = int(game.split()[1])
                    data[game_number] = []

                    sets = numbers.split(";")
                    for set_str in sets:
                        set_str = set_str.strip()
                        colors = re.findall(r"(\d+)\s+(\w+)", set_str)
                        color_data = {}
                        for count, color in colors:
                            color_data[color] = int(count)
                        data[game_number].append(color_data)
        # a function that take 'data' dictionary as input and return the desired result. The 'data' dictionary is in the following format:
        # 'data' format: {1: [{'blue': 3, 'red': 4}, {'red': 1, 'green': 2, 'blue': 6}, {'green': 2}], 2: [{'blue': 1, 'green': 2}, {'green': 3, 'blue': 4, 'red': 1}, {'green': 1, 'blue': 1}], 3: [{'green': 8, 'blue': 6, 'red': 20}, {'blue': 5, 'red': 4, 'green': 13}, {'green': 5, 'red': 1}], 4: [{'green': 1, 'red': 3, 'blue': 6}, {'green': 3, 'red': 6}, {'green': 3, 'blue': 15, 'red': 14}], 5: [{'red': 6, 'blue': 1, 'green': 3}, {'blue': 2, 'red': 1, 'green': 2}]}
        # Firstly, find the maximum number of blue, green and red in each game. The power of a set is equal to the numbers of maximum red, green, and blue number multiplied together.
        # secondly, find the maximum power of each game and add them together. This is the desired result.        #
        # Perform calculations on 'data' dictionary
        # Return the result as an integer value


        result = 0
        for game in data:
            max_blue = 0
            max_green = 0
            max_red = 0
            for set in data[game]:
                max_blue = max(max_blue, set.get('blue', 0))
                max_green = max(max_green, set.get('green', 0))
                max_red = max(max_red, set.get('red', 0))
            result += max_blue * max_green * max_red

        return result





# Unit Test
test = Solution()
directory = 'D2P1'
fileName = '\example.txt'
result = test.solutionCode(directory+fileName)
print('example:', result)


fileName = '\data.txt'
result = test.solutionCode(directory+fileName)
print('data:', result)
