import numpy as np

GRID_SERIAL_NUMBER = 7857


GRID_WIDTH = 300
GRID_HEIGHT = 300


def compute_power_level(x, y):
    power_level = 0
    rack_id = x + 10
    power_level += rack_id * y
    power_level += GRID_SERIAL_NUMBER
    power_level *= rack_id
    hundredth_digit = int((power_level % 1000) / 100)
    power_level = hundredth_digit
    power_level -= 5
    return power_level


def compute_power_square(top_left_x, top_left_y, square_length_power_levels, square_length, power_levels):
    total_power = 0

    if square_length - 1 in square_length_power_levels:
        total_power = square_length_power_levels[square_length - 1][top_left_x][top_left_y]

    for i in range(0, square_length):
        total_power += power_levels[top_left_x + square_length - 1][top_left_y + i]
    # not to count twice the same corner
    for i in range(0, square_length - 1):
        total_power += power_levels[top_left_x + i][top_left_y + square_length - 1]

    return total_power


power_levels = np.zeros((GRID_WIDTH + 1, GRID_HEIGHT + 1))

for x in range(1, GRID_WIDTH):
    for y in range(1, GRID_HEIGHT):
        power_levels[x][y] += compute_power_level(x, y)

max_power = None
top_left_length = None
# here save the power levels for different square sizes and reuse them for computing the greater ones
square_length_power_levels = {1: power_levels}

for square_length in range(1, GRID_WIDTH + 1):

    if square_length not in square_length_power_levels:
        square_length_power_levels[square_length] = np.zeros((GRID_WIDTH - (square_length - 1) + 1, GRID_HEIGHT - (square_length - 1) + 1))

    for x in range(1, GRID_WIDTH - (square_length - 1)):
        for y in range(1, GRID_HEIGHT - (square_length - 1)):
            # print(x, y, square_length)
            square_power = compute_power_square(x, y, square_length_power_levels, square_length, square_length_power_levels[1])
            square_length_power_levels[square_length][x][y] = square_power
            if max_power is None or max_power < square_power:
                max_power = square_power
                top_left_length = (x, y, square_length)

print("x, y, length: ", top_left_length)
print("total power: ", max_power)

# TODO: use map of partial sums: https://en.wikipedia.org/wiki/Summed-area_table instead of this
