import re

def get_score(players, marbles):
    stack = [0]
    curr_marble = 0
    scores = [0] * players
    for i in range(1, marbles + 1):
        if i % 23 == 0:
            curr_player = (i - 1) % players
            curr_marble = (len(stack) + curr_marble - 7) % len(stack)
            scores[curr_player] += i + stack[curr_marble]
            del stack[curr_marble]
        else:
            curr_marble = (curr_marble + 2) % (len(stack))
            stack.insert(curr_marble, i)

    return max(scores)

assert get_score(9, 25) == 32
assert get_score(10, 1618) == 8317
assert get_score(13, 7999) == 146373
assert get_score(17, 1104) == 2764
assert get_score(21, 6111) == 54718
assert get_score(30, 5807) == 37305

def main():
    with open("input.txt", "r") as fin:
        parsed = re.match(r'(\d+) players; last marble is worth (\d+) points', fin.read().strip())
        num_players, last_marble = [int(x) for x in parsed.group(1,2)]
        print(get_score(num_players, last_marble * 100))

if __name__ == "__main__":
    main()