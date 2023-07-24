#!/usr/bin/env python
# coding: utf-8

# In[65]:


def Classic_Sampling(N_sample,c,edge,p,node):
    import itertools
    import random
    '''
    we first generate N_sample samples from the probability distribution over the possible worlds, then calculate
    modularity for each sample graph and compute the average modularity
    
    input: 
    N_sample: the number of samples
    c: communities e.g., c=[0,1,1,0,2]
    edge: e.g., edge=[(0,1),(2,3),(0,4)]
    p: edge probabilities e.g., p=[0.2,0.4,0.4]
    node: #nodes in a probabilistic graph
    
    
    output:
    Q: average modularity by sampling method
    '''
    
    
    edge_n=len(edge)
   
    #initialize 
    
    Samp=[]
    
    # choose samples from all possible worlds
        
    while (len(Samp)<N_sample):
        pw_lst=[]

        for j in range(edge_n):
            p_r=random.random()
            if p_r<=edge_possibility[j]:
                pw_lst.append(1)
            else:
                pw_lst.append(0)

        Samp.append(pw_lst)

    # calculate modularity 
    
    Q=0
    
    for samp in Samp:
        
        Q+=modularity_deter(c,node,samp,edge)
    
    # average modularity
    
    Q/=len(Samp)
        
    
    return Q
               

