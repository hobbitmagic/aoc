"""Challenge 2"""
COLOR_LIMITS = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def main():
    """Main func"""
    with open("input.txt", "rt", encoding='UTF-8') as file:
        total_ids = 0
        for line in file:
            line_split = line.strip().split(':')
            game_id =  int("".join(c for c in line_split[0] if c.isdigit()))
            sets = line_split[1].split(';')
            if check_sets(sets):
                total_ids += game_id
    print(total_ids)

def check_sets(sets):
    """Checks if any color in all given sets exceed their limit"""
    for one_set in sets:
        pairs = one_set.split(',')
        for pair in pairs:
            pair = pair.strip().split(' ')
            if COLOR_LIMITS[pair[1]] < int(pair[0]):
                return False
    return True

if __name__ == "__main__":
    main()
