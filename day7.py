import re

lines = """
pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
""".strip().splitlines()

with open("./resources/day7.txt") as f:
    lines = f.read().strip().splitlines()


class Node(object):

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.children = set()
        self.parent = None
        self.total_weight = None

    def add_node(self, node):
        self.children.add(node)
        node.parent = self

    def __repr__(self):
        return f"{self.name} total_weight={self.total_weight}"

    def compute_total_weight(self):
        for child in self.children:
            child.compute_total_weight()

        self.total_weight = self.weight + sum(child.total_weight for child in self.children)


def get_nodes():
    nodes = dict()

    for line in lines:
        name, weight = re.findall(r"(\w+)\s+\((\d+)\).*", line)[0]
        nodes[name] = Node(name, int(weight))

    for line in lines:
        if "->" in line:
            left, right = line.split(" -> ")
            name, weight = re.findall(r"(\w+)\s+\((\d+)\)", left)[0]
            others = right.split(",")
            for other in others:
                nodes[name].add_node(nodes[other.strip()])

    return nodes


def get_root(node):
    current = node
    while current.parent:
        current = current.parent
    return current


def depth(node):
    current = node
    c = 0
    while current.parent:
        current = current.parent
        c += 1
    return c


def find_common_root(nodes):
    for node in nodes.values():
        if len(node.children) > 0:
            return get_root(node)

    raise Exception("No common root")


def find_wrong_weights_with_depth(node):
    weights = dict()
    for other in node.children:
        w = weights.get(other.total_weight, [])
        w.append(other)
        weights[other.total_weight] = w

    result = []

    if len(weights.keys()) > 1:
        items = weights.items()
        items = sorted(items, key=lambda x: len(x[1]))
        out_of_balance_node = items[0][1][0]
        any_balanced_node = items[1][1][0]
        difference = any_balanced_node.total_weight - out_of_balance_node.total_weight
        result.append((depth(out_of_balance_node), out_of_balance_node.weight + difference))

    for other in node.children:
        result += find_wrong_weights_with_depth(other)

    return result


def part1():
    print(find_common_root(get_nodes()).name)


def part2():
    nodes = get_nodes()
    root = find_common_root(nodes)
    root.compute_total_weight()
    wrong_weights_with_depth = find_wrong_weights_with_depth(root)
    wrong_weights_with_depth = sorted(wrong_weights_with_depth, key=lambda x: x[0], reverse=True)
    print(wrong_weights_with_depth[0][1])


part1()
part2()
