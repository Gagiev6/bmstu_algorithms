# Массив01li
class M_Stack:
    def __init__(self):
        self.massive = []

    def push(self, item):
        self.massive.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.massive.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.isEmpty():
            return self.massive[-1]
        else:
            raise IndexError("peek from empty stack")

    def isEmpty(self):
        return len(self.massive) == 0

    def size(self):
        return len(self.massive)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class SV_Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if not self.isEmpty():
            popped_value = self.top.value
            self.top = self.top.next
            self.size -= 1
            return popped_value
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.isEmpty():
            return self.top.value
        else:
            raise IndexError("peek from empty stack")

    def isEmpty(self):
        return self.size == 0

    def getSize(self):
        return self.size
class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0

    def enqueue(self, item):
        if self.size == self.capacity:
            raise IndexError("Queue is full")
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("dequeue from EMPTY ")
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def peek(self):
        if self.isEmpty():
            raise IndexError("peek from empty queue")
        return self.queue[self.front]

    def isEmpty(self):
        return self.size == 0

    def getSize(self):
        return self.size

class SV_Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, item):
        new_node = Node(item)
        if self.isEmpty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("dequeue from empty queue")
        item = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return item

    def peek(self):
        if self.isEmpty():
            raise IndexError("peek from empty queue")
        return self.front.value

    def isEmpty(self):
        return self.size == 0

    def getSize(self):
        return self.size

class Deque:
    def __init__(self, max_size):
        self.max_size = max_size
        self.data = [None] * max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.max_size

    def add_front(self, item):
        if self.is_full():
            raise IndexError("Deque is full")
        self.head = (self.head - 1) % self.max_size
        self.data[self.head] = item
        print(self.data[self.head])
        self.size += 1

    def add_rear(self, item):
        if self.is_full():
            raise IndexError("Deque is full")
        self.data[self.tail] = item
        self.tail = (self.tail + 1) % self.max_size
        self.size += 1

    def remove_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        item = self.data[self.head]
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return item

    def remove_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        self.tail = (self.tail - 1) % self.max_size
        item = self.data[self.tail]
        self.size -= 1
        return item

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.data[self.head]

    def peek_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.data[(self.tail - 1) % self.max_size]

    def GetLen(self):
        return self.size
    def print(self):
        print(self.data)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def add_first(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def add_last(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def remove_first(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        value = self.head.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
        return value

    def remove_last(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        value = self.tail.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        return value

    def peek_first(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.head.value

    def peek_last(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.tail.value

    def __len__(self):
        return self.size

    def __str__(self):
        if self.is_empty():
            return "Deque()"
        current = self.head
        elements = []
        while current:
            elements.append(str(current.value))
            current = current.next
        return "Deque(" + " <-> ".join(elements) + ")"


