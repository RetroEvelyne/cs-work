from random import choices, randint


class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

    def __str__(self):
        return f"{self.data}"


class LinkedList:
    def __init__(self, first_node=None):
        self.head = first_node

    def add_new(self, current=None,):
        print(current)


class Car:
    def __init__(self):
        self.plate = self.random_plate()

    @staticmethod
    def random_plate():
        letters = "ABCDEFGHIJKLMNOPRSTUVYZ"
        area_code = "".join(choices(letters, k=2))
        random_letters = "".join(choices(letters, k=3))
        numbers = randint(1, 100)
        return f"{area_code}{numbers:02d}-{random_letters}"


if __name__ == "__main__":
    node_collection = []
    for i in range(1, 11):
        node_collection.append(Node(Car.random_plate()))

    linked_list = LinkedList(node_collection[0])
    node_collection = node_collection.pop(0)
    for x, node in enumerate(node_collection, start=(-1)):
        LinkedList.add_new(node)

    for i, node in enumerate(node_collection, start=1):
        print(f"{i}: {node}")
