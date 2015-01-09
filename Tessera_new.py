# -*- coding: cp1252 -*-
#Copyright (c) 2014, f.c.
#
#Authors: Francesco Collovà
#
#
try:
    import matplotlib.pyplot as plt
except:
    raise 
import numpy
import networkx as nx
import matplotlib.pyplot as plt
import connectivity_approx as conn

#---------------F.C. Create Graph

filename= "Tessera_new.graphml"
net = nx.read_graphml(filename)
DG = net




#fh=open("test.edgelist",'wb')
#nx.write_edgelist(DG, fh)

#with open(filename) as f:
#    H = nx.read_adjlist(f, delimiter=";" , create_using=nx.DiGraph())
#dt=[('weight',int)]
#adj_mat = numpy.loadtxt(filename,delimiter=";")
#net = nx.from_numpy_matrix(adj_mat, create_using=nx.DiGraph())


pos=nx.graphviz_layout(DG,prog='twopi',args="")
plt.figure(figsize=(15,15))



#Calcola le labels da stampare prese dal campo label del nodo
labels = {}    
for node in DG.nodes():
        #set the node name as the key and the label as its value 
        labels[node]=DG.node[node]['label']
print labels




nx.draw(DG,pos,node_size=20,alpha=0.5,node_color="blue" , with_labels=False)
labels=nx.draw_networkx_labels(DG,pos, labels=labels, font_size=9, font_color='r')


plt.axis('equal')
plt.savefig('circular_tree.png')
#plt.show()


##
##pos1=nx.spring_layout(DG)
##nx.draw(DG,pos1,node_size=20,alpha=0.5,node_color="blue" , with_labels=False)
#labels=nx.draw_networkx_labels(DG,pos1, labels=labels, font_sixe=9)

##plt.axis('equal')
##plt.show()


path=nx.all_simple_paths(DG, source="1", target="20", cutoff=None)

# print sum(1 for x in path)

i=0
for x in path:
    i=i+1
    print(i)
    print x



# for x in DG.nodes():
#     for y in DG.nodes():
#         if x<>y:
#             try:
#                 path=nx.all_simple_paths(DG, source="1", target="100", cutoff=None)
#                 #path=nx.shortest_path(DG, source=x, target=y, weight=None)
#                 print list(path)
#             except nx.NetworkXNoPath:
#                 print 'No path', x, y

