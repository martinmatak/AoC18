import numpy as np

fname = 'input.txt'

with open(fname) as f:
    content = f.readlines()
content = [x.strip() for x in content]

def index_of_closest_station(x, y, stations):
    min_distance = None
    index = -1
    for station_x, station_y, station_index in stations:
        distance = abs(x - station_x) + abs(y - station_y)
        if min_distance is None or distance < min_distance:
            min_distance = distance
            index = station_index
        elif distance == min_distance:
            index = -1
    return index

stations = []
station_index = 0
max_x = None
max_y = None
min_x = None
min_y = None
area_covered = {}
for line in content:
    splits = line.split(", ")
    x = int(splits[0])
    y = int(splits[1])
    stations.append((x, y, station_index))
    area_covered[station_index] = 0
    station_index += 1
    if max_x is None or x > max_x:
        max_x = x
    if min_x is None or x < min_x:
        min_x = x
    if max_y is None or y > max_y:
        max_y = y
    if min_y is None or y < min_y:
        min_y = y

coordinates = np.zeros(shape=(max_x, max_y))
for x in range(0, max_x):
    for y in range(0, max_y):
        index = index_of_closest_station(x, y, stations)
        if index != -1:
            area_covered[index] += 1

# remove stations on the edge
for x in range(min_x, max_x):
    index = index_of_closest_station(x, min_y, stations)
    if index in area_covered:
        del area_covered[index]
    index = index_of_closest_station(x, max_y, stations)
    if index in area_covered:
        del area_covered[index]
for y in range(min_y, max_y):
    index = index_of_closest_station(min_x, y, stations)
    if index in area_covered:
        del area_covered[index]
    index = index_of_closest_station(max_x, y, stations)
    if index in area_covered:
        del area_covered[index]

sorted_by_area = sorted(area_covered.items(), key=lambda kv: kv[1], reverse=True)
for key, value in sorted_by_area:
    print(value)
    break