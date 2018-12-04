fname = 'input_sorted.txt'

with open(fname) as f:
    content = f.readlines()
content = [x.strip() for x in content]

# such a shame that python3 doesn't have built-in ordered set (TreeSet from java)

current_guard = None
sleeping = {}
start_sleep = None

for i in range(0, 60):
    sleeping[i] = {}

for line in content:
    splits = line.split(None, 2)
    time = splits[1][:-1]
    activity = splits[2]
    hour, minute = time.split(":")

    if "falls asleep" in activity:
        start_sleep = int(minute)

    if "wakes up" in activity:
        for current_minute in range(start_sleep, int(minute)):
            if current_guard in sleeping[current_minute]:
                sleeping[current_minute][current_guard] += 1
            else:
                sleeping[current_minute][current_guard] = 1

    if "Guard " in activity:
        current_guard = activity.split()[1]

max_minute = -1
max_times_asleep = -1
target_guard_id = ""
for key, value in sleeping.items():
    sleeping[key] = sorted(value.items(), key=lambda kv: kv[1], reverse=True)
    for guard, times_asleep in sleeping[key]:
        if times_asleep > max_times_asleep:
            max_times_asleep = times_asleep
            target_guard_id = guard
            max_minute = key

print(target_guard_id, max_minute)

print("Result: ", int(target_guard_id[1:]) * max_minute)