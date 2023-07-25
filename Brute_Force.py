#!/usr/bin/env python
# coding: utf-8

# In[5]:


def delta(i,j):
    if i==j:
        return 1
    else:
        return 0
def Adj_M(edge_position,pw_lst,node_n):
    import numpy as np
    A=np.zeros((node_n,node_n))
    for i in range(len(edge_position)):
        if (pw_lst[i]==1):
            A[edge_position[i][0]][edge_position[i][1]]=1
            A[edge_position[i][1]][edge_position[i][0]]=1
    return A


# In[12]:


def brute_force(p,c,node,edge):
    from Modularity import modularity_deter
    
    '''
    alculate expected modularity of probabilistic graph G is by dividing such probabilistic
    network into 2^m possible worlds, calculating the modularity on every possible world and their expected value.
    
    input:
    p: edge probabilities e.g., p=[0.2,0.3,0.5]
    c: communities e.g., c = [0,1,1,2,2,1]
    node: #nodse of probabilistic graph G
    edge: e.g., edge = [(0,1),(1,2),(1,3)]
    
    output:
    Q: expected modularity
    '''
    
    # initialization
    
    Q=0
    edge_n=len(p)
    
    # loop all possible worlds
    for i in range(2**edge_n):
        
        l_permu=bin(i)[2:].zfill(len(p))
        
        # initialize probability of each possible worlds
        
        p_pw=1
        
        # initialize possible worlds
        
        pw_lst=[]
        
        # generate possible worlds and probabilities of possible worlds
        
        for edge_id in range(len(l_permu)):

            pw_lst.append(int(l_permu[edge_id]))

            if int(l_permu[edge_id])==1:

                p_pw*=p[edge_id]
            else:

                p_pw*=(1-p[edge_id])
        
        # calculate expected modularity

        Q+=modularity_deter(c,node,pw_lst,edge)*p_pw

    return Q

