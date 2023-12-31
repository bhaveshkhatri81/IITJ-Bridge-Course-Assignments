class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append((u, v, w))

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_mst(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e += 1
                result.append((u, v, w))
                self.union(parent, rank, x, y)

        return result

    def update_mst(self, u, v, w):
        for i, (x, y, _) in enumerate(self.graph):
            if (u == x and v == y) or (u == y and v == x):
                if w < self.graph[i][2]:
                    self.graph[i] = (u, v, w)
                    self.rebuild_mst()
                return

        self.graph.append((u, v, w))
        self.rebuild_mst()

    def rebuild_mst(self):
        mst_edges = self.kruskal_mst()
        self.graph = mst_edges


V = 4
graph = Graph(V)
graph.add_edge(0, 1, 10)
graph.add_edge(0, 2, 6)
graph.add_edge(0, 3, 5)
graph.add_edge(1, 3, 15)
graph.add_edge(2, 3, 4)

u = 1
v = 2
w = 8

graph.update_mst(u, v, w)
print("Updated MST:")
print(graph.kruskal_mst())
