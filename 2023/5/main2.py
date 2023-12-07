"""Challenge 5B"""
SEEDS = []
TRANSLATOR = {}

def main():
    """Main"""
    filename = 'input.txt'
    source_category = ''
    dest_category = ''
    with open(filename, "rt", encoding='UTF-8') as file:
        for line in file:
            line = line.strip()
            if 'seeds:' in line:
                record_seeds(line)

    final_results = []
    i = 0
    while i < len(SEEDS):
        TRANSLATOR.clear()
        result = None
        with open(filename, "rt", encoding='UTF-8') as file:
            record_temp_seed(i)
            i += 2
            for line in file:
                line = line.strip()
                if 'seeds:' in line:
                    _ = file.readline()
                elif line == '':
                    copy_leftover_numbers(source_category, dest_category)
                elif '-to-' in line:
                    # Set category names
                    source_category, dest_category = line.strip(' map:').split('-to-')
                    # print("Processing " + source_category + " into " + dest_category)
                    TRANSLATOR[dest_category] = []
                else:
                    # Process ranges from one category to next
                    process_from_to(source_category, dest_category, line)
            # Don't forget to copy unmatched ranges one last time
            copy_leftover_numbers(source_category, dest_category)
            for minimum in TRANSLATOR[dest_category]:
                if result is None:
                    result = minimum[0]
                elif minimum[0] < result:
                    result = minimum[0]
            print("Smallest number in this range is:", result)
            final_results.append(result)
    print("Smalled number in all sets is:", min(final_results))

def copy_leftover_numbers(source_category, dest_category):
    """Check if all ranges matched/translated or copy the ones that didn't"""
    # print("Copying leftovers", len(TRANSLATOR[source_category]) )
    TRANSLATOR[dest_category] += TRANSLATOR[source_category]
    TRANSLATOR[source_category] = []

def process_from_to(source_category, dest_category, line):
    """Compare and convert ranges from one category to next and record them"""
    new_source_ranges = []
    dest_start, source_start, range_length = map(int, line.split())
    diff = dest_start - source_start
    temp_range = range(source_start, (source_start+range_length))

    for source_range in TRANSLATOR[source_category]:
        temp_matches = range(max(source_range[0], temp_range[0]), min(source_range[-1], temp_range[-1])+1)

        if temp_matches:
            if source_range[0] < temp_matches[0]:
                new_source_ranges.append(range(source_range[0], temp_matches[0]))
            if source_range[-1] > temp_matches[-1]:
                new_source_ranges.append(range(temp_matches[-1], source_range[-1]))
            TRANSLATOR[dest_category].append(range(temp_matches[0]+diff, temp_matches[-1]+diff+1))
        else:
            new_source_ranges.append(source_range)

    TRANSLATOR[source_category] = new_source_ranges

def record_seeds(line):
    """Parses ALL seeds line and records it into dict"""
    _, line = line.split(':')
    for seed in line.split():
        SEEDS.append(int(seed))

def record_temp_seed(index):
    """Puts one pair of seeds into TRANSLATOR dict"""
    print("Recording seed range", SEEDS[index], SEEDS[index + 1])
    TRANSLATOR["seed"] = [range(SEEDS[index], (SEEDS[index] + SEEDS[index + 1]))]

if __name__ == "__main__":
    main()
