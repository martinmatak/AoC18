fname = 'input.txt'

with open(fname) as f:
    content = f.readlines()
content = [x.strip() for x in content]

frequency = 0
for line in content:
    frequency += int(line)

print("Final frequency: " + str(frequency))