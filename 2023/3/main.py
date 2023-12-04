"""Challenge 3A"""

def main():
    """Main"""
    numbers_map, special_map = create_maps()
    total_parts = count_parts(numbers_map, special_map)
    print(total_parts)

def create_maps():
    """Reads input file and creates a map of numbers and a map of special characters"""
    numbers_map, special_map = {}, []
    with open("input.txt", "rt", encoding='UTF-8') as file:
        line_number = 1
        for line in file:
            line = line.strip()
            print(line_number, line)
            previous_number = None
            previous_position = None
            for char_position, char in enumerate(line):
                if char.isdigit():
                    # Digit case
                    if previous_number is not None:
                        # Continue previous number
                        previous_number = int(str(previous_number) + str(char))
                        numbers_map[str(line_number)][str(previous_position)] = previous_number
                        continue

                    # Record new number
                    # print(line_number, char_position)
                    if str(line_number) not in numbers_map:
                        numbers_map[str(line_number)] = {}
                    numbers_map[str(line_number)][str(char_position)] = char
                    previous_number=char
                    previous_position=char_position
                elif char == '.':
                    # Dot
                    previous_number = None
                    previous_position = None
                else:
                    # Special character
                    if line_number == 9 and char_position == 3:
                        print("found something")
                    special_map.append({line_number: char_position})
                    previous_number = None
                    previous_position = None
            # Reset for new line
            previous_number = None
            previous_position = None
            line_number += 1
        print("numbers map:", numbers_map)
        print("special map:", special_map)
    return numbers_map, special_map

def count_parts(numbers_map, special_map):
    """Counts all the numbers adjacent to special characters"""
    total = 0
    for spec_pair in special_map:
        for spec_line, spec_position in spec_pair.items():
            if str(int(spec_line)-1) in numbers_map:
                # previous line
                numbers_map, line_total = add_numbers(numbers_map, str(int(spec_line)-1), spec_position)
                total += line_total
            if str(int(spec_line)) in numbers_map:
                # current line
                numbers_map, line_total = add_numbers(numbers_map, str(int(spec_line)), spec_position)
                total += line_total
            if str(int(spec_line)+1) in numbers_map:
                # next line
                numbers_map, line_total = add_numbers(numbers_map, str(int(spec_line)+1), spec_position)
                total += line_total
    print("numbers map:", numbers_map)

    return total

def add_numbers(numbers_map, line_number, spec_position):
    """Adds numbers in a given line adjacent to given position"""
    line_total = 0
    number_line = numbers_map[line_number]
    for number_position in number_line:
        number = int(number_line[number_position])
        # print(number_position, number)
        if number == 664:
            print(range(int(number_position)-1, int(number_position)+len(str(number))+1), spec_position)
        if spec_position in range(int(number_position)-1, int(number_position)+len(str(number))+1):
            line_total += number
            # Make sure we don't count any numbers twice
            numbers_map[line_number][number_position] = 0
    return numbers_map, line_total

if __name__ == "__main__":
    main()
