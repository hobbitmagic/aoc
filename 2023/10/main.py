"""Challenge 10A"""

HEIGHT = 0
WIDTH = 0

def main():
    """Main"""
    matrix = []
    global HEIGHT, WIDTH
    with open("input.txt", "rt", encoding='UTF-8') as file:
        for line in file:
            line = line.strip()
            if line == '' or line is None:
                continue
            HEIGHT += 1
            WIDTH = len(line)
            matrix.append(line)

    spos = (0,0)
    for i, line in enumerate(matrix):
        # print("line", i, line)
        if 'S' in line:
            spos = (i, line.index('S'))
    print(spos)

    temp_position = spos
    moves = 1

    next_direction, temp_position = check_right(spos, matrix)
    if next_direction is False:
        next_direction, temp_position = check_down(spos, matrix)
    if next_direction is False:
        next_direction, temp_position = check_left(spos, matrix)
    if next_direction is False:
        next_direction, temp_position = check_up(spos, matrix)

    while temp_position is not False:
        moves += 1
        match next_direction:
            case "right":
                next_direction, temp_position = check_right(temp_position, matrix)
            case "down":
                next_direction, temp_position = check_down(temp_position, matrix)
            case "left":
                next_direction, temp_position = check_left(temp_position, matrix)
            case "up":
                next_direction, temp_position = check_up(temp_position, matrix)

    print("Moves:", moves, moves/2)

def check_right(temp_position, matrix):
    '''Checks if position on the right connects'''
    if temp_position[1]+1 < WIDTH:
        # right
        direction = matrix[temp_position[0]][temp_position[1]+1]
        if direction in ("J", "-", "7"):

            # print("Right")
            temp_position = (temp_position[0], temp_position[1]+1)
            if direction == "J":
                return "up", temp_position
            if direction == "-":
                return "right", temp_position
            if direction == "7":
                return "down", temp_position

    return False, False

def check_down(temp_position, matrix):
    '''Checks if position below connects'''
    if temp_position[0]+1 <= HEIGHT:
        # down
        direction = matrix[temp_position[0]+1][temp_position[1]]

        if direction in ("J", "|", "L"):
            # print("Down")
            temp_position = (temp_position[0]+1, temp_position[1])
            if direction == "J":
                return "left", temp_position
            if direction == "|":
                return "down", temp_position
            if direction == "L":
                return "right", temp_position

    return False, False

def check_left(temp_position, matrix):
    '''Checks if position on the left connects'''
    if temp_position[1]-1 >= 0:
        # left
        direction = matrix[temp_position[0]][temp_position[1]-1]

        if direction in ("L", "-", "F"):
            # print("Left")
            temp_position = (temp_position[0], temp_position[1]-1)
            if direction == "F":
                return "down", temp_position
            if direction == "-":
                return "left", temp_position
            if direction == "L":
                return "up", temp_position

    return False, False

def check_up(temp_position, matrix):
    '''Checks if position above connects'''
    if temp_position[0]-1 >= 0:
        # up
        direction = matrix[temp_position[0]-1][temp_position[1]]

        if direction in ("F", "|", "7"):
            # print("Up")
            temp_position = (temp_position[0]-1, temp_position[1])
            if direction == "F":
                return "right", temp_position
            if direction == "|":
                return "up", temp_position
            if direction == "7":
                return "left", temp_position

    return False, False

if __name__ == "__main__":
    main()
