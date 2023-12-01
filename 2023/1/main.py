"""Challenge 1 both parts"""

def main():
    """Main func"""
    with open("input.txt", "rt", encoding='UTF-8') as file:

        total = 0
        for line in file:
            line = line.strip()
            first_number = None
            second_number = None
            for i, _ in enumerate(line):
                char = line[i]
                if char.isdigit():
                    second_number = char
                    if first_number is None:
                        first_number = char
                else:
                    word = check_number(line, i)
                    if word > 0:
                        # print("Found: " + str(word) + " at position " + str(i))
                        second_number = word
                        if first_number is None:
                            first_number = word
            number = int(str(first_number)  + str(second_number))
            # print(number)
            total += number
        print(total)

def check_number(string, position):
    """Check if spelled out number exists at specific position in a string"""
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for p, _ in enumerate(words):
        if string.find(words[p], position, len(words[p])+position) != -1:
            return p+1
    return -1

if __name__ == "__main__":
    main()
