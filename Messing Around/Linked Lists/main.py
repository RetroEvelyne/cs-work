from random import choices, randint


class Node:
    def __init__(self, data: str | None):
        self.data = data or None
        self.next = None

    def __str__(self):
        return f"{self.data}"


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            print(f"{count}: {temp.data}")
            temp = temp.next

    def swap_two_taxis(self, first_node, second_node):
        # Find first taxi
        before_first = None
        first = self.head
        while first:
            try:
                if first.data == first_node:
                    break
                before_first = first
                first = first.next
            except AttributeError:
                return
        # Find second taxi
        before_second = None
        second = self.head
        while second:
            try:
                if second.data == second_node:
                    break
                before_second = second
                second = second.next
            except AttributeError:
                return

        try:
            temp = first.next
            first.next = second.next
            second.next = temp
            before_first.next = second
            before_second.next = first
        except AttributeError:
            ...
            # TODO
            # EITHER FIRST OR SECOND IS THE HEAD AND SO IT DOESN'T HAVE A BEFORE


class Car:
    def __init__(self):
        self.plate = self.random_plate()

    @staticmethod
    def random_plate():
        letters = "ABCDEFGHIJKLMNOPRSTUVYZ"
        area_code = "".join(choices(letters, k=2))
        random_letters = "".join(choices(letters, k=3))
        numbers = randint(1, 99)
        return f"{area_code}{numbers:02d}-{random_letters}"


if __name__ == "__main__":
    node_collection = []
    llist = LinkedList()
    llist.head = Node(Car.random_plate())
    for i in range(1, 10):
        node_collection.append(Node(Car.random_plate()))
    llist.head.next = node_collection[0]

    for i in range(len(node_collection)):
        try:
            node_collection[i].next = node_collection[i+1]
        except IndexError:
            node_collection[i] = None

    llist.print_list()

    first_taxi = input(": ")
    second_taxi = input(": ")
    llist.swap_two_taxis(first_taxi, second_taxi)

    llist.print_list()
