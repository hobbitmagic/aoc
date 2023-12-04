"""Challenge 4B"""

def main():
    """Main"""
    with open("input.txt", "rt", encoding='UTF-8') as file:
        total = 0
        copies = []
        for line in file:
            multiplier = 1
            if len(copies) > 0:
                multiplier = copies.pop(0)
            total += multiplier
            line = line.strip()
            card, line = line.split(':')
            _, card = card.split()
            line = line.strip()
            winning_numbers, my_numbers = line.split('|')
            winning_numbers = winning_numbers.split()
            matching_count = sum(1 for number in my_numbers.split() if number in winning_numbers)
            # print(matching_count)
            for index in range(0, matching_count):
                if index < len(copies):
                    copies[index] += multiplier
                else:
                    copies.append(1+multiplier)

        print(total)

if __name__ == "__main__":
    main()
