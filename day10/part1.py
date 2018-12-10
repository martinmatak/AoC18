fname = 'input.txt'

with open(fname) as f:
    content = f.readlines()
content = [x.strip() for x in content]

velocities = {}
positions = {}
coordinates = {}
num_of_points = 0

for line in content:
    splits = line.split(",")
    x = int(splits[0].split("<")[1])
    y = int(splits[1].split(">")[0].lstrip())
    velocity_x = int(splits[1].split("<")[1].lstrip())
    velocity_y = int(splits[-1].split(">")[0].lstrip())

    # initial position is id of the coordinate
    velocities[num_of_points] = (velocity_x, velocity_y)
    coordinates[num_of_points] = (x, y)
    positions[(x, y)] = num_of_points

    num_of_points += 1


def print_output(positions):
    x_min = min(position[0] for position in positions.keys())
    x_max = max(position[0] for position in positions.keys())
    y_min = min(position[1] for position in positions.keys())
    y_max = max(position[1] for position in positions.keys())

    for y in range(y_min, y_max + 1):
        for x in range(x_min, x_max + 1):
            if (x, y) in positions:
                print("#", end='')
            else:
                print(".", end='')
        print()


second = 0
treshold = 0.5
while True:

    # check for neighbours
    has_y_neighbour = 0
    for id, position in coordinates.items():
        x = position[0]
        y = position[1]
        if (x, y + 1) in positions or (x, y - 1) in positions:
            has_y_neighbour += 1

    # if more than treshold coordinates have a neighbour - here we are :)
    if has_y_neighbour * 1.0 / len(positions) > treshold:
        print("Second:", second)
        print_output(positions)
        break

    # update coordinates
    positions.clear()
    for id, position in coordinates.items():
        new_x = position[0] + velocities[id][0]
        new_y = position[1] + velocities[id][1]
        coordinates[id] = (new_x, new_y)
        positions[(new_x, new_y)] = id

    second += 1




