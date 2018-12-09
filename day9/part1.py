SPECIAL_MARBLE_WORTH = 23
REMOVING_MARBLE_INDEX = -7

num_of_players = 452
last_marble_worth = 70784

marbles = [0]

active_marble_worth = 1
current_marble_index = 0
current_player = 0

scores = {}
for i in range(0, num_of_players):
    scores[i] = 0

while active_marble_worth <= last_marble_worth:

    if active_marble_worth % SPECIAL_MARBLE_WORTH == 0:
        scores[current_player] += active_marble_worth
        index_to_remove = (current_marble_index + REMOVING_MARBLE_INDEX) % len(marbles)
        scores[current_player] += marbles[index_to_remove]
        del marbles[index_to_remove]
        current_marble_index = index_to_remove
    else:
        index_of_insertion = (current_marble_index + 2) % len(marbles)
        marbles.insert(index_of_insertion, active_marble_worth)
        current_marble_index = index_of_insertion

    current_player = (current_player + 1) % num_of_players
    active_marble_worth += 1

high_score = max(scores.values())
print("High score: ", high_score)
