# Single source shorest paths
class wgraph:
    def __init__(self):
        self.vertices = []
        self.edges = []
        self.length = 0

    def add_vertice(self, vertice):
        if (vertice not in self.vertices):
            self.length += 1
            self.vertices.append(vertice)
            for x in self.edges:
                x.append(float("inf"))
            self.edges.append([float("inf")] * self.length)
            self.edges[self.length - 1][self.length - 1] = 0    
    
    def set_connect(self, vertice1, vertice2, value):
        if (vertice1 in self.vertices and vertice2 in self.vertices):
            pos1 = self.vertices.index(vertice1)
            pos2 = self.vertices.index(vertice2)
            self.edges[pos1][pos2] = value
            self.edges[pos2][pos1] = value
            
    def connect(self, vertice1, vertice2, value):
        self.set_connect(vertice1, vertice2, value)
        
    def disconnect(self, vertice1, vertice2):
        self.set_connect(vertice1, vertice2, float("inf"))

    def get_edge(self, vertice1, vertice2):
        if (vertice1 in self.vertices and vertice2 in self.vertices):
            pos1 = self.vertices.index(vertice1)
            pos2 = self.vertices.index(vertice2)
            return self.edges[pos1][pos2]
        else:
            return float("inf")
        
    def has_edge(self, vertice1, vertice2):
        if (self.get_edge(vertice1, vertice2) == float("inf")):
            return False
        else:
            return True
        
    def get_neighbors(self, vertice):
        temp = []
        if (vertice in self.vertices):
            pos = self.vertices.index(vertice)
            for i in range(0, self.length):
                if (i != pos and self.edges[pos][i] != float("inf")):
                    temp.append(self.vertices[i])
        return temp
    
    def get_index(self, vertice):
        if (vertice in self.vertices):
            return self.vertices.index(vertice)
        else:
            return False
        
    def get_vertices(self):
        return self.vertices
    
    def get_edges(self):
        return self.edges
    
    def get_length(self):
        return self.length



class node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class stack:
    def __init__(self, data = None):
        self.head = None
        self.length = 0        
        if (data is not None):
            self.push(data)

    def push(self, data):
        self.head = node(data, self.head)
        self.length += 1
    
    def pop(self):
        if (self.length == 0):
            return "Empty"
        else:
            value = self.head.data
            self.head = self.head.next
            self.length -= 1
            return value
    
    def empty(self):
        return self.length == 0
    
    def get_data(self):
        temp = ""
        curr_data = self.head
        while (curr_data is not None):
            temp = temp + str(curr_data.data) + " -> "
            curr_data = curr_data.next
        temp = temp + "None"
        return temp



# DFS method
def dfs_sssp(graph, start):
    # check if there might be a never ending cycle
    edges = graph.get_edges()
    for vertice_pair in edges:
        for weight in vertice_pair:
            if (weight < 0):
                return False
            
    # distance = track the current shortest distances from each vertex to the start vertex
    # visited = track how each vertex is currently best reached
    # to_visit_stack = track which vertices to visit next
    distance = [float("inf")] * graph.get_length()
    visited = [None] * graph.get_length()
    to_visit_stack = stack()

    # starting vertex is visited by itself so distance is 0
    start_index = graph.get_index(start)
    distance[start_index] = 0
    visited[start_index] = start
    
    # first vertex to visit is the starting vertex
    to_visit_stack.push(start)
    
    # if there are vertices to visit, then for each vertex:
    # - if current shortest distance > current distance = distance from the previous vertex + distance from previous to current,
    #   set current shortest distance = current distance, update where vertex is visited from,
    #   add vertices connected to current vertex to visit which are visited by current vertex 
    # - if not, then do nothing since nothing needs to be updated or visited since current distance is worst than the current shortest distance
    while (not to_visit_stack.empty()):
        cur_vertex = to_visit_stack.pop()
        cur_index = graph.get_index(cur_vertex)
        
        next_vertices = graph.get_neighbors(cur_vertex)
        for v in next_vertices:
            cur_distance = distance[cur_index] + graph.get_edge(cur_vertex, v)
            next_index = graph.get_index(v)
            if (cur_distance < distance[next_index]):
                distance[next_index] = cur_distance
                visited[next_index] = cur_vertex
                to_visit_stack.push(v)
    return visited



class wnode:
    def __init__(self, data = None, value = None, next = None):
        self.data = data
        self.value = value
        self.next = next

# Priority Queue
class priority_queue:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0
    
    # O(n)
    def enqueue(self, data, priority):
        if (self.head is None):
            self.head = wnode(data, priority, self.head)
            self.tail = self.head
        else:
            if (self.tail.value < priority):
                self.tail.next = wnode(data, priority, None)
                self.tail = self.tail.next
            elif (self.head.value >= priority):
                self.head = wnode(data, priority, self.head)
            else:
                curr_data = self.head
                while (curr_data.next.value < priority):
                    curr_data = curr_data.next
                curr_data.next = wnode(data, priority, curr_data.next)
        self.length += 1
        
    # O(1)
    def dequeue(self):
        if (self.length == 0):
            return None
        else:
            value = self.head.data
            self.head = self.head.next
            self.length -= 1
            return value
    
    def empty(self):
        return self.length == 0



# Dijkstra (BFS method) using priority queue
def dijkstra(graph, start):
    # check if there might be a never ending cycle
    edges = graph.get_edges()
    for vertice_pair in edges:
        for weight in vertice_pair:
            if (weight < 0):
                return False
            
    # distance = track the current shortest distances from each vertex to the start vertex
    # visited = track how each vertex is currently best reached
    # to_visit_stack = track which vertices to visit next
    # completed = track which vertices still need to find shortest path
    distance = [float("inf")] * graph.get_length()
    visited = [None] * graph.get_length()
    to_visit = priority_queue()
    completed = [False] * graph.get_length()

    # starting vertex is visited by itself so distance is 0
    start_index = graph.get_index(start)
    distance[start_index] = 0
    visited[start_index] = start
    
    # first vertex to visit is the starting vertex
    to_visit.enqueue(start, 0)
    
    # if there are vertices to visit, then for each vertex:
    # - if current shortest distance > current distance = distance from the previous vertex + distance from previous to current,
    #   set current shortest distance = current distance, update where vertex is visited from,
    #   add vertices connected to current vertex to visit which are visited by current vertex 
    # - if not, then do nothing since nothing needs to be updated or visited since current distance is worst than the current shortest distance
    while (not to_visit.empty()):
        cur_vertex = to_visit.dequeue()
        cur_index = graph.get_index(cur_vertex)
        
        if (not completed[cur_index]):
            completed[cur_index] = True
            next_vertices = graph.get_neighbors(cur_vertex)
            for v in next_vertices:
                cur_distance = distance[cur_index] + graph.get_edge(cur_vertex, v)
                next_index = graph.get_index(v)
                if (cur_distance < distance[next_index]):
                    distance[next_index] = cur_distance
                    visited[next_index] = cur_vertex
                    priority = graph.get_edge(cur_vertex, v)
                    to_visit.enqueue(v, priority)
    return visited



# Binary Heap
class bin_heap:
    def __init__(self):
        self.size = 32
        self.length = 0
        self.keys = [None] * self.size
        self.values = [float("inf")] * self.size

    # O(log n) = Switch up to at most log(n) rows
    def insert(self, key, value: int):
        if (self.length == 0):
            self.keys[0] = key
            self.values[0] = value            
        else:
            cur_index = self.length
            parent_index = (cur_index - 1) // 2
            self.keys[cur_index] = key
            self.values[cur_index] = value
            while (parent_index >= 0 and value < self.values[parent_index]):
                self.values[cur_index] = self.values[parent_index]
                self.keys[cur_index] = self.keys[parent_index]
                self.values[parent_index] = value
                self.keys[parent_index] = key
                cur_index = parent_index
                parent_index = (cur_index - 1) // 2
        self.length += 1
        self.check_grow()

    # O(log n) = Switch down to at most log(n) rows
    def remove(self):
        if (self.length == 0):
            return None
        else:
            key = self.keys[0]
            cur_value = self.values[self.length - 1]
            cur_key = self.keys[self.length - 1]
            self.values[self.length - 1] = float("inf")
            self.keys[self.length - 1] = float("inf")
            cur_index = 0
            self.values[cur_index] = cur_value
            self.keys[cur_index] = cur_key
            left = 2 * cur_index + 1
            right = 2 * cur_index + 2
            while (left < self.size):
                if (cur_value > self.values[left] and cur_value > self.values[right]):
                    if (self.values[left] <= self.values[right]):
                        self.values[cur_index] = self.values[left]
                        self.keys[cur_index] = self.keys[left]
                        self.values[left] = cur_value
                        self.keys[left] = cur_key
                        cur_index = left
                    else:
                        self.values[cur_index] = self.values[right]
                        self.keys[cur_index] = self.keys[right]
                        self.values[right] = cur_value
                        self.keys[right] = cur_key
                        cur_index = right
                elif (cur_value > self.values[left]):
                    self.values[cur_index] = self.values[left]
                    self.keys[cur_index] = self.keys[left]
                    self.values[left] = cur_value
                    self.keys[left] = cur_key
                    cur_index = left
                elif (cur_value > self.values[right]):
                    self.values[cur_index] = self.values[right]
                    self.keys[cur_index] = self.keys[right]
                    self.values[right] = cur_value
                    self.keys[right] = cur_key
                    cur_index = right
                else:
                    break
                left = 2 * cur_index + 1
                right = 2 * cur_index + 2
            self.length -= 1
            return key
    
    def check_grow(self):
        if (self.length == self.size):
            self.keys = self.keys + [None] * self.size
            self.values = self.values + [float("inf")] * self.size
            self.size *= 2
            
    def get_keys(self):
        return self.keys
    
    def get_values(self):
        return self.values

    def empty(self):
        return (self.length == 0)


# Dijkstra (BFS method) using binary heap
def dijkstra_heap(graph, start):
    # check if there might be a never ending cycle
    edges = graph.get_edges()
    for vertice_pair in edges:
        for weight in vertice_pair:
            if (weight < 0):
                return False
            
    # distance = track the current shortest distances from each vertex to the start vertex
    # visited = track how each vertex is currently best reached
    # to_visit_stack = track which vertices to visit next
    # completed = track which vertices still need to find shortest path
    distance = [float("inf")] * graph.get_length()
    visited = [None] * graph.get_length()
    to_visit = bin_heap()
    completed = [False] * graph.get_length()

    # starting vertex is visited by itself so distance is 0
    start_index = graph.get_index(start)
    distance[start_index] = 0
    visited[start_index] = start
    
    # first vertex to visit is the starting vertex
    to_visit.insert(start, 0)
    
    # if there are vertices to visit, then for each vertex:
    # - if current shortest distance > current distance = distance from the previous vertex + distance from previous to current,
    #   set current shortest distance = current distance, update where vertex is visited from,
    #   add vertices connected to current vertex to visit which are visited by current vertex 
    # - if not, then do nothing since nothing needs to be updated or visited since current distance is worst than the current shortest distance
    while (not to_visit.empty()):
        cur_vertex = to_visit.remove()
        cur_index = graph.get_index(cur_vertex)
        
        if (not completed[cur_index]):
            completed[cur_index] = True
            next_vertices = graph.get_neighbors(cur_vertex)
            for v in next_vertices:
                cur_distance = distance[cur_index] + graph.get_edge(cur_vertex, v)
                next_index = graph.get_index(v)
                if (cur_distance < distance[next_index]):
                    distance[next_index] = cur_distance
                    visited[next_index] = cur_vertex
                    priority = graph.get_edge(cur_vertex, v)
                    to_visit.insert(v, priority)
    return visited







# Test Case 1 ----------------------------------------------------------

x = wgraph()

x.add_vertice("A")
x.add_vertice("B")
x.add_vertice("C")
x.add_vertice("D")
x.add_vertice("E")
x.connect("A", "B", 5)
x.connect("A", "D", 1)
x.connect("B", "D", 3)
x.connect("B", "E", 10)
x.connect("B", "C", 4)
x.connect("C", "E", 2)

# ['A', 'D', 'B', 'A', 'C']
#print(dfs_sssp(x, "A"))
#print(dijkstra(x, "A"))
#print(dijkstra_heap(x, "A"))

# Test Case 2 ----------------------------------------------------------

x = wgraph()

x.add_vertice("A")
x.add_vertice("B")
x.add_vertice("C")
x.add_vertice("D")
x.add_vertice("E")
x.add_vertice("F")
x.connect("A", "B", 1)
x.connect("B", "C", 1)
x.connect("C", "D", 1)
x.connect("D", "E", -9)
x.connect("E", "C", 1)

# Cycle Exist: False
#print(dfs_sssp(x, "A"))
#print(dijkstra(x, "A"))
#print(dijkstra_heap(x, "A"))

# Test Case 3 ----------------------------------------------------------

x = wgraph()

x.add_vertice("A")
x.add_vertice("B")
x.add_vertice("C")
x.add_vertice("D")
x.add_vertice("E")
x.add_vertice("F")
x.connect("A", "B", 7)
x.connect("A", "F", 9)
x.connect("A", "E", 14)
x.connect("E", "F", 2)
x.connect("F", "B", 10)
x.connect("E", "D", 9)
x.connect("F", "C", 11)
x.connect("B", "C", 15)
x.connect("D", "C", 6)

# ['A', 'A', 'F', 'E', 'F', 'A']
#print(dfs_sssp(x, "A"))
#print(dijkstra(x, "A"))
#print(dijkstra_heap(x, "A"))

# Test Case 4 ----------------------------------------------------------

x = wgraph()

x.add_vertice("A")
x.add_vertice("B")
x.add_vertice("C")
x.add_vertice("D")
x.add_vertice("E")
x.add_vertice("F")
x.add_vertice("G")
x.add_vertice("H")
x.add_vertice("I")
x.add_vertice("J")
x.connect("A", "B", 2)
x.connect("A", "C", 7)
x.connect("A", "D", 5)
x.connect("B", "E", 1)
x.connect("B", "F", 9)
x.connect("C", "F", 3)
x.connect("C", "G", 5)
x.connect("C", "H", 1)
x.connect("D", "H", 3)
x.connect("D", "G", 11)
x.connect("E", "H", 15)
x.connect("E", "I", 7)
x.connect("E", "J", 17)
x.connect("G", "I", 1)
x.connect("H", "I", 2)

# ['A', 'A', 'A', 'A', 'B', 'C', 'I', 'D', 'H/E', 'E']
print(dfs_sssp(x, "A"))
print(dijkstra(x, "A"))
print(dijkstra_heap(x, "A"))










