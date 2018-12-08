fname = 'input.txt'

with open(fname) as f:
    content = f.readlines()
content = [x.strip() for x in content]


# parent must be finished before children can begin
class Node(object):
    def __init__(self):
        self.header_children = None
        self.header_metadata = None
        self.children = []
        self.metadata = []


def compute_value(node, values):
    if node in values:
        return values[node]
    sum = 0
    if len(node.children) == 0:
        for data in node.metadata:
            sum += data
    else:
        for child_index in node.metadata:
            if child_index > len(node.children):
                continue

            # no negative indices, hence ==
            if child_index == 0:
                continue

            sum += compute_value(node.children[child_index-1], values)
    values[node] = sum
    return sum


def initialize_tree(root, splits, start_index):
    root.header_children = splits[start_index]
    root.header_metadata = splits[start_index + 1]

    # header children + header metadata
    total_numbers_stored = 2

    current_index = start_index + total_numbers_stored

    for child_i in range(0, root.header_children):
        child_node = Node()
        numbers_stored = initialize_tree(child_node, splits, current_index)
        root.children.append(child_node)

        total_numbers_stored += numbers_stored
        current_index += numbers_stored

    for index in range(0, root.header_metadata):
        root.metadata.append(splits[current_index + index])
        total_numbers_stored += 1

    return total_numbers_stored


splits = [int(x) for x in content[0].split(" ")]
root = Node()
initialize_tree(root, splits, 0)

values = {}
root_value = compute_value(root, values)
print("Root value: ", root_value)