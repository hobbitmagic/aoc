"""Challenge 9A"""

def main():
    """Main"""
    with open("input.txt", "rt", encoding='UTF-8') as file:
        total = 0
        for line in file:
            line = line.strip()
            if line == '' or line is None:
                continue

            numbers = []
            numbers.append(list(map(int,line.split())))

            print(numbers)
            line_num = 0
            while True:
                all_zeros = True
                numbers.append([])
                for index, number in enumerate(numbers[line_num]):
                    if index == 0:
                        continue
                    current = number - numbers[line_num][index-1]
                    if current != 0:
                        all_zeros = False
                    numbers[line_num + 1].append(current)
                if all_zeros:
                    break

                line_num += 1
            print(numbers)
            i = len(numbers) - 2
            temp_number = 0
            while i >= 0:
                temp_number = numbers[i][-1] + temp_number
                i -= 1
            total += temp_number


    print("ANSWER:", total)

if __name__ == "__main__":
    main()
