# There are multiple ways to open files. See https://sl.bing.net/dmS4VfKi4Ps
# open the file in read mode

class Solution:
    def solutionCode(self, fileName: str) -> int:
        with open(fileName, "r") as file:
            # use a list comprehension to strip the newline characters
            data = [line.strip() for line in file]
            # print the list
            # print(data)


        sum = 0
        for string in data:
            digit1 = '#'
            digit2 = '#'
            for char in string:
                if char not in '123456789':
                    continue
                if digit1 == '#':
                    digit1 = digit2 = char
                else:
                    digit2 = char
            print(digit1 + digit2)
            sum += int(digit1 + digit2)
        print('sum:', sum)





# Unit Test
test = Solution()
fileName = 'example.txt'
directory = 'D1P1'
fileName = '\example.txt'
test.solutionCode(directory+fileName)


fileName = '\data.txt'
test.solutionCode(directory+fileName)

