"""Challenge 10A"""

import copy

def main():
    """Main"""
    matrix = []
    with open("input.txt", "rt", encoding='UTF-8') as file:
        for line in file:
            line = line.strip()
            if line == '' or line is None:
                continue
            matrix.append(line)
            # print(line)

    # calculate coordinates
    orig_galaxies = []
    for i, _ in enumerate(matrix):
        for j, _ in enumerate(matrix[0]):
            # print("checking", i, j)
            if matrix[i][j] == '#':
                orig_galaxies.append([i,j])

    # find empty lines
    empty_lines = []
    for i, line in enumerate(matrix):
        if '#' not in line:
            empty_lines.append(i)

    # find empty columns
    v = 0
    empty_columns = []
    width = len(matrix[0])
    while v < width:
        has_one = False
        for line in matrix:
            if '#' == line[v]:
                has_one = True
                break
        if has_one is False:
            # print("Found a vertical line without galaxies")
            empty_columns.append(v)

        v += 1

    print("Width", len(matrix[0]))
    print("Empty lines", empty_lines)
    print("Empty columns", empty_columns)
    print("BEFORE", orig_galaxies)
    mod_galaxies = copy.deepcopy(orig_galaxies)
    # print("BEFORE MOD", mod_galaxies)

    # adjust coordinates
    len_galaxies = len(orig_galaxies)
    for eline in empty_lines:
        for g in range(0, len_galaxies):
        # for galaxy in galaxies:
            if eline < orig_galaxies[g][0]:
                mod_galaxies[g][0] += 999999

    for ecolumn in empty_columns:
        for g in range(0, len_galaxies):
            if ecolumn < orig_galaxies[g][1]:
                mod_galaxies[g][1] += 999999

    # print("OLD", orig_galaxies)
    print("NEW", mod_galaxies)

    # check shortest paths
    total_dist = 0
    for a_galaxy in mod_galaxies:
        for b_galaxy in mod_galaxies:
            if a_galaxy == b_galaxy:
                continue
            total_dist += (abs(a_galaxy[0]-b_galaxy[0]) + abs(a_galaxy[1] - b_galaxy[1]))
    print("Total distance:", total_dist/2)

if __name__ == "__main__":
    main()
