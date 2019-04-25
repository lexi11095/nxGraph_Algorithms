import networkx as nx
from functions.local_properties import degree


def V(G):
    return list(nx.nodes(G))

def n(G):
    return len(V(G))

def E(G):
    return list(nx.edges(G))

def m(G):
    return len(E(G))
    
def degree_sequence(G):
    D = [degree(G, v) for v in V(G)]
    D.sort(reverse = True)
    return D

def maximum_degree(G):
    return degree_sequence(G)[0]

def minimum_degree(G):
    return degree_sequence(G)[-1]

def avg_degree(G):
    return sum(degree(G, v) for v in V(G)/n(G))

def radius(G):
    return minimum_degree(G)

def diameter(G):
    return maximum_degree(G)
