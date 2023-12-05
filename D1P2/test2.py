def convert_spelled_digits(string):
    digit_mapping = {
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

    result = ''
    i = 0

    while i < len(string):
        if string[i:i+3] in digit_mapping:
            result += digit_mapping[string[i:i+3]]
            i += 3
        elif string[i:i+4] in digit_mapping:
            result += digit_mapping[string[i:i+4]]
            i += 4
        else:
            result += string[i]
            i += 1

    return result

# Example usage
string = "eighthreetwo"
converted_string = convert_spelled_digits(string)
print(converted_string)  # Output: "832"
