#!/usr/bin/env python
# coding: utf-8

# In[2]:


def Random_Community(N,node):
    import random
    '''
    Generate randomly communities
    
    input:
    N: #clusters
    node: #nodes
    
    output: 
    c: communities e.g., c=[0,0,0,1,1,2,2,1]
    '''
    
    # initialization
    
    c1=[]
    c2=[]
    c=[]
    
    c1=random.sample(range(1,N+1),N)
    c=c1+c2
    
    while(len(c)<node):
        c.append(random.randint(1,N))
    
    return c


# In[3]:


def SizeVariance_Commuinity(N_c, N_node ,N_clustering):
    import numpy as np
    import itertools
    '''
    we want to show the performance of APWP with the same number of communities but different community 
    size distributions. 
    
    input:
    N_c: #communities
    N_clustering: #sets of communities
    N_node: #nodes in probabilistic graph G
    
    output:
    c: communities e.g., c=[2,2,1,1,2,3,2,3,3]
    '''
    #initialization
    
    size=int(N_node/N_c)
    node=list(range(N_node))
    c=[]
    
    if size-(N_clustering -1 )<2:
        print('input (N_c) is unavailble, try to input a smaller N_c.')
        return
    
    
    #create average size clustering
    
    while(len(c)<N_clustering):
        
        c1=[node[x:x+size] for x in np.arange(0, len(node), size)]   
        c2=[]
        more_layer=len(c1)-N_clustering
        for i in range(len(c1)-more_layer):
            c2.append(c1[i])
            
        #merge the last remained layers
        
        c2.append(list(itertools.chain(*[i for i in c1[len(c1)-more_layer:len(c1)]])))
        
        c.append(c2)
        size-=1
    return c
            
        

