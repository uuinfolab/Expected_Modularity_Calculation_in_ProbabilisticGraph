#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import random
import time

# ------------------------------------
from Classic_Sampling import classic_sampling
from Brute_Force import brute_force
from Algorithms import APWP,PWP, Trans_C1,Trans_C2
from Probabilities import PB,DFT
from Network_Generator import rand_graph, rand_graph_com,entropy_
from Communities import Random_Community,SizeVariance_Commuinity
from Threshold import threshold
from Save_Load import save_graph,load_graph,save_com,load_com

# load graph

node, edge_position, edge_possibility=load_graph('graph.npy')
com=load_com('cluster.npy')

# Exp of number of communities

# number of communities from 2 to 26

re=[]

for N_cluster in range(2,26):
    S_t=0
    
    # repeat 3 times
    
    for j in range(3):
        com=Random_Community(N_cluster,node)
        c=Trans_C1(com)
        
        # calculate APWP
        
        start1=time.time()
        s1=APWP(edge_position,edge_possibility,c)
        end1=time.time()
        S_t+=end1-start1
    S_t/=3
    
    # collect results
    
    re.append(S_t)

# draw

fig, ax = plt.subplots()
x=list(range(2,26))
plt.plot(x,re,'go--',color='b',linewidth=2,markersize=10,mfc='none')
plt.ylabel('Time [s]')
plt.xlabel('Number of communities')
ax.set_xlim(xmin=0)
plt.title('Time corresponding to different number of communities')
plt.savefig('T_cluster_num.pdf')
plt.show()


# Exp of variance in cluster size

# generate sets of communities, each set contains 5 communities, and total 4 sets

Cring=SizeVariance_Commuinity(5, 25 ,4)

T_2=[]
for i in range(len(Cring)):
    S_t=0
    for j in range(3):
        
        # repeat 3 times
        
        c=Cring[i]
        start1=time.time()
        s1=APWP(edge_position,edge_possibility,c)
        end1=time.time()
        S_t+=end1-start1
    S_t/=3
    T_2.append(S_t)

# draw

from matplotlib.patches import Rectangle
species = ("[5,5,5,5,5]", "[9,4,4,4,4]", "[13,3,3,3,3]",'[17,2,2,2,2]')
penguin_means = {
    'FFN': (161.576),
    'Com_structure':(132.545)
}
width=0.25
patterns = [ "/" , "\\" , "|" , "-" , "+" , "x", "o", "O", ".", "*" ]
fig, ax = plt.subplots()
x = np.arange(len(species)) 



for xi, y in zip(x+0.25, T_2, ):
    
    re=ax.bar(xi, y, width=0.25, hatch="///", edgecolor="k",color='white')
    ax.bar_label(re,size=10)
ax.set_xticks(x + width, species,size=15)
plt.yticks(fontsize=15)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
          fancybox=True, shadow=True, ncol=5,frameon=False,fontsize=15)
ax.set_ylabel('Time [s]',fontsize=15)
ax.set_xlabel('List of community size [nodes]',fontsize=15)
ax.set_title('Calculation time of '+ r'$APWP^{EMOD}$' ,fontsize=15)
fig.set_figheight(6)
fig.set_figwidth(10)
plt.savefig('clustering_size.pdf')
