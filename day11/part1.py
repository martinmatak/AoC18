import numpy as np

GRID_SERIAL_NUMBER = 7857


GRID_WIDTH = 300
GRID_HEIGHT = 300

SQUARE_LENGTH = 3


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


def compute_power_square(top_left_x, top_left_y, power_levels):
    total_power = 0

    for i in range(0, SQUARE_LENGTH):
        for j in range(0, SQUARE_LENGTH):
            total_power += power_levels[top_left_x + i][top_left_y + j]

    return total_power


power_levels = np.zeros((GRID_WIDTH + 1, GRID_HEIGHT + 1))

for x in range(1, GRID_WIDTH):
    for y in range(1, GRID_HEIGHT):
        power_levels[x][y] += compute_power_level(x, y)

max_power = None
top_left = None
for x in range(1, GRID_WIDTH - 2):
    for y in range(1, GRID_HEIGHT - 2):
        square_power = compute_power_square(x, y, power_levels)
        if max_power is None or max_power < square_power:
            max_power = square_power
            top_left = (x, y)

print("x, y: ", top_left)
print("total power: ", max_power)

