class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


SPECIAL_MARBLE_WORTH = 23

num_of_players = 452
last_marble_worth = 70784 * 100

current_marble = Node(0)
current_marble.next = current_marble
current_marble.previous = current_marble

active_marble_worth = 1
current_player = 0

scores = {}
for i in range(0, num_of_players):
    scores[i] = 0

while active_marble_worth <= last_marble_worth:

    if active_marble_worth % SPECIAL_MARBLE_WORTH == 0:
        scores[current_player] += active_marble_worth
        node = current_marble
        for _ in range(0, 7):
            node = node.previous
        scores[current_player] += node.value
        current_marble = node.next
        previous_node = node.previous
        previous_node.next = current_marble
        current_marble.previous = previous_node
    else:
        node = Node(active_marble_worth)
        node.next = current_marble.next.next
        node.previous = current_marble.next
        node.previous.next = node
        node.next.previous = node
        current_marble = node

    current_player = (current_player + 1) % num_of_players
    active_marble_worth += 1

high_score = max(scores.values())
print("High score: ", high_score)
