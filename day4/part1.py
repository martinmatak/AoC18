fname = 'input_sorted.txt'

with open(fname) as f:
    content = f.readlines()
content = [x.strip() for x in content]

# such a shame that python3 doesn't have built-in ordered set (TreeSet from java)

most_sleepy_guard = {}
current_guard = None
sleeping = {}
start_sleep = None
for line in content:
    splits = line.split(None, 2)
    time = splits[1][:-1]
    activity = splits[2]
    hour, minute = time.split(":")

    if "falls asleep" in activity:
        start_sleep = int(minute)

    if "wakes up" in activity:
        for current_minute in range(start_sleep, int(minute)):
            if current_minute in sleeping[current_guard]:
                sleeping[current_guard][current_minute] += 1
            else:
                sleeping[current_guard][current_minute] = 1

            if current_guard in most_sleepy_guard:
                most_sleepy_guard[current_guard] += 1
            else:
                most_sleepy_guard[current_guard] = 1

    if "Guard " in activity:
        current_guard = activity.split()[1]
        if current_guard not in sleeping:
            sleeping[current_guard] = {}

most_sleepy_guard = sorted(most_sleepy_guard.items(), key=lambda kv: kv[1], reverse=True)
target_guard_id = None
for guard_id, minutes in most_sleepy_guard:
    target_guard_id = guard_id
    break
print("Target guard id: ", target_guard_id)

minutes = sorted(sleeping[target_guard_id].items(), key=lambda kv: kv[1], reverse=True)
print(sleeping[target_guard_id])
print(minutes)
target_minute = None
for minute, times_of_sleep in minutes:
    target_minute = minute
    break
print("Target minute: ", target_minute)

print("Result: ", int(target_guard_id[1:]) * target_minute)