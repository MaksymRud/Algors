from collections import defaultdict

infinit_minus = -1000000

class Node:
    def __init__(self, num, parent = None, distance = 0, color = ''):
        self.num = num
        self.color = color
        self.parent = parent
        self.d = distance

    def __repr__(self):
        if self.parent != None:
            return f"Node {self.num} is {self.color}, has Parent {self.parent.num} and path {self.d}"
        else:
            return f"Node {self.num} is {self.color}, dosn't have parent and has path {self.d}"
        


    
class Graph:
    def __init__(self):
        self._graph = defaultdict(list)
    
    @property
    def graph(self):
        return self._graph
    
    @graph.setter
    def graph(self, graph):
        self._graph = graph

    def addEdge(self, u, v):
        self._graph[u].append(v)

    def BFS(self, s):
        for u in self.graph.keys():
            if u is not s:
                u.color = "white"
                u.d = infinit_minus
                u.parent = None

        queue = []

        queue.append(s)

        while queue:

            u = queue.pop(0)

            print(u.num, end = " ")

            for v in self.graph[u]:
                if v.color == "white":
                    v.color = "grey"
                    v.d = u.d + 1
                    v.parent = u
                    queue.append(v)
        
            u.color = "black"
            
        print()
        
    @staticmethod
    def printPath(s, v):
        if s.num == v.num:
            print(s)
        elif v.parent == None:
            print("There is no path from s to v")
        else:
            Graph.printPath(s, v.parent)
            print(v)


if __name__ == "__main__":
    g = Graph()

    nodes = []

    for i in range(4):
        nodes.append(Node(i))

    g.addEdge(nodes[0], nodes[1])
    g.addEdge(nodes[0], nodes[2])
    g.addEdge(nodes[1], nodes[2])
    g.addEdge(nodes[2], nodes[0])
    g.addEdge(nodes[2], nodes[3])
    g.addEdge(nodes[3], nodes[3])

    g.BFS(nodes[2])

    Graph.printPath(nodes[2], nodes[1])