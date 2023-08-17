#!/usr/bin/env python
# coding: utf-8

# In[6]:


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


# In[14]:


n=100
N_c=5

com = Random_Community(N_c,n)
com=Trans_C1(com)
t=[]
for i in np.arange(200,800,100):
    #construct network
    
    m=i
    edge_position,edge_possibility,node,nocom=rand_graph(n,m)
    entropy=0.4*m
    edge_possibility=entropy_(entropy,len(edge_possibility))
    edge_possibility=edge_possibility[0]
    random.shuffle(edge_possibility)
    
    #
    
    start1=time.time()
    s1=APWP(edge_position,edge_possibility,com)
    end1=time.time()
    
    #
    t.append(end1-start1)
    print(s1)
    


# In[15]:


for i in np.arange(900,1100,100):
    #construct network
    
    m=i
    edge_position,edge_possibility,node,nocom=rand_graph(n,m)
    entropy=0.4*m
    edge_possibility=entropy_(entropy,len(edge_possibility))
    edge_possibility=edge_possibility[0]
    random.shuffle(edge_possibility)
    
    #
    
    start1=time.time()
    s1=APWP(edge_position,edge_possibility,com)
    end1=time.time()
    
    #
    t.append(end1-start1)
    print(s1)


# In[18]:


for i in np.arange(1100,2600,500):
    #construct network
    
    m=i
    edge_position,edge_possibility,node,nocom=rand_graph(n,m)
    entropy=0.4*m
    edge_possibility=entropy_(entropy,len(edge_possibility))
    edge_possibility=edge_possibility[0]
    random.shuffle(edge_possibility)
    
    #
    
    start1=time.time()
    s1=APWP(edge_position,edge_possibility,com)
    end1=time.time()
    
    #
    t.append(end1-start1)
    print(s1)


# In[19]:


print(t)


# # Comparison

# In[21]:


n=10
N_c=5
t_our=[]
t_brute=[]
t_no_app=[]
com=Random_Community(N_c,n)

for i in np.arange(10,25,5):
    #construct network
    
    m=i
    edge_position,edge_possibility,node,nocom=rand_graph(n,m)
    entropy=0.4*m
    edge_possibility=entropy_(entropy,len(edge_possibility))
    edge_possibility=edge_possibility[0]
    random.shuffle(edge_possibility)
    
    #
    
    start1=time.time()
    s1=APWP(edge_position,edge_possibility,Trans_C1(com))
    end1=time.time()
    
    #
    t_our.append(end1-start1)
    
    
    #
    
    start2=time.time()
    s2=brute_force(edge_possibility,com,n,edge_position)
    end2=time.time()
    
    t_brute.append(end2-start2)
    
    #
    start3=time.time()
    s3=PWP(edge_position,edge_possibility,Trans_C1(com))
    end3=time.time()
    
    t_no_app.append(end3-start3)
    
    
    print('T our',end1-start1, 'T_brute',end2-start2,'T_noAppr',t_no_app)


# In[ ]:


t_our=[0.00030875205993652344,0.0006678104400634766,0.0012683868408203125,0.0014414787292480469,0.001672983169555664]
t_brute=[0.29813480377197266,12.224852085113525,483.53242683410645,1001.1495580673218,2048.8761751651764 ]
t_non=[0.0023784637451171875, 0.017066240310668945, 0.12788987159729004, 0.16925358772277832, 0.37462472915649414]


# In[ ]:


for i in np.arange(21,24,1):
    #construct network
    
    m=i
    edge_position,edge_possibility,node,nocom=rand_graph(n,m)
    entropy=0.4*m
    edge_possibility=entropy_(entropy,len(edge_possibility))
    edge_possibility=edge_possibility[0]
    random.shuffle(edge_possibility)
    
    
    
    
    #
    
    start2=time.time()
    s2=brute_force(edge_possibility,com,n,edge_position)
    end2=time.time()
    
    t_brute.append(end2-start2)
    
    
    #
    
    start1=time.time()
    s1=APWP(edge_position,edge_possibility,Trans_C1(com))
    end1=time.time()
    
    #
    t_our.append(end1-start1)
    
    #
    
    start3=time.time()
    s3=PWP(edge_position,edge_possibility,Trans_C1(com))
    end3=time.time()
    
    t_no_app.append(end3-start3)
    
    print('T our',end1-start1, 'T_brute',end2-start2,'T_noAppr',t_no_app)


# In[41]:


import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()

#data store

x=[10,15,20,23]+list(np.arange(200,1100,100))+list(np.arange(1100,2700,500))
print(x)
t=[0.0009,0.0021,0.0044,0.0074,2.777,9.779,24.265,47.686,83.091,155.835,233.461,288.008,443.471,534.077,1787.5306,3972.3575, 7553.0115]
plt.plot(x,t,'go--',color='r',linewidth=2,markersize=10,mfc='none',label=r'$APWP^{EMOD}$')
t2=[0.3813,14.759,560.034,5125.3251]
x2=[10,15,20,23]

x3=[10,15,20,25,30]
t3=[0.0016660690307617188,
 0.031000137329101562,
 0.19469213485717773,
 1.4496428966522217,
 20.115010738372803]
plt.plot(x3,t3,ls='--',marker='v',color='black',linewidth=2,markersize=10,mfc='none',label=r'$PWP^{EMOD}$')
plt.plot(x2,t2,ls='--',marker='d',color='b',linewidth=2,markersize=10,mfc='none',label='BF')
plt.ylabel('Time [s]')
plt.xlabel('Networks size [edges]')
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlim(xmin=0)
plt.legend()
plt.title('Time comparison according to different sizes of networks')
plt.savefig('size_Net.pdf')
plt.show()


# In[ ]:




