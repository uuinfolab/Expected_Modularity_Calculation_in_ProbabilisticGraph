#!/usr/bin/env python
# coding: utf-8

# In[1]:


def rand_graph(n,m):
    
    import random
    import networkx as nx


    seed = 20160  # seed random number generators for reproducibility

    # Use seed for reproducibility
    
    G = nx.gnm_random_graph(n, m, seed=seed)
    com=nx.community.louvain_communities(G)

    # some properties
    edge_possibility=[]
    edge_position=[]
    node=[]
    for v in nx.nodes(G):
        node.append(v)

    for m in nx.edges(G):
        edge_position.append(m)
        edge_possibility.append(random.random())
    
    return edge_position,edge_possibility,node,com


# In[2]:


from itertools import chain
from math import log, fabs, sqrt
from random import randint, betavariate, sample, random, uniform

from time import time
from bisect import bisect_left
import os
import mmap

def pd_shuffle(pd, times, prob_min):
    
    '''
    pick 2 probabilities and replace them to form new distribution.
    each time only choose 2 probabilities but can repeat 'times' time
    '''
    for i in range(times):
        idx0 = randint(0,len(pd)-1)
        p0 = pd.pop(idx0)
        idx1 = randint(0,len(pd)-1)
        p1 = pd.pop(idx1)
        s = p0 + p1
        if s==0:
            a=0
        else:
            a = min(p0,p1)/s
        
        xmin=a
        xmax = .5
        q0 = uniform(xmin,xmax)
       
        if q0*s>1:
                
                pd.append(q0*s-1)
        else:
            pd.append(q0*s)
        if (1-q0)*s>1:
            pd.append((1-q0)*s-1)
        else:
            pd.append((1-q0)*s)

def plog2p(p):
    '''
    basic entropy
    '''
    if p==0:
        return 0
    elif p>1:
        return log(1,2)
    else:
    
        return p*log(p,2) 

def entropy1(pd):
    '''
    basic entropy
    '''
    sum=0
    
    for p in pd:
       
        sum-=plog2p(p)+plog2p(1-p)
    
    return sum
   

def deviation(data):
    '''
    calculate data deviation
    '''
    if not (isinstance(data, TupleType) or isinstance(data, ListType)):
        data = tuple(data)
    m = mean(data)
    dev = sqrt(float(sum(( (m-d)**2 for d in data )))/len(data))
    return dev

def mean(data):
    '''
    calculate data mean
    '''
    s = 0.0
    i = 0
    for item in data:
        s += item
        i += 1
    return s/i



def _de(a, b, sum):
    return sum*(_plog2p(a) + _plog2p(1-a) - _plog2p(b) - _plog2p(1-b))

def pd_en_max(symbols_nr):
    '''
    symbols_nr is a integer
    return [1/sy,1/sy,...,1/sy]
    '''
    symbols_nr_fl = float(symbols_nr)
   
    return (( 0.5 for i in range(symbols_nr) ))

def entropy_max(symbols_nr):
    
    '''
    #calculate pd_en_max entropy
   
    '''
  
    return entropy1(list(pd_en_max(symbols_nr)))

def pd_en_min(symbols_nr, prob_min):
    '''
    return list[prob_max,prob_min,prob_min,prob_min...]
    '''
   
    
    #v2
    import random
    return list(random.randint(0,1) for i in range(symbols_nr))
   

def entropy_min(symbols_nr, prob_min):
    '''
    calculate pd_en_min entropy
    don't know its realistic reason???
    '''
    return entropy1(pd_en_min(symbols_nr, prob_min))
    
__prob_min = 1e-6
def e2pd_initial_pd(symbols_nr, prob_min=__prob_min, shuffle=0, initial="max"):
        if initial == "min":
            
            #pd list's entropy is the smallest
            
            pd = list(pd_en_min(symbols_nr, prob_min))
        elif initial == "max":
            
            #pd list's entropy is the largest
            
             pd = list(pd_en_max(symbols_nr))
        else:
            raise ValueError( "initial %s unknown" % initial )
        pd_shuffle(pd, shuffle, prob_min)
        
        #small to large
        
        pd.sort()
        return pd
    
    
def entropy2pd(tentropy, symbols_nr, pd=None, prob_min=__prob_min, entropy_err=.01):
        """ Create a probability distribution (pd) for a set of symbols that will
            adhere to the given entropy value

            tentropy    : target entropy value
            symbols_nr  : number of symbols
            prob_min    : minum value for probabilities
            entropy_err : margin for error between the given and pd entropy

            The basic concept is to choose two probabilities from the list and
            modify them so that we are close to the target entropy.

            returns a list of symbols_nr probabilities
        """
        # sanity checks
        
        if (tentropy > entropy_max(symbols_nr)):   
            raise ValueError( "entropy specified (%f) is too high" % tentropy)
        if (tentropy < entropy_min(symbols_nr,prob_min)):
            raise ValueError( "entropy specified (%f) is too small" % tentropy)

            
        #lowest entropy=0
        
        if float(tentropy)==0.0:
            return [1 for i in range(symbols_nr)]
        
        #largest entropy=1*symbols_nr
        
        if tentropy==1*symbols_nr:
            return [0.5 for i in range(symbols_nr)]
        

        # Choose an initial probability distribution
        
        if pd is None:
            
            #default max entropy list
            
            pd = e2pd_initial_pd(symbols_nr, prob_min)
       
        iterations = 0
        alpha = beta = 1.3
        while True:
            
            pd.sort()
          
            for k in pd:
                if k>1:
                    print('illege!!', iterations,'time')
                    print('Beta distribution','alpha',alpha,'beta',beta)
                    print('old edge possibilites','p0',p0,'p1',p1,'p0+p1',s)
                    print('new value','q0',q0, 'edge_pos1',q0*s,'edge_pos2',(1-q0)*s)
                    
                    
            #________________________
            entropy_pd = entropy1(pd)
            
            # convergence
            
            de = tentropy - entropy_pd
            
            if iterations % 512 == 1: 
                alpha = uniform(.5, 10)
                beta  = uniform(.5, 10)
                
            #judge difference between target entropy and realistic current entropy
     
            if fabs(de) <= entropy_err:
                break
                
            elif tentropy > entropy_pd:
                p0 = pd.pop(int((len(pd))*(betavariate(alpha,beta))))
                p1 = pd.pop(int((len(pd))*(betavariate(beta,alpha))))
                s = p0 + p1
                if s==0:
                    a=0
                else:
                    a = min(p0,p1)/s
                
                xmin = a
                xmax = .5

            else:
                
                p0 = pd.pop(int((len(pd))*(betavariate(alpha,beta))))
                p1 = pd.pop(int((len(pd))*(betavariate(alpha,beta))))
                s = p0 + p1
                if s==0:
                    a=0
                else:
                    a = min(p0,p1)/s
               
                if s==0:
                    xmin=0
                else:
                    xmin = prob_min/s
                
                xmax = a
                        
            q0 = uniform(xmin,xmax)
            nu1=q0*s
            nu2=(1-q0)*s
            
            if q0*s>1:
                
                pd.append(q0*s-1)
            else:
                pd.append(q0*s)
            if (1-q0)*s>1:
                pd.append((1-q0)*s-1)
            else:
                pd.append((1-q0)*s)

            iterations += 1
            
        #change all 0 to 1 in pd
        
        for i in range(len(pd)):
            if float(pd[i])==0.0:
                pd[i]=1

        return pd


import matplotlib.pyplot as plt
from random import randint, sample
from random import sample


import sys

def entropy_(entropy, symbols_nr, graphs_nr=1):
        
        
        _initial = ("min", "max")
        pd = []
        for i in range(graphs_nr):
            
            sys.stdout.flush()
            pdi = e2pd_initial_pd(symbols_nr,shuffle=randint(0,symbols_nr*2),initial=sample(_initial, 1)[0])
            
            l=entropy2pd(entropy, symbols_nr, pdi)
            pd.append(list(l))
            
        return pd
def rand_graph_entropy(n,m,entropy):
    '''
    create the same structure random graphs with different edge possibilities assignment using entropy
    input:
    n: number of nodes
    m: number of edges
   
    entropy: list [1,2,3,4,5]
    
    output:
    networks with same edge_positions and nodes but different edge possibilities distribution
    each networks' entropy
    '''
    import random
    import networkx as nx

    # seed random number generators for reproducibility

    seed = 20160  
    
    # Use seed for reproducibility
    
    G = nx.gnm_random_graph(n, m, seed=seed)

    # some properties
    
    edge_position=[]
    node=[]
    for v in nx.nodes(G):
        node.append(v)
        
        
    E_P=[]
   
    
    for i in range(len(entropy)):
        ep=rand_graph(entropy[i], m)
        E_P.append(ep)

    for m in nx.edges(G):
        edge_position.append(m)
       
    
    return edge_position,node,E_P


# In[3]:


def rand_graph_com(l,k,p_in,p_out,entropy):
    '''
    l: number of groups
    k: number of vertex in each groups
    p_in: possibility within groups
    p_out: possibility between groups
    entropy: int
    '''
    import networkx as nx
    import random
    g=nx.planted_partition_graph(l,k,p_in,p_out)
    
    com=nx.community.louvain_communities(g)
    node=[]
    for v in nx.nodes(g):
            node.append(v)
    edge_position=[]
    edge_possibility=[]
    for m in nx.edges(g):
            edge_position.append(m)
           
    edge_possibility=rand_graph(entropy, len(nx.edges(g)))
    
    return edge_position, edge_possibility[0],com,len(g.nodes)

