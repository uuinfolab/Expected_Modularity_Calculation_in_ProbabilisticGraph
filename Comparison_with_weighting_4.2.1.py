#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import random

# ------------------------------------
from Classic_Sampling import classic_sampling
from Brute_Force import brute_force
from Algorithms import APWP,PWP, Trans_C1,Trans_C2
from Probabilities import PB,DFT
from Network_Generator import rand_graph, rand_graph_com,entropy_
from Communities import Random_Community,SizeVariance_Commuinity
from Threshold import threshold
from Save_Load import save_graph,load_graph,save_com,load_com


# load graph and communities

node, edge_position, edge_possibility=load_graph('/.../Downloads/Expected_Modularity_Calculation_in_ProbabilisticGraph-main/datasets/3Community9nodes_each0.99within0.01betweenEntr=0.npy')
com=load_com('/.../Downloads/Expected_Modularity_Calculation_in_ProbabilisticGraph-main/datasets/3Community9nodes_each0.99within0.01between_clusterEntr=0.npy')


S1=[]
S2=[]
for p in np.arange(0.1,1.1,0.1):
    
    #evenly assign same edge possibilities
    
    edge_possibility=[p for x in range(len(edge_position))]


    #probabilistic graph calculation
    
    s1=APWP(edge_position,edge_possibility,com)

    #construct weighted g
    
    edge_weight=[]
    for i in range(len(edge_position)):
        edge_weight.append((edge_position[i][0],edge_position[i][1],p))
        
    G=nx.Graph()
    G.add_weighted_edges_from(edge_weight)

    # weighted graph calculation
   
    s2=nx.community.modularity(G,com, weight='weight')
    
    # collect results
    
    S1.append(s1.real)
    S2.append(s2)
    


# In[13]:


# draw

fig, ax = plt.subplots()
x=list(np.arange(0.1,1.1,0.1))
plt.plot(x,S1,'go--',color='r',linewidth=2,markersize=10,mfc='none',label='probabilistic graphs')
plt.plot(x,S2,'go--',color='b',linewidth=2,markersize=10,mfc='none',label='weighted deterministic graphs')
plt.ylabel('Expected modularity')
plt.xlabel('Edge probability')
ax.set_xlim(xmin=0)
xx=np.arange(0.10,1.10,0.10)
ll = ['%.2f' % a for a in xx]
plt.xticks(xx, ll)
plt.legend()
plt.savefig('weighted.pdf')
plt.show()

