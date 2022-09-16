# Linked Link (Double)
class node:
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
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
            self.__head = node(data, None, None)
            self.__tail = self.__head
        else:
            self.__head.next = node(data, self.__head, None)
            self.__head = self.__head.next
        self.__length += 1
        
    def push_back(self, data):
        if (self.__head is None):
            self.__head = node(data, None, None)
            self.__tail = self.__head
        else:
            self.__tail.prev = node(data, None, self.__tail)
            self.__tail = self.__tail.prev
        self.__length += 1
        
    def pop_front(self):
        if (self.__length == 0):
            print("List is length 0. Nothing to remove")
        elif (self.__length == 1):
            self.__head = None
            self.__tail = None
            self.__length -= 1
        else:
            self.__head = self.__head.prev
            self.__head.next = None
            self.__length -= 1
            
    def pop_back(self):
        if (self.__length == 0):
            print("List is length 0. Nothing to remove")
        elif (self.__length == 1):
            self.__head = None
            self.__tail = None
            self.__length -= 1
        else:
            self.__tail = self.__tail.next
            self.__head.prev = None
            self.__length -= 1

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
            heading = "List of length " + str(self.__length) + ":\n"
            temp = str(self.__tail.data)
            cur_index = 1
            cur = self.__tail.next
            
            while (cur_index < self.__length):
                temp = temp + ", " + str(cur.data)
                cur = cur.next
                cur_index += 1
            return heading + temp
            
x = linkedlist(5)
