class Stack:
    # Initialize the stack with a maximum size
    def __init__(self, max_size: int):
        self.max_size: int = max_size  # max_size: Maximum size of the stack
        self._items: list = [None for _ in range(max_size)]  # items: List of items in stack | Starts out full of None
        self._pointer: int = 0  # pointer: Index of the top of the stack

    # Allow the stack to be printed in a formatted way
    def __str__(self) -> str:
        return str(self._items)

    # Print Error Message Then Exit With Code 1
    @staticmethod
    def _fatal(msg: str):
        print(f"Fatal Error: {msg}")
        exit(1)

    # Push an item to the stack
    def push(self, item):
        # If the stack is full then return an error
        if not self.is_full():
            self._items[self._pointer] = item  # Set the item at the pointer to the pushed item
            self._pointer += 1  # Increment the pointer
        else:
            self._fatal(f"cannot add '{item}' as the stack is full")

    # pop an item from the stack
    def pop(self):
        # If the stack is empty then return an error
        if not self.is_empty():
            self._pointer -= 1  # Decrement the pointer
            print(self._items[self._pointer])  # Print the item at the pointer
            self._items[self._pointer] = None  # Set the item at the pointer to None
        else:
            self._fatal("stack is empty")

    # check if the stack is empty
    def is_empty(self) -> bool:
        # If the pointer is at 0 then the stack is empty
        if self._pointer == 0:
            return True
        return False

    # check if the stack is full
    def is_full(self) -> bool:
        # If the pointer is at the max size then the stack is full
        if self._pointer >= self.max_size:
            return True
        return False


class TwoDimensionalList:
    def __init__(self):
        self.items: list = []

    def __getitem__(self, item):
        return self.items[item]

    def __str__(self) -> str:
        print("List: [")
        for i in range(len(self.items)):
            print(f"{self.items[i]}")
        print("]")
        return ""

    def add(self, item):
        self.items.append(item)


if __name__ == "__main__":
    stack = Stack(5)
    stack.pop()
