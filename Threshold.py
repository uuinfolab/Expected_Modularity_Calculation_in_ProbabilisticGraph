#!/usr/bin/env python
# coding: utf-8

# In[17]:


def threshold(thre, node, edge,p,c):
    from Modularity import modularity_deter
    '''
    After setting a threshold, we remove edges whose probability is lower than the threshold and consider 
    the others as deterministic
    
    input: 
    thre: threshold (float)
    node: #nodes in probabilistic graph G
    p: edge probabilities
    c: communities e.g., c=[0,0,1,0,2,1,2,2]
    '''
    ep=[]
    for i in range(len(p)):
        if p[i]<thre:
            ep.append(0)
        else:
            ep.append(1)
            
    
    Q=modularity_deter(c,node,ep,edge)
    
    return Q

