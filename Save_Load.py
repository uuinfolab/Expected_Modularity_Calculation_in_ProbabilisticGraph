#!/usr/bin/env python
# coding: utf-8

# In[1]:


def save_graph(node, edge_position, edge_possibility,filename):
    import numpy as np
    file=filename
    M=np.zeros([node,node])
    
    for i in range(len(edge_position)):
        M[edge_position[i][0],edge_position[i][1]]=edge_possibility[i]
        M[edge_position[i][1],edge_position[i][0]]=edge_possibility[i]
        
    np.save(file,M)
    


# In[3]:


def save_com(com,filename):
    
    import numpy as np
    comm=[]
    for i in range(len(com)):
        c1=[]
        cc=list(com[i])
        for j in range(len(cc)):
            c1.append(cc[j])
        comm.append(c1)
    file=filename
    np.save(file,comm)



def load_graph(filename):
    import numpy as np
    M=np.load(filename)
    node=len(M)
    edge_position=[]
    edge_possibility=[]
    for i in range(node):
        for j in range(i,node):
            if M[i,j]!=0:
                edge_position.append((i,j))
                edge_possibility.append(M[i,j])
  
    return node, edge_position, edge_possibility




def load_com(filename):
    import numpy as np
    return np.load(filename,allow_pickle=True).astype(int)
   
