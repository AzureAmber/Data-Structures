# Graph
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
    
    
    
# DFS (Depth First Search)
# Visit every vertice in the graph by going far out for each branch and backtracking (First In, Last Out) -> Stack
# O(n^2) = Each vertex visited where their neighbors need to be found = O(n) * O(n) 
def dfs_visit(graph):
    # list to track vertices that have been visited by which vertex
    visited = [None] * graph.length 
    # if not visited, then visit, update visited list, and go to next vertices
    def go_next(cur_vertex, from_vertex):
        vertex_index = graph.get_index(cur_vertex)
        if (visited[vertex_index] is None):
            # Current vertice visited
            visited[vertex_index] = from_vertex
            # INSERT CODE PERFORM IN VERTICE HERE
            # Find next vertices to go through
            next_vertices = graph.get_neighbors(cur_vertex)
            for x in next_vertices:
                go_next(x, cur_vertex)
    for v in graph.get_vertices():
        go_next(v, v)
    # return list of how vertices were visited
    return visited
    


# DFS for cycle detection
def dfs_cycle(graph):
    # list to track vertices thaat have been visited
    visited = [False] * graph.length
    # list to track if vertices search for cycle is done
    finished = [False] * graph.length
    # if not vertice isn't finished checking, then go to next vertices. For each of these next vertices:
    # - if not visited yet, visit it, update visited list, and go to the next vertices connected to it
    # - if already visited, then a cycle is found
    # If vertex is finished checking, then no cycle is detected
    def go_next(cur_vertex):
        vertex_index = graph.get_index(cur_vertex)
        if (not finished[vertex_index]):
            if (not visited[vertex_index]):
                visited[vertex_index] = True
                next_vertices = graph.get_neighbors(cur_vertex)
                for x in next_vertices:
                    if (go_next(x)):
                        return True
                finished[vertex_index] = True
            else:
                return True
        else:
            return False
    # Warning:
    # - the return True from go_next() DOESN'T STOP dfs_cycle(), must call return True here as well
    # - the return True if visited in go_next() only stops the CURRENT go_next() iteration,
    #   must call return True if go_next() is True
    for v in graph.get_vertices():
        if (go_next(v)):
            return True
    return False



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

print(dfs_visit(x))