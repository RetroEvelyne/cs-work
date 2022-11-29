class Stack:
    def __init__(self, max_size: int):
        self.max_size: int = max_size
        self.items: list = [None for _ in range(max_size)]
        self.pointer: int = 0

    def __str__(self):
        return str(self.items)

    def push(self, item):
        if not self.is_full():
            self.items[self.pointer] = item
            self.pointer += 1
        else:
            print(f"Error, cannot add '{item}' as the stack is full")

    def pop(self):
        if not self.is_empty():
            self.pointer -= 1
            print(self.items[self.pointer])
            self.items[self.pointer] = None
        else:
            print("Error, stack is empty")

    def is_empty(self):
        if self.pointer == 0:
            return True
        return False

    def is_full(self):
        if self.pointer >= self.max_size:
            return True
        return False


class TwoDimensionalList:
    def __init__(self):
        self.items = []

    def __getitem__(self, item):
        return self.items[item]

    def __str__(self):
        print("List: [")
        for i in range(len(self.items)):
            print(f"{self.items[i]}")
        print("]")
        return ""

    def add(self, item):
        self.items.append(item)


if __name__ == "__main__":
    my_list = TwoDimensionalList()
    my_list.add(Stack(5))
    my_list.add(Stack(5))
    my_list[0].push(1)
    my_list[0].push(25)
    my_list[0].push("Hello")
    my_list[1].push(3.14)
    my_list[1].push("World")
    print(my_list)
