fname = 'input.txt'

with open(fname) as f:
    content = f.readlines()
content = [x.strip() for x in content]

hit_frequencies = set()
current_frequency = 0

hit_frequencies.add(current_frequency)

frequency_reached_twice = False
while not frequency_reached_twice:
    for line in content:
        current_frequency += int(line)
        if current_frequency in hit_frequencies:
            print("First reaches " + str(current_frequency) + " twice")
            frequency_reached_twice = True
            break
        else:
            hit_frequencies.add(current_frequency)
