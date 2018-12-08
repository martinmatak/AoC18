fname = 'input.txt'

with open(fname) as f:
    content = f.readlines()
content = [x.strip() for x in content]


# parent must be finished before children can begin
class Node(object):
    def __init__(self):
        self.children = set()
        self.parents = set()
        self.data = None


nodes = {}
unfinished_steps = set()
for i in range(ord('A'), ord('Z') + 1):
    nodes[chr(i)] = None
    unfinished_steps.add(chr(i))

root = None
for line in content:
    splits = line.split(" ")
    data = splits[1]
    child = splits[7]

    node_parent = None
    if nodes[data] is None:
        node_parent = Node()
        node_parent.data = data
        nodes[data] = node_parent
    else:
        node_parent = nodes[data]
    node_parent.children.add(child)

    node_child = None
    if nodes[child] is None:
        node_child = Node()
        node_child.data = child
        nodes[child] = node_child
    else:
        node_child = nodes[child]
    node_child.parents.add(data)

    # assumption: first line is root of the tree
    if root is None:
        root = node_parent

# remove unused letters:
for i in range(ord('A'), ord('Z') + 1):
    letter = chr(i)
    if nodes[letter] is None:
        del nodes[letter]
        unfinished_steps.remove(letter)

# time needed
time_per_letter = {}
for letter in unfinished_steps:
    time_per_letter[letter] = 60 + ord(letter) - ord('A') + 1

workers = {}
available_steps = set()
current_second = 0
while len(unfinished_steps) > 0:

    for step_letter in unfinished_steps:
        if len(nodes[step_letter].parents) == 0 and step_letter not in workers:
            available_steps.add(step_letter)

    for step in sorted(available_steps):
        if len(workers) == 5:
            break
        else:
            workers[step] = time_per_letter[step]

    min_time = min(workers.values())
    finished_workers_ids = []
    for worker_id in workers.keys():

        # not available anymore
        if worker_id in available_steps:
            available_steps.remove(worker_id)

        workers[worker_id] -= min_time

        if workers[worker_id] == 0:
            finished_workers_ids.append(worker_id)

    for finished_workers_id in finished_workers_ids:
        # done with job
        workers.pop(finished_workers_id)

        # remove dependency
        for child in nodes[finished_workers_id].children:
            nodes[child].parents.remove(finished_workers_id)
        unfinished_steps.remove(finished_workers_id)

    current_second += min_time

print("Current second: ", current_second)