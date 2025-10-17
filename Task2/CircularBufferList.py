class CircularBufferList:
    __slots__ = {"capacity", "buffer", "head", "tail", "size"}

    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_full(self) -> bool:
        return self.size == self.capacity

    def is_empty(self) -> bool:
        return self.size == 0

    def push(self, value):
        if (self.is_full()):
            raise OverflowError("Buffer is full")
        self.buffer[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def take(self):
        if (self.is_empty()):
            raise IndexError("Buffer is empty")
        value = self.buffer[self.head]
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return value

    def __len__(self):
        return self.size
