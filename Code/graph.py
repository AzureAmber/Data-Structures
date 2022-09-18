# Graph
class graph:
    # Vertices = Vertices in graph
    # Edges = Connections between Vertices (Table of True and False)
    # Length = Number of vertices in graph
    def __init__(self):
        self.vertices = []
        self.edges = []
        self.length = 0

    # If vertice does not exist: add vertice, increment length, set edges
    # If vertice exist: do nothing
    # O(n) = Set default value for each new connection between new vertice and old vertice
    def add_vertice(self, vertice):
        if (vertice not in self.vertices):
            self.length += 1
            self.vertices.append(vertice)
            for x in self.edges:
                x.append(False)
            self.edges.append([False] * self.length)
            self.edges[self.length - 1][self.length - 1] = True    
                    
    # Helper function for connect, disconnect
    # Sets the connection between two vertices
    # O(n) = Find the indices of the two vertices
    def set_connect(self, vertice1, vertice2, value):
        if (vertice1 in self.vertices and vertice2 in self.vertices):
            pos1 = self.vertices.index(vertice1)
            pos2 = self.vertices.index(vertice2)
            self.edges[pos1][pos2] = value
            self.edges[pos2][pos1] = value
            
    def connect(self, vertice1, vertice2):
        self.set_connect(vertice1, vertice2, True)
        
    def disconnect(self, vertice1, vertice2):
        self.set_connect(vertice1, vertice2, False)
        
    # Checks if there is a connection between two vertices
    # O(n) = Find the indices of the two vertices
    def has_edge(self, vertice1, vertice2):
        if (vertice1 in self.vertices and vertice2 in self.vertices):
            pos1 = self.vertices.index(vertice1)
            pos2 = self.vertices.index(vertice2)
            return self.edges[pos1][pos2] 
        else:
            return False
        
    # Returns the vertices connected with given vertice
    # O(n) = Find the index of vertice, then increment through each connection
    def get_neighbors(self, vertice):
        temp = []
        if (vertice in self.vertices):
            pos = self.vertices.index(vertice)
            for i in range(0, self.length):
                if (i != pos and self.edges[pos][i]):
                    temp.append(self.vertices[i])
        return temp

    # Prints the graph (aka the edges)
    # O(n^2) = For each vertice, print its connection with other vertices
    def get_graph(self):
        print("***")
        for col in range(0, self.length):
            temp = ""
            for row in range(0, self.length):
                temp = temp + str(self.edges[row][col]) + " "
            print(temp)
        print("***")



# Digraph (Directed Graph = Graph where edges have a direction)
# Same as a graph, but when adding a connection, only one direction is set to True
class digraph:
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
                x.append(False)
            self.edges.append([False] * self.length)
            self.edges[self.length - 1][self.length - 1] = True    
                    
    # Helper function for connect, disconnect
    # Sets the connection between two vertices
    def set_connect(self, vertice1, vertice2, value):
        if (vertice1 in self.vertices and vertice2 in self.vertices):
            pos1 = self.vertices.index(vertice1)
            pos2 = self.vertices.index(vertice2)
            self.edges[pos1][pos2] = value
            
    def connect(self, vertice1, vertice2):
        self.set_connect(vertice1, vertice2, True)
        
    def disconnect(self, vertice1, vertice2):
        self.set_connect(vertice1, vertice2, False)
        
    def has_edge(self, vertice1, vertice2):
        if (vertice1 in self.vertices and vertice2 in self.vertices):
            pos1 = self.vertices.index(vertice1)
            pos2 = self.vertices.index(vertice2)
            return self.edges[pos1][pos2] 
        else:
            return False
        
    def get_neighbors(self, vertice):
        temp = []
        if (vertice in self.vertices):
            pos = self.vertices.index(vertice)
            for i in range(0, self.length):
                if (i != pos and self.edges[pos][i]):
                    temp.append(self.vertices[i])
        return temp

    # Prints the graph (aka the edges)
    def get_graph(self):
        print("***")
        for col in range(0, self.length):
            temp = ""
            for row in range(0, self.length):
                temp = temp + str(self.edges[row][col]) + " "
            print(temp)
        print("***")
        
# Weighted Digraph (Graph where edges have a direction and a weight)
# Same as a digraph, but connections has values to represent their weights instead of True
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

    # Prints the graph (aka the edges)
    def get_graph(self):
        print("***")
        for col in range(0, self.length):
            temp = ""
            for row in range(0, self.length):
                temp = temp + str(self.edges[row][col]) + " "
            print(temp)
        print("***")




