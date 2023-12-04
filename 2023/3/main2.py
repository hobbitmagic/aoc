"""Challenge 3B"""

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
                elif char == '*':
                    # Special character
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
            nearby_numbers = 0
            first_line_total = 0
            second_line_total = 0
            third_line_total = 0
            if str(int(spec_line)-1) in numbers_map:
                # previous line
                numbers_map, line_total, nearby_number_count = add_numbers(numbers_map, str(int(spec_line)-1), spec_position)
                nearby_numbers += nearby_number_count
                first_line_total += line_total
            if str(int(spec_line)) in numbers_map:
                # current line
                numbers_map, line_total, nearby_number_count = add_numbers(numbers_map, str(int(spec_line)), spec_position)
                nearby_numbers += nearby_number_count
                second_line_total += line_total
            if str(int(spec_line)+1) in numbers_map:
                # next line
                numbers_map, line_total, nearby_number_count = add_numbers(numbers_map, str(int(spec_line)+1), spec_position)
                nearby_numbers += nearby_number_count
                third_line_total += line_total
            if nearby_numbers == 2:
                print("Spec line found 2 adjacent on line", spec_line, first_line_total, second_line_total, third_line_total, total)
                total += ((first_line_total or 1) * (second_line_total or 1) *(third_line_total or 1))
    print("numbers map:", numbers_map)

    return total

def add_numbers(numbers_map, line_number, spec_position):
    """Add adjacent numbers in a given line and count numbers"""
    line_total = 0
    nearby_number_count = 0
    number_line = numbers_map[line_number]
    for number_position in number_line:
        number = int(number_line[number_position])
        # print(number_position, number)
        if spec_position in range(int(number_position)-1, int(number_position)+len(str(number))+1):
            if line_total == 0:
                line_total = number
            else:
                line_total *= number
            nearby_number_count += 1
            # Make sure we don't count any numbers twice
            numbers_map[line_number][number_position] = 0
    return numbers_map, line_total, nearby_number_count

if __name__ == "__main__":
    main()
