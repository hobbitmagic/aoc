"""Challenge 7A"""

from functools import cmp_to_key

def main():
    """Main"""
    hands = []
    with open("input.txt", "rt", encoding='UTF-8') as file:
        for line in file:
            line = line.strip()
            # print(line)
            cards, bid = line.split()
            hand_type = check_hand_type(cards)
            hands.append({"cards": cards, "bid": int(bid), "type": hand_type})
    # print(hands)

    hands = sorted(hands, key=cmp_to_key(custom_sort), reverse=True)
    # print(hands)
    print(calculate_winning_sum(hands))
    # wrong 249748891

def calculate_winning_sum(hands):
    """Calculate total: all the winning bids multiplied by multiplier"""
    total = 0
    multiplier = len(hands)
    print(multiplier)
    for ind, hand in enumerate(hands):
        # print(hand["bid"], "*", multiplier-hands.index(hand))
        total += (hand["bid"]*(multiplier-ind))
    return total

def check_hand_type(cards):
    """Checks each hand type and ranks it 1-7"""
    count = {}
    for card in cards:
        if card in count:
            count[card] += 1
        else:
            count[card] = 1
    count_list = list(count.values())
    count_list.sort(reverse=True)
    # print(count_list)
    hand_type = count_list[0]
    if count_list[0] == 3 and count_list[1] == 2:
        # full_house
        hand_type = 5
    elif count_list[0] == 2 and count_list[1] == 2:
        # two_pair
        hand_type = 3
    elif hand_type == 3:
        hand_type = 4
    elif hand_type == 4:
        hand_type = 6
    elif hand_type == 5:
        hand_type = 7
    # else hand_type = highest repeated card 1 or 2

    # print(hand_type)
    return hand_type

def custom_sort(a, b):
    """Compare card type and individual cards if needed"""
    card_list = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    if a["type"] > b["type"]:
        return 1
    if a["type"] == b["type"]:
        for i in range(0, 5):
            if card_list.index(a["cards"][i]) > card_list.index(b["cards"][i]):
                return 1
            if card_list.index(a["cards"][i]) < card_list.index(b["cards"][i]):
                return -1
        return 0
    return -1

if __name__ == "__main__":
    main()
