# Binary search tree
class node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class bst:
    def __init__(self):
        self.data = None
    
    def insert(self, value: int):
        if (self.data is None):
            self.data = node(value, None, None)
        else:
            cur_node = self.data
            while (cur_node.value != value):
                if (value < cur_node.value):
                    if (cur_node.left is not None):
                        cur_node = cur_node.left
                    else:
                        break
                else:
                    if (cur_node.right is not None):
                        cur_node = cur_node.right
                    else:
                        break
            if (value < cur_node.value):
                cur_node.left = node(value, None, None)
            elif (value > cur_node.value):
                cur_node.right = node(value, None, None)
            
    def search(self, value: int):
        cur_node = self.data
        while (cur_node is not None):
            if (value < cur_node.value):
                cur_node = cur_node.left
            elif (value > cur_node.value):
                cur_node = cur_node.right
            else:
                return True
        return False
    
    def delete(self, value: int):
        prev_node = self.data
        cur_node = prev_node
        while (cur_node is not None):
            if (value < cur_node.value):
                prev_node = cur_node
                cur_node = cur_node.left
            elif (value > cur_node.value):
                prev_node = cur_node
                cur_node = cur_node.right
            else:
                break
        if (cur_node is not None):
            if (prev_node.value == cur_node.value):
                if (cur_node.right is None and cur_node.left is None):
                    self.data = None
                elif (cur_node.right is not None):
                    new_prev_node = cur_node
                    cur_node = cur_node.right
                    if (cur_node.left is None):
                        new_prev_node.value = cur_node.value
                        new_prev_node.right = cur_node.right
                    else:                                        
                        while (cur_node.left is not None):
                            new_prev_node = cur_node
                            cur_node = cur_node.left
                        prev_node.value = cur_node.value
                        new_prev_node.left = None
                else:
                    new_prev_node = cur_node
                    cur_node = cur_node.left
                    if (cur_node.right is None):
                        new_prev_node.value = cur_node.value
                        new_prev_node.left = cur_node.left
                    else:                                        
                        while (cur_node.right is not None):
                            new_prev_node = cur_node
                            cur_node = cur_node.right
                        prev_node.value = cur_node.value
                        new_prev_node.right = None
            elif (cur_node.left is None and cur_node.right is None):
                if (prev_node.left.value == value):
                    prev_node.left = None
                else:
                    prev_node.right = None
            elif (cur_node.right is not None):
                new_prev_node = cur_node
                cur_node = cur_node.right
                if (cur_node.left is None):
                    new_prev_node.value = cur_node.value
                    new_prev_node.right = cur_node.right
                else:                                        
                    while (cur_node.left is not None):
                        new_prev_node = cur_node
                        cur_node = cur_node.left
                    if (prev_node.left.value == value):
                        prev_node.left.value = cur_node.value
                    else:
                        prev_node.right.value = cur_node.value
                    new_prev_node.left = None
            else:
                new_prev_node = cur_node
                cur_node = cur_node.left
                if (cur_node.right is None):
                    new_prev_node.value = cur_node.value
                    new_prev_node.left = cur_node.left
                else:                                        
                    while (cur_node.right is not None):
                        new_prev_node = cur_node
                        cur_node = cur_node.right
                    if (prev_node.left.value == value):
                        prev_node.left.value = cur_node.value
                    else:
                        prev_node.right.value = cur_node.value
                    new_prev_node.right = None

    def get_data(self):
        return self.data

    def print_data(self, cur_node: node):
        if (cur_node is not None):
            print(cur_node.value)
            self.print_data(cur_node.left)
            self.print_data(cur_node.right)




x = bst()
