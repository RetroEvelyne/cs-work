class Node:
    def __init__(self, data):
        self.data = data or None
        self.next = [None]

    def __str__(self):
        return f"{self.data}"


class Tree:
    def __init__(self, root: Node | None):
        self.root = root or None
        self.nodes = [self.root]

    def __str__(self):
        return f"{self.root}"

    def add_node(self, node: Node, parent: Node):
        parent.next.append(node)
        self.nodes.append(node)

    def remove_node(self, node):
        nodes_list = self.nodes
        parent = nodes_list[0]
        while node not in parent.next:
            nodes_list.pop(0)
            parent = nodes_list[0]


if __name__ == "__main__":
    t = Tree(Node("root"))
    t.add_node(Node("child1"), t.root)
    t.add_node(Node("child2"), t.root)
    t.remove_node()

