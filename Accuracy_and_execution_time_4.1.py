#!/usr/bin/env python
# coding: utf-8

# In[5]:


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


# edge = 9,14,21

for i in range(3,6):
    
    # load graph and communities
    
    node, edge_position, edge_possibility=load_graph('Expected_Modularity_Calculation_in_ProbabilisticGraph-main/datasets/'+str(i*3)+'nodes.npy')
    com = np.load('Expected_Modularity_Calculation_in_ProbabilisticGraph-main/datasets/'+str(i*3)+'_cluster.npy',allow_pickle=True)
    # assign edge probabilities as 0.3
    
    edge_possibility=[0.3 for i in range(len(edge_position))]
    
    # brute-force 

    start1=time.time()
    s2=brute_force(edge_possibility,Trans_C2(com,node),node,edge_position)
    end1=time.time()
    
    # APWP
    
    start2=time.time()
    s1=APWP(edge_position,edge_possibility,com)
    end2=time.time()
    
    # PWP
    
    start3=time.time()
    s3=PWP(edge_position,edge_possibility,com)
    end3=time.time()
    
    print('#edge=',len(edge_position))
    print('appro',s1,'brute',s2,'no appro',s3)
    print('no appro time',end3-start3,'brute-force',end1-start1,'appro time',end2-start2)


# edge = 25

i=6

# load graph and communities

node, edge_position, edge_possibility=load_graph('Expected_Modularity_Calculation_in_ProbabilisticGraph-main/datasets/'+str(i*3)+'nodes.npy')
com=com=np.load('Expected_Modularity_Calculation_in_ProbabilisticGraph-main/datasets/'+str(i*3)+'_cluster.npy',allow_pickle=True)
                
# assign edge probabilities as 0.3

edge_possibility=[0.3 for i in range(len(edge_position))]

# brute-force 

start1=time.time()
s2=brute_force(edge_possibility,Trans_C2(com,node),node,edge_position)
end1=time.time()

# APWP

start2=time.time()
s1=APWP(edge_position,edge_possibility,com)
end2=time.time()

# PWP

start3=time.time()
s3=PWP(edge_position,edge_possibility,com)
end3=time.time()

print('#edge=',len(edge_position))
print('appro',s1,'brute',s2,'no appro',s3)
print('no appro time',end3-start3,'brute-force',end1-start1,'appro time',end2-start2)

for i in range(7,9):
    

    # load graph and communities

    node, edge_position, edge_possibility=load_graph(str(i*3)+'nodes.npy')
    com=load_com(str(i*3)+'_cluster.npy')
    #com=np.load(str(i*3)+'_cluster.npy',allow_pickle=True) # when i=6,8 

    # assign edge probabilities as 0.3

    edge_possibility=[0.3 for i in range(len(edge_position))]

    # brute-force 

    start1=time.time()
    #s2=brute_force(edge_possibility,Trans_C2(com,node),node,edge_position)
    end1=time.time()

    # APWP

    start2=time.time()
    s1=APWP(edge_position,edge_possibility,com)
    end2=time.time()

    # PWP

    start3=time.time()
    s3=PWP(edge_position,edge_possibility,com)
    end3=time.time()

    print('#edge=',len(edge_position))
    print('appro',s1,'brute',s2,'no appro',s3)
    print('no appro time',end3-start3,'brute-force',end1-start1,'appro time',end2-start2)



