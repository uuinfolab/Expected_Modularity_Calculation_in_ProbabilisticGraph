#!/usr/bin/env python
# coding: utf-8

def delta(i,j):
    if i==j:
        return 1
    else:
        return 0
def Adj_M(edge,pw_lst,node):
    import numpy as np
    A=np.zeros((node,node))
    for i in range(len(edge)):
        if (pw_lst[i]==1):
            A[edge[i][0]][edge[i][1]]=1
            A[edge[i][1]][edge[i][0]]=1
    return A



def modularity_deter(c,node,pw_lst,edge):
    import numpy as np
    '''
    input:
    c: communities e.g., c=[0,1,1,2,3,2]
    node: #nodes in probabilistic graph G
    pw_lst: each possible world e.g., pw_lst=[0,0,1,1,0,1,0,1,0]
    edge: e.g., edge=[(0,1),(0,2),(2,3),(1,4),(5,2),(3,7),(6,4),(5,6),(1,8)]
    
    output:
    modularity
    '''
    
    # initialization
    
    Q=0
    edge_n=len(pw_lst)    
    node_deg=list(np.zeros(node))
    
    # calculate node's degree
    
    for i in range(len(edge)):
        if pw_lst[i]==1:
            node_deg[edge[i][0]]+=1
            node_deg[edge[i][1]]+=1
    
    # if graph is an empty graph:
    
    if sum(pw_lst)==0:
        return 0
    
    # if graph is not empty:
    
    else:
    
    # iterate node by node
    
        for i in range(node):              
            for j in range(node):
                
                A=Adj_M(edge,pw_lst,node)

                # calculate modularity
                
                Q+=(A[i][j]/(2*sum(pw_lst))-(node_deg[i]*node_deg[j])/(2*sum(pw_lst))**2)*delta(c[i],c[j])
                
    return Q

