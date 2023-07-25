#!/usr/bin/env python
# coding: utf-8

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

# load graph, parameters: k=3, n=27, l=9, p_in=0.99, p_out=0.01

node, edge_position, edge_possibility=load_graph('/.../Downloads/Expected_Modularity_Calculation_in_ProbabilisticGraph-main/datasets/3Community9nodes_each0.99within0.01betweenEntr=0.npy')
com=load_com('.../Downloads/Expected_Modularity_Calculation_in_ProbabilisticGraph-main/datasets/3Community9nodes_each0.99within0.01between_clusterEntr=0.npy')

# initialization

S1=[]
S2_dev=[]
S2_mean=[]
for p in np.arange(0,1.1,0.1):
    
    #generate random edge probabilities, entropy ratio of those probabilities is equal to p 
    
    p=np.round(p,1)
    entropy=p*len(edge_position)
    edge_possibility=entropy_(entropy,len(edge_position))
    edge_possibility=edge_possibility[0]
    
    #our method
    
    s1=APWP(edge_position,edge_possibility,com)
    
    #threshold

    S2=[]
    for shre in np.arange(0.1,1.1,0.1):
        s2=threshold(shre, node, edge_position,edge_possibility,Trans_C2(com,node))
        S2.append(s2)

    # collect results
    S1.append(s1.real)
    S2_dev.append(np.std(S2))
    S2_mean.append(np.mean(S2))

# draw

fig, ax = plt.subplots()
x=list(np.arange(0,1.1,0.1))

plt.plot(x,S1,ls='--',marker='x',color='r',linewidth=2,markersize=10,mfc='none',label=r'$APWP^{EMOD}$')
plt.plot(x,S2_mean,'go--',color='b',linewidth=2,markersize=10,mfc='none',label='Threshold method')
plt.errorbar(x,S2_mean, S2_dev, marker='o', mfc='none',
         mec='none', ms=0,ecolor='b',alpha=0.5,elinewidth=6,color='none')

plt.ylabel('Expected modularity')
plt.xlabel('Entropy ratio')
ax.set_xlim(xmin=0)
plt.xticks(np.arange(0,1.1,0.1))
ax.legend(loc='upper right', bbox_to_anchor=(1, 0.9),prop={'size': 8})
plt.savefig('thre.pdf')
plt.show()
