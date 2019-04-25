import networkx as nx
from itertools import combinations
from functions.bool_functions import *
from matching import *

G = nx.read_edgelist('sample_graphs/sample_G.txt')
nx.draw_networkx(G)

print(is_clique(G))

