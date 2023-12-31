# There are multiple ways to open files. See https://sl.bing.net/dmS4VfKi4Ps
# open the file in read mode

import re

class Solution:
    def solutionCode(self, fileName: str) -> int:
        sum1 = 0
        sum2 = 0
        wordToInt = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
        }
        digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


        def convertToInt(s):
            if wordToInt.get(s) != None:
                return wordToInt[s]
            else:
                return int(s)


        def getCalibrationValue(pattern, line):
            matches = re.findall(pattern, line)
            if len(matches) > 0:
                fnum = convertToInt(matches[0])
                lnum = convertToInt(matches[len(matches) - 1])
                return fnum * 10 + lnum
            else:
                return 0

        with open(fileName, "r") as file:
            lines = file.read().splitlines()
            for line in lines:
                cv1 = getCalibrationValue(r"(\d)", line)
                # using positive lookahead to capture overlapping words like twone
                cv2 = getCalibrationValue(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line)
                sum1 += cv1
                sum2 += cv2

        print("Part 1 Sum", sum1)
        print("Part 2 Sum", sum2)





# Unit Test
test = Solution()
directory = 'D1P2'
fileName = '\example.txt'
test.solutionCode(directory+fileName)


fileName = '\data.txt'
test.solutionCode(directory+fileName)
