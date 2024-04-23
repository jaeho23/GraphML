import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
V = {'Dublin', 'Paris', 'Milan', 'Rome'}
E = [('Milan', 'Dublin'), ('Milan', 'Paris'), ('Paris', 'Dublin'), ('Milan', 'Rome')]

G.add_nodes_from(V)
G.add_edges_from(E)

print(f"V = {G.nodes}")
print(f"E = {G.edges}")

# print(f"Graph Order: {G.number_of_nodes()}")
# print(f"Graph Size: {G.number_of_edges()}")
# print(f"Degree for nodes: { {v: G.degree(v) for v in G.nodes} }")
# print(f"Neighbors for nodes: { {v: list(G.neighbors(v)) for v in G.nodes} }")

ego_graph_milan = nx.ego_graph(G, "Milan")
# print(f"Nodes: {ego_graph_milan.nodes}")
# print(f"Nodes: {ego_graph_milan.edges}")

new_nodes = {'London', 'Madrid'}
new_edges = [('London', 'Rome'), ('Madrid', 'Paris')]
G.add_nodes_from(new_nodes)
G.add_edges_from(new_edges)

print(f"V = {G.nodes}")
print(f"E = {G.edges}")

node_remove = {'London', 'Madrid'}
G.remove_nodes_from(node_remove)
print(f"V = {G.nodes}")
print(f"E = {G.edges}")