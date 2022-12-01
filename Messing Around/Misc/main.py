class Queue:
    def __init__(self, max_size: int):
        self.maxsize: int = max_size; self._items: list[None] = [None for _ in range(max_size)]; self._head: int = 0; self._tail: int = 0
    def __str__(self): return str(self._items)
    def is_full(self) -> bool: return (self._tail + 1 == self._head) or (self._tail == self.maxsize and self._head == 0)
    def is_empty(self) -> bool: return self._head == self._tail
    def enqueue(self, item):
        if self.is_full(): print("Error queue is full")
        if self._tail == self.maxsize: self._tail = 0; self._items[self._tail] = item; self._tail += 1
    def dequeue(self) -> tuple:
        if self.is_empty(): print("Error queue is empty"); item = self._items[self._head]; self._items[self._head] = None; self._head += 1; return item, f"Dequeued {item} from the queue"


if __name__ == "__main__":
    q: Queue = Queue(5)
    print(f"Queue: {q}")
    q.enqueue(1)
    print(f"Queue: {q}")







