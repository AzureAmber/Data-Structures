# mst (minimum spanning trees)
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
            while (left < self.size and right < self.size):
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



# Union-find: Disjoint set ADT (Quick-find version)
class union_find_qf:
    def __init__(self, length):
        self.elements = list(range(0, length))
        self.length = length
        
    # O(1)
    def get_parent(self, value):
        return self.elements[value]
    
    # O(1)
    def is_same_set(self, value1, value2):
        return self.get_parent(value1) == self.get_parent(value2)
    
    # O(n)
    def union(self, value1, value2):
        convert_from = self.get_parent(value1)
        convert_to = self.get_parent(value2)
        if (convert_from != convert_to):
            for value in range(0, self.length):
                if (self.get_parent(value) == convert_from):
                    self.elements[value] = convert_to

    # O(1)                    
    def get_set(self):
        return self.elements



def kruskal_qf(graph: wgraph):
    # graph to be returned of minimum spanning graph
    min_graph = wgraph()
    graph_vertices = graph.get_vertices()
    for vertex in graph_vertices:
        min_graph.add_vertice(vertex)
    # components of the graph that are connected and how
    components = union_find_qf(graph.get_length())
    # edges that could be added to minimum spanning graph from least to greatest
    edges_to_check = bin_heap()
    graph_edges = graph.get_edges()
    for vertex_from_index in range(0, graph.get_length()):
        for vertex_to_index in range(0, graph.get_length()):
            if (graph_edges[vertex_from_index][vertex_to_index] < float("inf") and vertex_from_index != vertex_to_index):
                edges_to_check.insert([vertex_from_index, vertex_to_index], graph_edges[vertex_from_index][vertex_to_index])
    
    while (not edges_to_check.empty()):
        cur_edge = edges_to_check.remove()
        if (not components.is_same_set(cur_edge[0], cur_edge[1])):
            components.union(cur_edge[0], cur_edge[1])
            min_graph.connect(graph_vertices[cur_edge[0]], graph_vertices[cur_edge[1]], graph_edges[cur_edge[0]][cur_edge[1]])
    
    return min_graph



# Union-find: (Weighted Quick-Union version)
class union_find_wqu:
    def __init__(self, length: int):
        self.elements = list(range(0, length))
        self.weights = [1] * length
        self.length = length

    # O(log n)        
    def get_parent(self, value):
        cur_parent = self.elements[value]
        while (self.elements[cur_parent] != cur_parent):
            cur_parent = self.elements[cur_parent]
        return cur_parent

    # O(log n)
    def is_same_set(self, value1, value2):
        return self.get_parent(value1) == self.get_parent(value2)
    
    # O(log n)
    def union(self, value1, value2):
        root1 = self.get_parent(value1)
        root2 = self.get_parent(value2)
        if (root1 != root2):
            if (self.weights[root1] <= self.weights[root2]):
                self.elements[root1] = root2
                self.weights[root2] += self.weights[root1]
            else:
                self.elements[root2] = root1
                self.weights[root1] += self.weights[root2]

    def get_set(self):
        return self.elements
    
    def get_weights(self):
        return self.weights



def kruskal_wqu(graph: wgraph):
    # graph to be returned of minimum spanning graph
    min_graph = wgraph()
    graph_vertices = graph.get_vertices()
    for vertex in graph_vertices:
        min_graph.add_vertice(vertex)
    # components of the graph that are connected and how
    components = union_find_wqu(graph.get_length())
    # edges that could be added to minimum spanning graph from least to greatest
    edges_to_check = bin_heap()
    graph_edges = graph.get_edges()
    for vertex_from_index in range(0, graph.get_length()):
        for vertex_to_index in range(0, graph.get_length()):
            if (graph_edges[vertex_from_index][vertex_to_index] < float("inf") and vertex_from_index != vertex_to_index):
                edges_to_check.insert([vertex_from_index, vertex_to_index], graph_edges[vertex_from_index][vertex_to_index])
    
    while (not edges_to_check.empty()):
        cur_edge = edges_to_check.remove()
        if (not components.is_same_set(cur_edge[0], cur_edge[1])):
            components.union(cur_edge[0], cur_edge[1])
            min_graph.connect(graph_vertices[cur_edge[0]], graph_vertices[cur_edge[1]], graph_edges[cur_edge[0]][cur_edge[1]])
    
    return min_graph



# Union-find: (Weighted Quick-Union version) + Path Compression
class union_find_wqupc:
    def __init__(self, length: int):
        self.elements = list(range(0, length))
        self.weights = [1] * length
        self.length = length

    # O(log n)        
    def get_parent(self, value):
        prev_value = value
        cur_value = self.elements[prev_value]
        elements_passed_through = []
        cur_weight_total = 0
        while (self.elements[cur_value] != cur_value):
            elements_passed_through.append(prev_value)
            cur_weight_total += self.weights[prev_value]
            self.weights[cur_value] -= cur_weight_total
            prev_value = cur_value
            cur_value = self.elements[cur_value]
        for element in elements_passed_through:
            self.elements[element] = cur_value
        return cur_value

    # O(log n)
    def is_same_set(self, value1, value2):
        return self.get_parent(value1) == self.get_parent(value2)
    
    # O(log n)
    def union(self, value1, value2):
        root1 = self.get_parent(value1)
        root2 = self.get_parent(value2)
        if (root1 != root2):
            if (self.weights[root1] <= self.weights[root2]):
                self.elements[root1] = root2
                self.weights[root2] += self.weights[root1]
            else:
                self.elements[root2] = root1
                self.weights[root1] += self.weights[root2]

    def get_set(self):
        return self.elements
    
    def get_weights(self):
        return self.weights



def kruskal_wqupc(graph: wgraph):
    # graph to be returned of minimum spanning graph
    min_graph = wgraph()
    graph_vertices = graph.get_vertices()
    for vertex in graph_vertices:
        min_graph.add_vertice(vertex)
    # components of the graph that are connected and how
    components = union_find_wqupc(graph.get_length())
    # edges that could be added to minimum spanning graph from least to greatest
    edges_to_check = bin_heap()
    graph_edges = graph.get_edges()
    for vertex_from_index in range(0, graph.get_length()):
        for vertex_to_index in range(0, graph.get_length()):
            if (graph_edges[vertex_from_index][vertex_to_index] < float("inf") and vertex_from_index != vertex_to_index):
                edges_to_check.insert([vertex_from_index, vertex_to_index], graph_edges[vertex_from_index][vertex_to_index])
    
    while (not edges_to_check.empty()):
        cur_edge = edges_to_check.remove()
        if (not components.is_same_set(cur_edge[0], cur_edge[1])):
            components.union(cur_edge[0], cur_edge[1])
            min_graph.connect(graph_vertices[cur_edge[0]], graph_vertices[cur_edge[1]], graph_edges[cur_edge[0]][cur_edge[1]])
    
    return min_graph









# Test case ----------------------------------
import time

x = wgraph()

x.add_vertice("A")
x.add_vertice("B")
x.add_vertice("C")
x.add_vertice("D")
x.add_vertice("E")
x.add_vertice("F")
x.connect("A", "E", 7)
x.connect("E", "D", 2)
x.connect("A", "B", 2)
x.connect("A", "F", 1)
x.connect("F", "D", 8)
x.connect("B", "F", 3)
x.connect("F", "C", 1)
x.connect("C", "D", 5)
x.connect("B", "C", 3)

min_graph = kruskal_qf(x)
min_graph2 = kruskal_wqu(x)
min_graph3 = kruskal_wqupc(x)





