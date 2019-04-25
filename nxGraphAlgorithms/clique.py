import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations
from functions.bool_functions import *

def maximum_clique_set(G):
    for i in range (len(S)):
        N = neighbors(G, S[i])
        for j in range(i + 1, len(S)):
            if S[i + 1] not in N:
                return False
    return True

def clique_number(G):
    return len(maximum_clique_set(G))