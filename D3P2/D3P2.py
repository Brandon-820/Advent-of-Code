import string

class Solution:
    def solutionCode(self, fileName: str) -> int:
        def sum_gear_ratios(schematic):
            # Parse the schematic into a 2D array (called schematic_parse) of numbers and symbols. As the example below, '467' becomes [467, 467, 467] and '...' becomes ['.', '.', '.']
            # '467..114..' -> [[467, 467, 467 '.', '.', 114, 114, 114, '.', '.']]
            # '...*......' -> [['.', '.', '.', '*', '.', '.', '.', '.', '.']]
            # '..35..633.' -> [['.', '.', 35, 35, '.', '.', 633, 633, 633, '.']
            # '3..*..*...' -> [[3, '.', '.', '*', '.', '.', '*', '.', '.', '.']]
            # '617*......' -> [[617, 617, 617, '*', '.', '.', '.', '.', '.', '.']]
            # '.....+.58.' -> [['.', '.', '.', '.', '.', '+', '.', 58, 58, '.']]
            schematic_parse = []
            for line in schematic:
                line_parse = []
                for cell in line:
                    if cell.isdigit():
                        line_parse.append(int(cell))
                    else:
                        line_parse.append(cell)
                schematic_parse.append(line_parse)

            # Define the eight possible directions to check
            directions = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if i != 0 or j != 0]

            total_ratio = 0

            # Iterate over each cell in the array
            for i in range(len(schematic_parse)):
                for j in range(len(schematic_parse[i])):
                    # If the cell contains a '*', check its surrounding cells
                    if schematic_parse[i][j] == '*':
                        part_numbers = []
                        for di, dj in directions:
                            ni, nj = i + di, j + dj
                            if 0 <= ni < len(schematic_parse) and 0 <= nj < len(schematic_parse[ni]) and isinstance(schematic_parse[ni][nj], int):
                                part_numbers.append(schematic_parse[ni][nj])
                        # If exactly two of the surrounding cells contain numbers, calculate the gear ratio
                        if len(part_numbers) == 2:
                            total_ratio += part_numbers[0] * part_numbers[1]

            return total_ratio

            # Define the eight possible directions to check
            directions = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if i != 0 or j != 0]

            total_ratio = 0

            # Iterate over each cell in the array
            for i in range(len(schematic)):
                for j in range(len(schematic[i])):
                    # If the cell contains a '*', check its surrounding cells
                    if schematic[i][j] == '*':
                        part_numbers = []
                        for di, dj in directions:
                            ni, nj = i + di, j + dj
                            if 0 <= ni < len(schematic) and 0 <= nj < len(schematic[ni]) and isinstance(schematic[ni][nj], int):
                                part_numbers.append(schematic[ni][nj])
                        # If exactly two of the surrounding cells contain numbers, calculate the gear ratio
                        if len(part_numbers) == 2:
                            total_ratio += part_numbers[0] * part_numbers[1]

            return total_ratio

        with open(fileName, "r") as file:
            lines = file.read().splitlines()
            return sum_gear_ratios(lines)



# Unit Test
test = Solution()
directory = 'D3P1'
fileName = '\example.txt'
result = test.solutionCode(directory+fileName)
print('example:', result)


fileName = '\data.txt'
result = test.solutionCode(directory+fileName)
print('data:', result)
