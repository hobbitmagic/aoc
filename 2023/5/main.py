"""Challenge 5A"""

TRANSLATOR = {}
DONE = []

def main():
    """Main"""
    source_category = ''
    dest_category = ''
    with open("input.txt", "rt", encoding='UTF-8') as file:
        for line in file:
            line = line.strip()
            # print(line)
            if 'seeds:' in line:
                record_seeds(line)
                _ = file.readline()
            elif line == '':
                copy_leftover_numbers(source_category, dest_category)
            elif '-to-' in line:
                source_category, dest_category = line.strip(' map:').split('-to-')
                TRANSLATOR[dest_category] = []
            else:
                process_from_to(source_category, dest_category, line)
    copy_leftover_numbers(source_category, dest_category)
    print(TRANSLATOR)
    print("The smallest number is: ", min(TRANSLATOR[dest_category]))

def copy_leftover_numbers(source_category, dest_category):
    """Check if all numbers copied or copy the ones that didn't"""
    for number in TRANSLATOR[source_category]:
        if int(number) not in DONE:
            TRANSLATOR[dest_category].append(int(number))
    DONE.clear()

def process_from_to(source_category, dest_category, line):
    """Convert numbers from one category to next and record them"""
    dest_start, source_start, range_length = line.split()
    for source_number in TRANSLATOR[source_category]:
        if int(source_number) in range(int(source_start), (int(source_start)+int(range_length))):
            DONE.append(int(source_number))
            TRANSLATOR[dest_category].append((int(source_number) + int(dest_start) - int(source_start)))

def record_seeds(line):
    """Parses seeds line and records it into dict"""
    _, line = line.split(':')
    TRANSLATOR["seed"] = []
    for seed in line.split():
        TRANSLATOR["seed"].append(int(seed))
    # print(TRANSLATOR)

if __name__ == "__main__":
    main()
