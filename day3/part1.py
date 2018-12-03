fname = 'input.txt'

with open(fname) as f:
    content = f.readlines()
content = [x.strip() for x in content]

used_coordinates = {}
for word in content:
    splits = word.split(" ")
    coordinates = splits[2][:-1].split(",")
    lengths = splits[3].split("x")

    # (0,0) is upper left coordinate
    x0 = int(coordinates[0]) + 1
    y0 = int(coordinates[1]) + 1

    lengthX = int(lengths[0])
    lengthY = int(lengths[1])

    for i in range (0,lengthX):
        for j in range (0, lengthY):
            x = x0 + i
            y = y0 + j
            if (x, y) not in used_coordinates:
                used_coordinates[(x, y)] = 1
            else:
                used_coordinates[(x, y)] += 1

total_overlapping_inches = 0
for key, value in used_coordinates.items():
    if used_coordinates[key] > 1:
        total_overlapping_inches += 1

print("Total overlapping inches: " + str(total_overlapping_inches))