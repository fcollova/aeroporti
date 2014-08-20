# -*- coding: cp1252 -*-
#Copyright (c) 2014, f.c.
#
#Authors: Francesco Collovà
#
#


import networkx as nx
from networkx.readwrite import json_graph

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


data_json = json_graph.node_link_data(DG)
print data_json
