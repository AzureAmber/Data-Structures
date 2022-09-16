class wdigraph:
    # Vertices = Vertices in graph
    # Edges = Connections between Vertices (Table of True and False)
    # Length = Number of vertices in graph
    def __init__(self):
        self.vertices = []
        self.edges = []
        self.length = 0

    # If vertice does not exist: add vertice, increment length, set edges
    # If vertice exist: do nothing
    def add_vertice(self, vertice):
        if (vertice not in self.vertices):
            self.length += 1
            self.vertices.append(vertice)
            for x in self.edges:
                x.append(float("inf"))
            self.edges.append([float("inf")] * self.length)
            self.edges[self.length - 1][self.length - 1] = 0    
                    
    # Helper function for connect, disconnect
    # Sets the connection between two vertices
    def set_connect(self, vertice1, vertice2, value):
        if (vertice1 in self.vertices and vertice2 in self.vertices):
            pos1 = self.vertices.index(vertice1)
            pos2 = self.vertices.index(vertice2)
            self.edges[pos1][pos2] = value
            
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

class queue:
    def __init__(self, data = None):
        self.head = None
        self.tail = self.head
        self.length = 0
    
    def enqueue(self, data):
        if (self.head is None):
            self.head = node(data, self.head)
            self.tail = self.head
        else:
            self.tail.next = node(data, None)
            self.tail = self.tail.next
        self.length += 1
        
    def dequeue(self):
        if (self.length == 0):
            return "Empty"
        else:
            value = self.head.data
            self.head = self.head.next
            self.length -= 1
            return value
    
    def empty(self):
        return self.length == 0



# DFS (Depth First Search)
# Visit every vertice in the graph by going far out for each branch and backtracking (First In, Last Out) -> Stack
# O(n^2) = Each vertex visited where their neighbors need to be found = O(n) * O(n)
def dfs(graph, start):
    # keep track of vertices that were visited
    visited = [None] * graph.length
    # keep track of which vertices to visit next
    to_visit_stack = stack()
    # keep track of where each vertice was visited from
    visited_from_stack = stack()
    
    # start visiting vertices from start vertex
    # start vertex visits itself 
    to_visit_stack.push(start)
    visited_from_stack.push(start)
    
    # if there are vertices to visit, for each such vertice:
    # - if not visited, then visit it, update visit list with where it visited from,
    #   and add vertices it could visit and add where they came from
    # - if visited, then there is no use for where it came from
    while (not to_visit_stack.empty()):
        from_vertex = to_visit_stack.pop()
        vertex_index = graph.get_index(from_vertex)
        if (visited[vertex_index] is None):
            # Insert code to affect vertex here
            visited[vertex_index] = visited_from_stack.pop()
            next_vertices = graph.get_neighbors(from_vertex)
            for v in next_vertices:
                to_visit_stack.push(v)
                visited_from_stack.push(from_vertex)
        else:
            visited_from_stack.pop()
    return visited



# BFS (Breath First Search)
# Visit every vertice in the graph by going for each vertice in a branch first (First in, First Out) -> Queue
# O(n^2) = Each vertex visited where their neighbors need to be found = O(n) * O(n)
def bfs(graph, start):
    # keep track of vertices that were visited
    visited = [None] * graph.length
    # keep track of which vertices to visit next
    to_visit_queue = queue()
    # keep track of where each vertice was visited from
    visited_from_queue = queue()
    
    # start visiting vertices from start vertex
    # start vertex visits itself 
    to_visit_queue.enqueue(start)
    visited_from_queue.enqueue(start)
    
    # if there are vertices to visit, for each such vertice:
    # - if not visited, then visit it, update visit list with where it visited from,
    #   and add vertices it could visit and add where they came from
    # - if visited, then there is no use for where it came from
    while (not to_visit_queue.empty()):
        from_vertex = to_visit_queue.dequeue()
        vertex_index = graph.get_index(from_vertex)
        if (visited[vertex_index] is None):
            # Insert code to affect vertex here
            visited[vertex_index] = visited_from_queue.dequeue()
            next_vertices = graph.get_neighbors(from_vertex)
            for v in next_vertices:
                to_visit_queue.enqueue(v)
                visited_from_queue.enqueue(from_vertex)
        else:
            visited_from_queue.dequeue()
    return visited



x = wdigraph()

x.add_vertice(0)
x.add_vertice(1)
x.add_vertice(2)
x.add_vertice(3)
x.add_vertice(4)
x.add_vertice(5)
x.add_vertice(6)
x.add_vertice(7)

x.connect(0, 1, 0)
x.connect(0, 4, 0)
x.connect(0, 7, 0)
x.connect(1, 2, 0)
x.connect(2, 3, 0)
x.connect(3, 1, 0)
x.connect(4, 5, 0)
x.connect(5, 2, 0)
x.connect(5, 6, 0)
x.connect(5, 7, 0)

print(dfs(x, 0))









































