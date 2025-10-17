class Node:
    __slots__ = ('value', 'next', 'prev')

    def __init__(self, value):
        self.value = value
        self.next: Node = None
        self.prev: Node = None


class CircularBufferLinkedArray:
    __slots__ = ('capacity', 'head', 'tail', 'size')

    def __init__(self, capacity):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self) -> bool:
        return self.size == 0

    def is_full(self) -> bool:
        return self.size == self.capacity

    def push(self, item):
        if (self.is_full()):
            raise OverflowError("Buffer is full")

        new_node = Node(item)
        if (self.is_empty()):
            self.head = self.tail = new_node
            new_node.next = new_node.prev = new_node
        else:
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail.next = new_node
            self.head.prev = new_node
            self.tail = new_node
        self.size += 1

    def take(self):
        if (self.is_empty()):
            raise IndexError("Buffer is empty")

        value = self.head.value
        if (self.size == 1):
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head
        self.size -= 1
        return value

    def __len__(self):
        return self.size
