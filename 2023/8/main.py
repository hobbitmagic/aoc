"""Challenge 8A"""

DIRECTIONS = ''
MOVES = 0
NODES = {}
POINTER = 0

def main():
    """Main"""
    global DIRECTIONS, NODES, MOVES, POINTER
    with open("input-sample2.txt", "rt", encoding='UTF-8') as file:
        first_line = True
        for line in file:
            line = line.strip()
            if line == '' or line is None:
                continue
            # print(line)
            if first_line:
                first_line = False
                DIRECTIONS = line
                continue
            # print(line)
            node, info = line.replace('(','').replace(')','').split(' = ')
            NODES[node] = info.split(', ')
    # print(DIRECTIONS)
    DIRECTIONS = DIRECTIONS.replace('L', '0').replace('R', '1')
    # print(DIRECTIONS)
    # print(NODES)
    next_node = 'AAA'
    while next_node != 'ZZZ':
        MOVES += 1
        if POINTER > (len(DIRECTIONS)-1):
            POINTER -=  (len(DIRECTIONS))
        current_node = NODES[next_node]
        next_node = current_node[int(DIRECTIONS[POINTER])]
        POINTER += 1

    print("Total moves:", MOVES)

if __name__ == "__main__":
    main()
