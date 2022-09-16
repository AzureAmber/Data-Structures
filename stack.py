# Asymptotic complexity
# Stack: First in, last out
class node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class stack:
    def __init__(self):
        self.head = None
        self.length = 0

    # O(1)
    def push(self, data):
        self.head = node(data, self.head)
        self.length += 1
    
    # O(1)
    def pop(self):
        if (self.length == 0):
            return "Empty"
        else:
            value = self.head.data
            self.head = self.head.next
            self.length -= 1
            return value
    
    # O(1)
    def empty(self):
        return self.length == 0


x = stack()



# Queue: First in, first out
class queue:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0
    
    # O(1)
    def enqueue(self, data):
        if (self.head is None):
            self.head = node(data, self.head)
            self.tail = self.head
        else:
            self.tail.next = node(data, None)
            self.tail = self.tail.next
        self.length += 1
        
    # O(1)
    def dequeue(self):
        if (self.length == 0):
            return "Empty"
        else:
            value = self.head.data
            self.head = self.head.next
            self.length -= 1
            return value
    
    # O(1)
    def empty(self):
        return self.length == 0
    
x = queue()








# -----------------------------
# Binary search tree
class bst:
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None
    
    def insert(self, value: int):
        if (self.value is None):
            self.value = value
        else:
            if (value < self.value):
                if (self.left is None):
                    self.left = bst()
                self.left.insert(value)
            elif (value > self.value):
                if (self.right is None):
                    self.right = bst()
                self.right.insert(value)

    def find(self, value: int):
        if (self.value is None):
            return False
        else:
            if (value < self.value):
                if (self.left is None):
                    return False
                else:
                    return self.left.find(value)
            elif (value > self.value):
                if (self.right is None):
                    return False
                else:
                    return self.right.find(value)
            else:
                return True

    def get_value(self):
        return self.value
    
    def print_tree(self):
        print(self.value)
        if (self.left is not None):
            self.left.print_tree()
        if (self.right is not None):
            self.right.print_tree()
        

x = bst()

x.insert(43)
x.insert(10)
x.insert(90)
x.insert(17)








