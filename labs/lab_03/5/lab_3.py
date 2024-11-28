class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_by_value(self, value):
        if not self.head:
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        current_node = self.head
        while current_node.next and current_node.next.data != value:
            current_node = current_node.next

        if current_node.next:
            current_node.next = current_node.next.next

    def insert_after_value(self, value, new_data):
        new_node = Node(new_data)
        current_node = self.head
        while current_node and current_node.data != value:
            current_node = current_node.next

        if current_node:
            new_node.next = current_node.next
            current_node.next = new_node

    def search(self, value):
        current_node = self.head
        while current_node:
            if current_node.data == value:
                return True
            current_node = current_node.next
        return False

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    def reverse(self):
        def print_list(head):
            current = head
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")

        prev_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
            print_list(prev_node)
        self.head = prev_node

    def sort(self):
        if not self.head or not self.head.next:
            return

        sorted_head = self.head
        unsorted_head = self.head.next
        sorted_head.next = None

        while unsorted_head:
            current = unsorted_head
            unsorted_head = unsorted_head.next
            if current.data < sorted_head.data:
                current.next = sorted_head
                sorted_head = current
            else:
                search_node = sorted_head
                while search_node.next and search_node.next.data < current.data:
                    search_node = search_node.next
                current.next = search_node.next
                search_node.next = current
        self.head = sorted_head


    def keep_last_occurrences(self):
        if not self.head:
            return

        last_occurrences = {}
        current_node = self.head

        while current_node:
            last_occurrences[current_node.data] = current_node
            current_node = current_node.next

        new_head = None
        for key in sorted(last_occurrences.keys()):
            if not new_head:
                new_head = last_occurrences[key]
                current_node = new_head
            else:
                current_node.next = last_occurrences[key]
                current_node = current_node.next
        current_node.next = None

        self.head = new_head
ll = LinkedList()
print("Проверяем метод, который добавляет элементы:")
ll.append(1)
ll.append(2)
ll.append(3)
ll.print_list()

print("Проверяем метод, который добавляет элемент в начало списка:")
ll.prepend(0)
ll.print_list()

print("Проверяем метод, который удаляет элементы:")
ll.delete_by_value(2)
ll.print_list()

print("Проверяем метод, который добавляет элемент после другого элемента:")
ll.insert_after_value(1, 1.5)
ll.print_list()

print("Проверяем метод, который добавляет элемент перед другим элементом:")
ll.insert_after_value(1.5, 1.25)
ll.print_list()

print("Проверяем метод, который переворачивает список:")
ll.reverse()
ll.print_list()

print("Проверяем метод, который сортирует элементы:")
ll.sort()
ll.print_list()


print("Проверяем метод, который удаляет дубликаты:")
L1 = LinkedList()
L1.append(1)
L1.append(2)
L1.append(3)
L1.append(3)
L1.keep_last_occurrences()
L1.print_list()

