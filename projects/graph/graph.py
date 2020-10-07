"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    # """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else: 
            raise IndexError("nonexistant vertex")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create empty queue
        q =  Queue()
        # add starting vertex id
        q.enqueue(starting_vertex)
        # create set for visited 
        visited = set()
        # while queue not
        while q.size() > 0:
            v =  q.dequeue()
            if v not in visited:
                print(v)
                visited.add(v)
                for n in self.get_neighbors(v):
                    q.enqueue(n)
    
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s =  Stack()
        # add starting vertex id
        s.push(starting_vertex)
        # create set for visited 
        visited = set()
        # while queue not
        while s.size() > 0:
            v =  s.pop()
            if v not in visited:
                print(v)
                visited.add(v)
                for n in self.get_neighbors(v):
                    s.push(n)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        visited.add(starting_vertex)
        print(starting_vertex)
        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create empty queue
        q =  Queue()
        # add starting vertex id
        q.enqueue([starting_vertex])
        # create set for visited 
        visited = set()
        # while queue not
        while q.size() > 0:
            v =  q.dequeue()
            if v[-1] not in visited:
                # print(v)
                visited.add(v[-1])
                for n in self.get_neighbors(v[-1]):
                    new_path = v + [n]
                    if new_path[-1] == destination_vertex:
                        return new_path
                    q.enqueue(new_path)

            
        
        

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        path = []
        s =  Stack()
        # add starting vertex id
        s.push(starting_vertex)
        # create set for visited 
        visited = set()
        # while queue not
        while s.size() > 0:
            v =  s.pop()
            if v not in visited:
                # print(v)
                visited.add(v)
                path.append(v)
                for n in self.get_neighbors(v):
                    s.push(n)
                    if v == destination_vertex:
                        return path
                

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if path is None:
            path = []
        visited.add(starting_vertex)
        path = path + [starting_vertex]
        # path = list(path)
        # path.append(starting_vertex)
        if starting_vertex == destination_vertex:
            return path
        for n in self.get_neighbors(starting_vertex):
            if n not in visited:
                new_path = self.dfs_recursive(n, destination_vertex, visited, path)
                if new_path is not None:
                    return new_path
        
        

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print("Breadth First Traversal")
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("breadth first search")
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("depth first search")
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))