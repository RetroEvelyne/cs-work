class Colors:
    red = "\033[91m"
    green = "\033[92m"
    yellow = "\033[93m"
    blue = "\033[94m"
    purple = "\033[95m"
    cyan = "\033[96m"
    norm = "\033[0m"


# Python Circular Queue Implementation
class Queue:
    # Initialize the Queue
    def __init__(self, max_size: int):
        self.maxsize: int = max_size  # > max_size: Maximum size of the Queue
        self._items: list[None] = [None for _ in range(max_size)]  # > items: List of items in the Queue
        self._head: int = 0  # > head: Index of the head of the Queue
        self._tail: int = 0  # > tail: Index of the tail of the Queue

    # Allow the queue to be printed in a formatted way
    def __str__(self) -> str:
        return_str = ""
        for i in range(len(self._items) - 1):
            return_str += f"{Colors.cyan}{self._items[i]} {Colors.purple}-> {Colors.norm}"
        return return_str + f"{Colors.cyan}{str(self._items[-1])}{Colors.norm}"

    # Print Error Message Then Exit With Code 1
    @staticmethod
    def _fatal(error: str):
        print(f"{Colors.red}Error: {Colors.yellow}{error}{Colors.norm}")
        exit(1)

    # Check if the Queue is full
    def is_full(self) -> bool:
        # See if the tail and head are neighbors & See if the tail is at the end and the head is at the start
        return (self._tail + 1 == self._head) or (self._tail == self.maxsize and self._head == 0)

    # Check if the Queue is empty
    def is_empty(self) -> bool:
        return self._head == self._tail

    # Enqueue an item to the Queue
    def enqueue(self, item):
        # If it is full then return an error
        if self.is_full():
            self._fatal("Queue is full")
        # If the tail is at the end of the list then reset it to 0
        # This allows the queue to be circular
        if self._tail == self.maxsize:
            self._tail = 0
        # Set the item at the tail to the enqueued item and then increment the tail
        self._items[self._tail] = item
        self._tail += 1

    # Dequeue an item from the Queue
    def dequeue(self) -> tuple:
        # If it is empty then return an error
        if self.is_empty():
            self._fatal("Queue is empty")
        # Get item at the head and then set it to None
        item = self._items[self._head]
        self._items[self._head] = None
        # Increment the head and return the item
        self._head += 1
        return item, f"{Colors.green}Dequeued {Colors.cyan}{item}{Colors.green} from the queue{Colors.norm}"


# Python Basic Stack Implementation
class Stack:
    # Initialize the stack with a maximum size
    def __init__(self, max_size: int, default: str = None):
        self._default: str = default  # default: Default value of the empty stack
        self.max_size: int = max_size  # max_size: Maximum size of the stack
        self._items: list = [self._default for _ in range(self.max_size)]  # items: List of items in stack
        self._pointer: int = 0  # pointer: Index of the top of the stack

    # Allow the stack to be printed in a formatted way
    def __str__(self) -> str:
        return_str = ""
        for item in range(len(self._items) - 1):
            return_str += f"{Colors.cyan}{self._items[item]} {Colors.purple} |  {Colors.norm}"
        return return_str + f"{Colors.cyan}{str(self._items[-1])}{Colors.norm}"

    # Print Error Message Then Exit With Code 1
    @staticmethod
    def _fatal(error: str):
        print(f"{Colors.red}Error: {Colors.yellow}{error}{Colors.norm}")
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
            self._items[self._pointer] = self._default  # Set the item at the pointer to the empty value
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
