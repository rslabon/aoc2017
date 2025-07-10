# Bron-Kerbosch algorithm for finding maximal cliques in an undirected graph
class Graph:
    def __init__(self):
        self.graph = dict()

    def add_edge(self, v, u):
        adj = self.graph.get(v, set())
        adj.add(u)
        self.graph[v] = adj

        adj2 = self.graph.get(u, set())
        adj2.add(v)
        self.graph[u] = adj2

    def vertices(self):
        return set(self.graph.keys())

    def adj(self, v):
        return self.graph.get(v, set())

    def __repr__(self):
        return str(self.graph)


def bron_kerbosch(cliques, graph, R, P, X):
    if not P and not X:
        if len(R) > 2:
            cliques.add(tuple(sorted(R)))

    pivot = None
    for v in P | X:
        if not pivot:
            pivot = v
        elif len(graph.adj(v)) > len(graph.adj(pivot)):
            pivot = v

    for v in P - graph.adj(pivot):
        adj = graph.adj(v)
        bron_kerbosch(cliques, graph, R | {v}, P & adj, X & adj)
        P = P - {v}
        X = X | {v}


g = Graph()
g.add_edge("a", "b")
g.add_edge("b", "c")
g.add_edge("a", "c")
g.add_edge("d", "e")
g.add_edge("d", "f")
g.add_edge("f", "e")

print(g)
cliques = set()
bron_kerbosch(cliques, g, set(), g.vertices(), set())
print(cliques)
