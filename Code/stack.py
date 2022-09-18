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








