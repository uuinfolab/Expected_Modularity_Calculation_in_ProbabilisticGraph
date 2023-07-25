#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[2]:


node, edge_position, edge_possibility=load_graph('/.../Downloads/Expected_Modularity_Calculation_in_ProbabilisticGraph-main/datasets/3Community9nodes_each0.72within0.12between.npy')
com=load_com('/.../Downloads/Expected_Modularity_Calculation_in_ProbabilisticGraph-main/datasets/3Community9nodes_each0.72within0.12between_cluster.npy')


# In[3]:


edge_possibility=[]

'''
x=1, entropy ratio = 0.00
x=0.9, entropy ratio = 0.47
x=0.5, entropy ratio = 1.00
'''

x=0.5
for i in range(len(edge_position)):
    edge_possibility.append(x)


# In[5]:


t_our=[]
s_our=[]

_t1_pro_quota=[]
_s1_pro_quota=[]

node_n=node

#our method

start1=time.time()
s1=APWP(edge_position,edge_possibility,com)
end1=time.time()

# collect results

t_our.append(end1-start1)
s_our.append(s1)

# Classic Sampling

for i in np.arange(100,900,100):
   
    p_t1_pro_quota=[]
    p_s1_pro_quota=[]
    p_t1_quota=[]
    p_s1_quota=[]
    for k in range(10):
        N_sample=i
        
        start3=time.time()

        Q_2=classic_sampling(N_sample,Trans_C2(com,node),edge_position,edge_possibility,node)

        end3=time.time()

        p_t1_pro_quota.append(end3-start3)
        
        p_s1_pro_quota.append(Q_2)

    _t1_pro_quota.append(p_t1_pro_quota)
    _s1_pro_quota.append(p_s1_pro_quota)
    


# In[6]:


for i in np.arange(10,100,10):
   
    p_t1_pro_quota=[]
    p_s1_pro_quota=[]
    p_t1_quota=[]
    p_s1_quota=[]
    for k in range(10):
        N_sample=i

        start3=time.time()

        Q_2=classic_sampling(N_sample,Trans_C2(com,node),edge_position,edge_possibility,node)

        end3=time.time()

        p_t1_pro_quota.append(end3-start3)
       
        p_s1_pro_quota.append(Q_2)

    _t1_pro_quota.append(p_t1_pro_quota)
    _s1_pro_quota.append(p_s1_pro_quota)
    


# # Calculate mean and deviation

# In[7]:


import numpy as np

T_pro_quota_mean=[]
T_pro_quota_dev=[]
T_quota_mean=[]
T_quota_dev=[]


S_pro_quota_mean=[]
S_pro_quota_dev=[]
S_quota_mean=[]
S_quota_dev=[]

for i in range(len(_t1_pro_quota)):

    T_pro_quota_mean.append(np.mean(_t1_pro_quota[i]))
    T_pro_quota_dev.append(np.std(_t1_pro_quota[i]))
    S_pro_quota_mean.append(np.mean(_s1_pro_quota[i]))
    S_pro_quota_dev.append(np.std(_s1_pro_quota[i]))
   


# # Draw and save

# In[8]:


T=[]

for j in range(len(_t1_pro_quota[0])):
    t=[]
    for i in range(len(_t1_pro_quota)):
        
        t.append(_t1_pro_quota[i][j])
        
    T.append(t)

S=[]
for j in range(len(_s1_pro_quota[0])):
    s=[]
    for i in range(len(_s1_pro_quota)):
        s.append(_s1_pro_quota[i][j])
        
    S.append(s)


# In[9]:



# draw

fig, ax = plt.subplots()

for i in range(len(_t1_pro_quota[0])-1):
    plt.plot(T[i],S[i],'o',mfc='red',
     mec='black')
plt.plot(T[1],S[1],'o',mfc='red',
     mec='black',label='Classic Sampling')
uu=0.1
col=['lightcoral','coral','greenyellow','turquoise','cyan','indigo','fuchsia','plum','steelblue','magenta','blueviolet']
ax.axvline(x =t_our, color = 'b',ls=':',linewidth=3)
ax.axhline(y=s_our[0].real, color='b',ls=':',linewidth=3)
plt.plot(t_our,s_our[0].real,'o',mfc='blue',
     mec='black',markersize=8,label=r'$APWP^{EMOD}$')
plt.ylabel('Value of expected modularity')
plt.xlabel('Time [s]')
ax.set_xlim(xmin=0)
ax.set_ylim([0.4, 0.45])
ax.set_xlim([0.001,20])
ax.set_xscale('log')

ax.annotate('({}, {})'.format(round(t_our[0],3),round(s_our[0].real,3) ), xy=(2,1), xytext=(3, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05))
ax.legend(loc='upper right', bbox_to_anchor=(1, 0.9),prop={'size': 8})

# entropy ratio depend on edge probability

plt.title('Entropy ratio=1.00')
plt.savefig('Pe=0.5_lccs.pdf')
plt.show()

