from sys import exit  # Import exit from sys module
import colors as c  # Importing colors.py to use colored text


# Python Circular Queue Implementation
class Queue:
    # Initialize the Queue
    def __init__(self, max_size: int):
        self.maxsize: int = max_size  # > max_size: Maximum size of the Queue
        self._items: list[None] = [None for _ in range(max_size)]  # > items: List of items in the Queue
        self._head: int = 0  # > head: Index of the head of the Queue
        self._tail: int = 0  # > tail: Index of the tail of the Queue

    # Allow the queue to be printed in a formatted way
    def __str__(self):
        return_str = ""
        for i in range(len(self._items) - 1):
            return_str += f"{c.cyan}{self._items[i]} {c.purple}-> {c.norm}"
        return return_str + f"{c.cyan}{str(self._items[-1])}{c.norm}"

    # Print Error Message
    @staticmethod
    def _fatal(error: str):
        print(f"{c.red}Error: {c.yellow}{error}{c.norm}")
        exit(1)

    # Check if the Queue is full
    def is_full(self) -> bool:
        return (self._tail + 1 == self._head) or (self._tail == self.maxsize and self._head == 0)

    # Check if the Queue is empty
    def is_empty(self) -> bool:
        return self._head == self._tail

    # Enqueue an item to the Queue
    def enqueue(self, item):
        print(f"tail: {self._tail}, head: {self._head}")
        # If it is full then return an error
        if self.is_full():
            self._fatal("Error queue is full")
        # If the tail is at the end of the list then reset it to 0
        # This allows the queue to be circular
        if self._tail == self.maxsize:
            self._tail = 0
        # Set the item at the tail to the enqueued item and then increment the tail
        self._items[self._tail] = item
        self._tail += 1

    # Dequeue an item from the Queue
    def dequeue(self):
        # If it is empty then return an error
        if self.is_empty():
            self._fatal("Error queue is empty")
        # Get item at the head and then set it to None
        item = self._items[self._head]
        self._items[self._head] = None
        # Increment the head and return the item
        self._head += 1
        print(f"{c.green}Dequeued {c.cyan}{item}{c.green} from the queue{c.norm}")
        return item


if __name__ == "__main__":
    q = Queue(5)
    print(f"{c.green}Queue: {c.norm}{q}")
    q.enqueue(1)
    print(f"{c.green}Queue: {c.norm}{q}")
    q.enqueue(2)
    print(f"{c.green}Queue: {c.norm}{q}")
    q.enqueue(3)
    print(f"{c.green}Queue: {c.norm}{q}")
    q.enqueue(4)
    print(f"{c.green}Queue: {c.norm}{q}")
    q.enqueue(5)
    print(f"{c.green}Queue: {c.norm}{q}")
    q.dequeue()
    print(f"{c.green}Queue: {c.norm}{q}")
    q.enqueue("69")
    print(f"{c.green}Queue: {c.norm}{q}")
