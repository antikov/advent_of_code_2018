import re

class Node:
    def __init__(self, prev, next, value):
        self.prev = prev
        self.next = next
        self.value = value

def del_node(node):
    next = node.next
    prev = node.prev
    prev.next = next
    next.prev = prev
    return next

def insert_node(value, prev, next):
    node = Node(prev, next, value)
    prev.next = node
    next.prev = node
    return node

def get_score(players, marbles):
    stack = Node(None, None, 0)
    stack.prev = stack
    stack.next = stack
    curr_marble = stack
    scores = [0] * players
    for i in range(1, marbles + 1):
        if i % 23 == 0:
            curr_player = (i - 1) % players
            for _ in range(7):
                curr_marble = curr_marble.prev
            scores[curr_player] += i + curr_marble.value
            curr_marble = del_node(curr_marble)
        else:
            curr_marble = curr_marble.next
            curr_marble = insert_node(i, curr_marble, curr_marble.next)

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