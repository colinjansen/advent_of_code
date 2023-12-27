import networkx as nx

G = nx.Graph()

with open("_input/day25.txt", encoding='utf8') as f:
    for line in f.read().splitlines():
        left, right = line.split(': ')
        for node in right.strip().split():
            G.add_edge(left, node)
            G.add_edge(node, left)
edges_to_cut = nx.minimum_edge_cut(G)
G.remove_edges_from(edges_to_cut)
a, b = nx.connected_components(G)
print(len(a) * len(b))