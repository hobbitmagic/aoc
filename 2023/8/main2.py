"""Challenge 8B"""

import math

def main():
    """Main"""

    directions = ''
    nodes = {}
    starting_nodes = []
    with open("input.txt", "rt", encoding='UTF-8') as file:
        first_line = True
        for line in file:
            line = line.strip()
            if line == '' or line is None:
                continue
            # print(line)
            if first_line:
                first_line = False
                directions = line
                continue
            # print(line)
            node, info = line.replace('(','').replace(')','').split(' = ')
            nodes[node] = tuple(info.split(', '))
            if node.endswith('A'):
                starting_nodes.append(node)
    print("Starting nodes:", starting_nodes)

    # print(directions)
    directions = list(directions.replace('L', '0').replace('R', '1'))
    directions = list(map(int, directions))
    # print(directions)
    # print(nodes)
    len_directions = len(directions)
    # print("Directions:", directions)
    # print("Nodes", nodes)
    node_moves = []
    for node in starting_nodes:
        print("Starting node:", node)
        temp_node = node
        temp_pointer = 0
        temp_moves = 0
        while True:
            temp_moves += 1
            temp_pointer %= len_directions
            # print("Pointer:", temp_pointer)
            # print("direction:", directions[temp_pointer])
            temp_node = nodes[temp_node][directions[temp_pointer]]
            # print("Temp node:", temp_node)
            temp_pointer += 1
            if temp_node[-1] == 'Z':
                node_moves.append(temp_moves)
                break

    print("Total moves:", math.lcm(*node_moves))

if __name__ == "__main__":
    main()
