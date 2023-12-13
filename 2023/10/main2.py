"""Challenge 10B"""

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
    # moves = 1

    next_direction, temp_position = check_right(spos, matrix)
    if next_direction is False:
        next_direction, temp_position = check_down(spos, matrix)
    if next_direction is False:
        next_direction, temp_position = check_left(spos, matrix)
    if next_direction is False:
        next_direction, temp_position = check_up(spos, matrix)

    border = []
    while temp_position is not False:
        # print(type(temp_position))
        border.append(temp_position)
        # moves += 1
        match next_direction:
            case "right":
                next_direction, temp_position = check_right(temp_position, matrix)
            case "down":
                next_direction, temp_position = check_down(temp_position, matrix)
            case "left":
                next_direction, temp_position = check_left(temp_position, matrix)
            case "up":
                next_direction, temp_position = check_up(temp_position, matrix)

    # print("Moves:", moves)
    inside = 0
    # print(matrix)
    # print("Height", HEIGHT)
    # print("Width", WIDTH)
    for i in range(0, HEIGHT):
        for j in range(0, WIDTH):
            print("Checking", i, j, "out of", HEIGHT, WIDTH)
            count_lines = 0
            came_from = ''
            if (i, j) not in border:
                if 'S' in matrix[i]:
                    inside = check_vertically(inside, i, j, border, matrix)
                else:
                    for checkpoint in range(j+1, WIDTH):
                        if (i, checkpoint) in border:
                            symbol = matrix[i][checkpoint]
                            if symbol == "|":
                                count_lines += 1
                            elif symbol == "L":
                                came_from = 'up'
                            elif symbol == "J":
                                if came_from == 'down':
                                    count_lines += 1
                                came_from = ''
                            elif symbol == 'F':
                                came_from = 'down'
                            elif symbol == '7':
                                if came_from == 'up':
                                    count_lines += 1
                                came_from = ''
                    if count_lines % 2 == 1:
                        inside += 1

    print("Area =", inside)

def check_vertically(inside, i, j, border, matrix):
    '''Checks if give position is inside by checking border crossings below it'''
    count_lines = 0
    came_from = ''
    for checkpoint in range(i+1, HEIGHT):
        if (checkpoint, j) in border:
            symbol = matrix[checkpoint][j]
            if symbol == "-":
                count_lines += 1
            elif symbol == "7":
                came_from = 'left'
            elif symbol == "L":
                if came_from == 'left':
                    count_lines += 1
                came_from = ''
            elif symbol == 'F':
                came_from = 'right'
            elif symbol == 'J':
                if came_from == 'right':
                    count_lines += 1
                came_from = ''
    if count_lines % 2 == 1:
        inside += 1

    return inside

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
