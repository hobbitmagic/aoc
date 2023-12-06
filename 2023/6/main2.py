"""Challenge 6A"""

def main():
    """Main"""
    file = open("input.txt", "rt", encoding='UTF-8')
    time_line = file.readline().strip()
    dist_line = file.readline().strip()
    file.close()
    print(time_line)
    print(dist_line)
    _, time_line = time_line.split(':')
    total_time = int(time_line.replace(" ", ""))
    _, dist_line = dist_line.split(':')
    prev_dist = int(dist_line.replace(" ", ""))
    print("Total Time", total_time)
    print("Record Distance", prev_dist)
    victories = calculate_ways_to_win(total_time, prev_dist)

    print("Total victories:", victories)

def calculate_ways_to_win(total_time, prev_dist):
    """Calculates possible ways to win for a given time and record"""
    i = 0
    current_victories = 0
    while i < total_time:
        hold = i
        dist = (total_time - hold)*hold
        if dist > prev_dist:
            current_victories += 1
        i += 1
    return current_victories

if __name__ == "__main__":
    main()
