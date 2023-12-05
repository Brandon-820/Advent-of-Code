# There are multiple ways to open files. See https://sl.bing.net/dmS4VfKi4Ps
# open the file in read mode

import re

class Solution:
    def solutionCode(self, fileName: str) -> int:
        with open(fileName, "r") as file:
            # use a list comprehension to strip the newline characters
            data = [line.strip() for line in file]
            # print the list
            # print(data)

        def strToNum(rawData:str):
            word_map = {
                'one': '1',
                'two': '2',
                'three': '3',
                'four': '4',
                'five': '5',
                'six': '6',
                'seven': '7',
                'eight': '8',
                'nine': '9'
            }
            newData = []
            for string in rawData:
                newString = re.sub(r'one|two|three|four|five|six|seven|eight|nine', lambda x: word_map[x.group()], string, flags=re.IGNORECASE)
                newData.append(newString)
                print(newString)

            return newData

        def getSum(data:str) -> None:
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

        # getSum(strToNum(data))
        strToNum(data)




# Unit Test
test = Solution()
directory = 'D1P2'
fileName = '\example.txt'
test.solutionCode(directory+fileName)


# fileName = '\data.txt'
# test.solutionCode(directory+fileName)
