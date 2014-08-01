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
DG.add_edge("Gate1", 4, weight=1)
DG.add_edge(4,"Gate1", weight=1)
DG.add_edge("Gate2",5, weight=1)
DG.add_edge(5,"Gate2", weight=1)
DG.add_edge("Gate3",6, weight=1)
DG.add_edge(6,"Gate3", weight=1)
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
DG.add_edge("Ranway1",7, weight=1)
DG.add_edge(7,"Ranway1", weight=1)
DG.add_edge("Ranway1",8, weight=1)
DG.add_edge(8,"Ranway1", weight=11)
DG.add_edge("Ranway1",9, weight=1)
DG.add_edge(9,"Ranway1", weight=1)


#pos=nx.spring_layout(DG)
#labels=nx.draw_networkx_labels(DG,pos)
#nx.draw(DG,pos)
#plt.show()


print(nx.shortest_path(DG, source="Gate1",target="Ranway1", weight="weight"))

print(nx.dijkstra_path(DG,  source="Gate1", target="Ranway1"))
#path=nx.all_pairs_dijkstra_path(DG)
#print("dijkstra", path)
#bfstree = nx.bfs_edges(DG, "Ranway1")
#print(list(bfstree))

pathex=conn.bidirectional_shortest_path(DG, "Ranway1", "Gate1", [7])
print(pathex)

T_DG = DG.copy()
T_DG.remove_node(7)
#T_DG.remove_node(8)
#T_DG.remove_node(9)


print(nx.dijkstra_path(T_DG,  source="Gate1", target="Ranway1"))
