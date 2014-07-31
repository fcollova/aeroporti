# -*- coding: cp1252 -*-
#Copyright (c) 2014, f.c.
#
#Authors: Francesco Collovà
#
#


import networkx as nx
import matplotlib.pyplot as plt
import connectivity_approx as conn

#---------------F.C. Create Graph

DG=nx.DiGraph()
DG.add_edge(1, 4, weight=1)
DG.add_edge(4,1, weight=1)
DG.add_edge(2,5, weight=1)
DG.add_edge(5,2, weight=1)
DG.add_edge(3,6, weight=1)
DG.add_edge(6,3, weight=1)
DG.add_edge(4,5, weight=2)
DG.add_edge(5,4, weight=2)
DG.add_edge(4,7, weight=1)
DG.add_edge(7,4, weight=1)
DG.add_edge(5,8, weight=1)
DG.add_edge(8,5, weight=1)
DG.add_edge(5,6, weight=2)
DG.add_edge(6,5, weight=2)
DG.add_edge(6,9, weight=1)
DG.add_edge(9,6, weight=1)
DG.add_edge(7,8, weight=2)
DG.add_edge(8,7, weight=2)
DG.add_edge(9,8, weight=2)
DG.add_edge(8,9, weight=2)
DG.add_edge(10,7, weight=1)
DG.add_edge(7,10, weight=1)
DG.add_edge(10,8, weight=1)
DG.add_edge(8,10, weight=1)
DG.add_edge(10,9, weight=1)
DG.add_edge(9,10, weight=1)


#nx.draw(DG)
#plt.show()
#print(nx.shortest_path(DG, source=3,target=10, weight="weight"))

print(nx.dijkstra_path(DG,  source=1, target=10))
path=nx.all_pairs_dijkstra_path(DG)
print(path)
bfstree = nx.bfs_edges(DG, 10)
print(list(bfstree))

pathex=conn.bidirectional_shortest_path(DG, 10, 1, [4])
print(pathex)
