#!/usr/bin/env python
# coding: utf-8

# In[1]:


def PB(k,p):
    '''
    calculate partitions' probabilities using poisson binomial distribution
    
    input:
    k: #edges existed in one partition
    p: edge probabilities e.g., p=[0.2,0.3,0.1,0.5,0.5,0.8]
    
    output:
    result: probabilities of partitions
    '''
    
    #initialization
    
    result=0
    
    # if no edge in a partition:
    
    if len(p)==0:
        return 1
    
    # loop all possible worlds in a partition
    
    for i in range(2**len(p)):
        
        l_permu=bin(i)[2:].zfill(len(p))
        
        #if the number of edges in possible world is equal to k
        
        if  sum([int(j) for j in l_permu])==k:
            
            re=1
            
            # calculate probability of this possible world
            
            for edge_id in range(len(l_permu)):

                if int(l_permu[edge_id])==1:
                    
                    re*=p[edge_id]
                else:
                   
                    re*=(1-p[edge_id])
            result+=re
                   
    return result


# In[2]:


def DFT(k,p):
    import math
    import cmath
    '''
    Approximate the probability of partitions using discrete fourier transform
    
    input:
    k: #edges existed in one partition
    p: edge probabilities e.g., p=[0.2,0.3,0.5,0.6,0.5]
    
    output:
    approximated probabilities of partitions
    '''

    n=len(p)
    C=math.e**((2*cmath.sqrt(-1)*math.pi)/(n+1))
    result=0
    
    for l in range(n+1):
        re1=C**(-l*k)
        re2=1
        for m in range(n):
            re2*=(1+(C**l-1)*p[m])
        result+=re1*re2
    return (1/(1+n))*result  

