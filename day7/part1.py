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


result = []
current_node = root
to_do = set()
while len(unfinished_steps) > 0:
    finished_step = True

    # add dependencies
    for parent in current_node.parents:
        if parent in unfinished_steps:
            to_do.add(parent)
            finished_step = False

    # mark as finished
    if finished_step:
        result.append(current_node.data)
        unfinished_steps.remove(current_node.data)

        # remove as dependency
        for child_node_data in current_node.children:
            nodes[child_node_data].parents.remove(current_node.data)

    unfinished_steps_lex = sorted(unfinished_steps)
    for step in unfinished_steps_lex:
        if len(nodes[step].parents) == 0:
            current_node = nodes[step]
            break

print("".join(result))
