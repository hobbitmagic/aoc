"""Challenge 4A"""

def main():
    """Main"""
    with open("input.txt", "rt", encoding='UTF-8') as file:
        total = 0
        for line in file:
            line = line.strip()
            _, line = line.split(':')
            line = line.strip()
            winning_numbers, my_numbers = line.split('|')
            winning_numbers = winning_numbers.split()
            matching_count = sum(1 for number in my_numbers.split() if number in winning_numbers)
            # print(matching_count)
            if matching_count > 0:
                total +=  2 ** (matching_count-1)
        print(total)

if __name__ == "__main__":
    main()
