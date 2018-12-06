fname = 'input.txt'

with open(fname) as f:
    content = f.readlines()
content = [x.strip() for x in content]

stations = []

TRESHOLD = 10000

max_x = None
max_y = None
min_x = None
min_y = None
for line in content:
    splits = line.split(", ")
    x = int(splits[0]) + TRESHOLD
    y = int(splits[1]) + TRESHOLD
    stations.append((x, y))
    if max_x is None or x > max_x:
        max_x = x
    if min_x is None or x < min_x:
        min_x = x
    if max_y is None or y > max_y:
        max_y = y
    if min_y is None or y < min_y:
        min_y = y


def sum_of_distances_to_all_stations(stations, x, y):
    distance = 0
    for station_x, station_y in stations:
        distance += abs(x - station_x) + abs(y - station_y)
        if distance > TRESHOLD:
            return distance
    return distance


points_within_treshold = 0

for x in range(max_x - TRESHOLD - 1, min_x + TRESHOLD + 1):
    for y in range(max_y - TRESHOLD - 1, min_y + TRESHOLD + 1):
        if sum_of_distances_to_all_stations(stations, x, y) < TRESHOLD:
            points_within_treshold += 1

print("Total number of points: ", points_within_treshold)