numbers_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def main():
    sum = 0
    # read file
    with open('input.txt') as file:
        rows = file.readlines()
    # loop through each row and get the first and last number
    for row in rows:
        numbers = find_numbers(row)
        first_number = numbers[0] 
        last_number = numbers[-1]

        calibration_value = int(first_number + last_number)
        sum += calibration_value
        
    print(sum)

def find_numbers(sequence):
    numbers = []
    for index, character in enumerate(sequence):
        # check if character is a number
        try:
            number = int(character)
            numbers.append(character)
        except ValueError:
            pass # not a number
        # check if character is part of a word
        characters = ""
        for character in sequence[index:]:
            characters += (character)
            if characters in numbers_map.keys():
                number = numbers_map[characters]
                numbers.append(number)
    return numbers


if __name__ == "__main__":
    main()