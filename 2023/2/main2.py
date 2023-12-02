"""Challenge 2"""

def main():
    """Main func"""
    with open("input.txt", "rt", encoding='UTF-8') as file:
        total_power = 0
        for line in file:
            line_split = line.strip().split(':')
            sets = line_split[1].split(';')
            total_power += check_sets(sets)
    print(total_power)

def check_sets(sets):
    """Calculates for minimum color cubes needed in given sets"""
    color_power = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    for one_set in sets:
        pairs = one_set.split(',')
        for pair in pairs:
            pair = pair.strip().split(' ')
            if color_power[pair[1]] < int(pair[0]):
                color_power[pair[1]] = int(pair[0])
    return color_power['red'] * color_power['green'] * color_power['blue']

if __name__ == "__main__":
    main()
