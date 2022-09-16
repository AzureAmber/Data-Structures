# Set ADTs
# - Vector
# - Sorted Vector
# - Linked List


# Vector
# Linear search: Loop through list, check each element

x = [30, 10, 40, 20]

x.pop()
x.append(50)

40 in x
x.index(40)
len(x)

sorted(x)
sorted(x, reverse = True)

# Sorted Vector
# Invariant: Must be sort for binary search


 
# Linked List (Single)
# Insertion: Add node
# Membership: Linear search
class node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class linkedlist:
    def __init__(self, data = None):
        self.__head = None
        self.__tail = self.__head
        self.__length = 0
        
        if (data is not None):
            self.push_front(data)
        
    def push_front(self, data):
        if (self.__head is None):
            self.__head = node(data, None)
            self.__tail = self.__head
        else:
            self.__head = node(data, self.__head)
        self.__length += 1

    def get_front(self):
        if (self.__head is None):
            return None
        else:
            return self.__head.data
        
    def get_back(self):
        if (self.__tail is None):
            return None
        else:
            return self.__tail.data
        
    def get_list(self):
        if (self.__length == 0):
            return "Empty List"
        else:
            temp = "List of length " + str(self.__length) + ":\n" + str(self.__head.data)
            cur_index = 1
            cur = self.__head.next
            
            while (cur_index < self.__length):
                temp = temp + ", " + str(cur.data)
                cur = cur.next
                cur_index += 1
            return temp

    def find_nth(self, index):
        if (index >= self.__length):
            return "List is length " + str(self.__length) + ". Index " + str(index) + " is too large."
        else:
            cur_index = 0
            cur = self.__head
            
            while (cur_index < index):
                cur = cur.next
                cur_index += 1
            return cur
    
    def get_nth(self, index):
        if (index >= self.__length):
            return "List is length " + str(self.__length) + ". Index " + str(index) + " is too large."
        else:
            return self.find_nth(index).data
    
    def set_nth(self, index, data):
        if (index >= self.__length):
            return "List is length " + str(self.__length) + ". Index " + str(index) + " is too large."
        else:
            self.find_nth(index).data = data
        
# To check class, use type(x). To check specific class, isinstance(x, linkedlist)
x = linkedlist()






