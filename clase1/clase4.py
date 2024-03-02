class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            return None
        popped_node = self.head
        self.head = self.head.next
        popped_node.next = None
        return popped_node.data

    def peek(self):
        if self.is_empty():
            return None
        return self.head.data

    def display(self):
        current = self.head
        while current:
            print(current.data, end='->')
            current = current.next
        print()

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

stack = Stack()

stack.push(7)
stack.push(10)
stack.push(13)

stack.display()  # Imprime: 13->10->7->

print("Elemento superior de la pila:", stack.pop())  # Imprime: Elemento superior de la pila: 13

stack.display()  # Imprime: 10->7->

print("Elemento superior de la pila:", stack.peek())  # Imprime: Elemento superior de la pila: 10

stack.display()  # Imprime: 10->7->

print("¿La pila está vacía?", stack.is_empty())  # Imprime: ¿La pila está vacía? False

print("Tamaño de la pila:", stack.size())  # Imprime: Tamaño de la pila: 2
