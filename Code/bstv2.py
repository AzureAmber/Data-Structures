# Self Balancing Binary Search Tree (AVL trees)
class node:
    def __init__(self, value = None, height = 1, up_left = None, up_right = None, down_left = None, down_right = None):
        self.value = value
        self.height = height
        self.up_left = up_left
        self.up_right = up_right
        self.down_left = down_left
        self.down_right = down_right
        
    def get_balance(self):
        if (self.down_left is not None and self.down_right is not None):
            return self.down_right.height - self.down_left.height
        elif (self.down_left is None and self.down_right is not None):
            return self.down_right.height
        elif (self.down_left is not None and self.down_right is None):
            return -1 * self.down_left.height
        else:
            return 0
        
    def insert(self, value: int):
        if (self.value is None):
            self.value = value
        else:
            if (value < self.value):
                if (self.down_left is None):
                    self.down_left = node(value, up_right = self)
                else:
                    self.down_left.insert(value)
                self.updateheight()
            elif (value > self.value):
                if (self.down_right is None):
                    self.down_right = node(value, up_left = self)
                else:
                    self.down_right.insert(value)
                self.updateheight()
                
    def remove(self, value: int):
        if (self.value is not None):
            if (value < self.value):
                if (self.down_left is not None):
                    self.down_left.remove(value)
                    self.updateheight()
            elif (value > self.value):
                if (self.down_right is not None):
                    self.down_right.remove(value)
                    self.updateheight()
            else:
                if (self.down_left is None and self.down_right is None):
                    if (self.up_left is None and self.up_right is None):
                        self.value = None
                    elif (self.up_left is None):
                        self.up_right.down_left = None
                    else:
                        self.up_left.down_right = None
                elif (self.down_right is not None):
                    if (self.down_right.down_left is None):
                        self.value = self.down_right.value
                        self.down_right = self.down_right.down_right
                    else:
                        cur_node = self.down_right
                        while (cur_node.down_left is not None):
                            cur_node = cur_node.down_left
                        self.value = cur_node.value
                        cur_node.up_right.down_left = cur_node.down_right
                        while (cur_node.up_right is not None):
                            cur_node = cur_node.up_right
                            cur_node.updateheight()
                else:
                    if (self.down_left.down_right is None):
                        self.value = self.down_left.value
                        self.down_left = self.down_left.down_left
                    else:
                        cur_node = self.down_left
                        while (cur_node.down_right is not None):
                            cur_node = cur_node.down_right
                        self.value = cur_node.value
                        cur_node.up_left.down_right = cur_node.down_left
                        while (cur_node.up_left is not None):
                            cur_node = cur_node.up_left
                            cur_node.updateheight()
                self.updateheight()

    def updateheight(self):
        if (self.down_left is not None and self.down_right is not None):
            self.height = max(self.down_right.height, self.down_left.height) + 1
        elif (self.down_left is None and self.down_right is not None):
            self.height = self.down_right.height + 1
        elif (self.down_left is not None and self.down_right is None):
            self.height = self.down_left.height + 1
        else:
            self.height = 1
        if (self.get_balance() == 2):
            if (self.down_right.get_balance() == 1 or self.down_right.get_balance() == 0):
                self.rotate_left()
            elif (self.down_right.get_balance() == -1):
                self.down_right.rotate_right()
        elif (self.get_balance() == -2):
            if (self.down_left.get_balance() == -1 or self.down_left.get_balance() == 0):
                self.rotate_right()
            elif (self.down_left.get_balance() == 1):
                self.down_left.rotate_left()
            
    def rotate_right(self):
        if (self.up_left is None and self.up_right is None):
            self.up_left = self.down_left
            self.down_left = self.up_left.down_right
            self.up_left.up_right = None
            self.up_left.down_right = self
            if (self.down_left is not None):
                self.down_left.up_right = self
                self.down_left.up_left = None
        elif (self.up_left is not None):
            self.up_left.down_right = self.down_left
            self.down_left.up_left = self.up_left
            self.up_left = self.down_left
            self.down_left = self.up_left.down_right
            self.up_left.up_right = None
            self.up_left.down_right = self
            if (self.down_left is not None):
                self.down_left.up_right = self
                self.down_left.up_left = None
        else:
            self.up_right.down_left = self.down_left
            self.down_left.up_right = self.up_right
            self.up_right = None
            self.up_left = self.down_left
            self.down_left = self.up_left.down_right
            self.up_left.down_right = self
            if (self.down_left is not None):
                self.down_left.up_right = self
                self.down_left.up_left = None
        cur_node = self
        while (cur_node is not None):
            cur_node.updateheight()
            if (cur_node.up_left is not None):
                cur_node = cur_node.up_left
            elif (cur_node.up_right is not None):
                cur_node = cur_node.up_right
            else:
                break
    
    def rotate_left(self):
        if (self.up_left is None and self.up_right is None):
            self.up_right = self.down_right
            self.down_right = self.up_right.down_left
            self.up_right.up_left = None
            self.up_right.down_left = self
            if (self.down_right is not None):
                self.down_right.up_left = self
                self.down_right.up_right = None
        elif (self.up_left is not None):
            self.up_left.down_right = self.down_right
            self.down_right.up_left = self.up_left
            self.up_left = None
            self.up_right = self.down_right
            self.down_right = self.up_right.down_left
            self.up_right.down_left = self
            if (self.down_right is not None):
                self.down_right.up_left = self
                self.down_right.up_right = None
        else:
            self.up_right.down_left = self.down_right
            self.down_right.up_right = self.up_right
            self.up_right = self.down_right
            self.down_right = self.up_right.down_left
            self.up_right.up_left = None
            self.up_right.down_left = self
            if (self.down_right is not None):
                self.down_right.up_left = self
                self.down_right.up_right = None
        cur_node = self
        while (cur_node is not None):
            cur_node.updateheight()
            if (cur_node.up_left is not None):
                cur_node = cur_node.up_left
            elif (cur_node.up_right is not None):
                cur_node = cur_node.up_right
            else:
                break
            
    def print_tree(self):
        print("Value: " + str(self.value) + "\t Height: " + str(self.height))
        if (self.down_left is not None):
            self.down_left.print_tree()
        if (self.down_right is not None):
            self.down_right.print_tree()



class avl:
    def __init__(self):
        self.data = node()
        
    def insert(self, value: int):
        self.data.insert(value)
        self.checktop()
        
    def remove(self, value: int):
        self.data.remove(value)
        self.checktop()
        
    def print_tree(self):
        self.data.print_tree()
        
    def checktop(self):
        if (self.data.up_left is not None):
            self.data = self.data.up_left
        elif (self.data.up_right is not None):
            self.data = self.data.up_right

x = avl()




