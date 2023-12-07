import string

class Solution:
    def solutionCode(self, fileName: str) -> int:
        def sum_part_numbers(schematic):
            # symbols = {'*', '#', '+', '$', '='} - {'.'}

            symbols = set(string.printable) - set(string.digits) - set('.')
            total = 0
            rows, cols = len(schematic), len(schematic[0])

            # Create a visited array to keep track of the cells we've already processed
            visited = [[False]*cols for _ in range(rows)]

            for i in range(rows):
                for j in range(cols):
                    if schematic[i][j].isdigit() and not visited[i][j]:
                        num = ''
                        stack = [(i, j)]

                        # Use a depth-first search to find all digits of the number
                        while stack:
                            x, y = stack.pop()
                            if 0 <= x < rows and 0 <= y < cols and schematic[x][y].isdigit() and not visited[x][y]:
                                num += schematic[x][y]
                                visited[x][y] = True
                                for d_row in [-1, 0, 1]:
                                    for d_column in [-1, 0, 1]:
                                        stack.append((x+d_row, y+d_column))

                        # Check if the number is adjacent to a symbol
                        for d_row in [-1, 0, 1]:
                            for d_column in range(-1, len(num) + 1):
                                nx, ny = i + d_row, j + d_column
                                if 0 <= nx < rows and 0 <= ny < cols and schematic[nx][ny] in symbols:
                                    total += int(num)
                                    break
            return total

        with open(fileName, "r") as file:
            lines = file.read().splitlines()
            return sum_part_numbers(lines)


# Unit Test
test = Solution()
directory = 'D3P1'
fileName = '\example.txt'
result = test.solutionCode(directory+fileName)
print('example:', result)


fileName = '\data.txt'
result = test.solutionCode(directory+fileName)
print('data:', result)
