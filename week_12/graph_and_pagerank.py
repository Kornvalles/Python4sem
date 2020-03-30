import networkx as nx
import numpy as np

graph = nx.read_edgelist('twitter_combined.txt')

in_deg_vec = np.array([graph.in_degree(n) for n in graph.nodes()])
print(in_deg_vec)
in_deg_vec.max() # return largest value

print(np.argmax(in_deg_vec))
idx = np.argmax(in_deg_vec) # returns the index of the largest value
print(graph.nodes[idx]['name'])