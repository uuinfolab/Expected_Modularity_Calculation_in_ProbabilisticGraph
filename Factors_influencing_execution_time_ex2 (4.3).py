#!/usr/bin/env python
# coding: utf-8

# # Forest Fire Network Model

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import random
import time
import csv
from collections import defaultdict


# ------------------------------------
from Classic_Sampling import classic_sampling
from Brute_Force import brute_force
from Algorithms import APWP,PWP, Trans_C1,Trans_C2
from Probabilities import PB,DFT
from Network_Generator import rand_graph, rand_graph_com,entropy_
from Communities import Random_Community,SizeVariance_Commuinity
from Threshold import threshold
from Save_Load import save_graph,load_graph,save_com,load_com

# read edges of FFN 

filename='ffn.csv'
f=open(filename,"r")
lines=f.readlines()
edge_position_ffn=[]

for x in lines:
    node1=int(x.split(' ')[0])
    node2=int(x.split(' ')[1].split('\n')[0])
 
    edge_position_ffn.append((node1,node2))
    
f.close()

#generate edge probabilities

entropy=0.4
edge_possibility_FFN=entropy_(entropy*len(edge_position_ffn),len(edge_position_ffn))
edge_possibility_FFN=edge_possibility_FFN[0]

columns = defaultdict(list) # each value in each column is appended to a list

#open community file to read the number of communities
'''
#c = 4: cluster_ffn_c=4.csv
#c = 5: cluster_ffn_c=5.csv
#c = 6: cluster_ffn_c=6.csv
'''

with open('cluster_ffn_c=6.csv') as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value 
            columns[k].append(v) # append the value into the appropriate list
                                 # based on column name k

c=[]
for i in range(len(columns['Id'])):
    c.append([int(columns['Id'][i]),int(columns['modularity_class'][i])])
c=sorted(c,key=lambda l:l[1])

com=[]
front_point=0
c1=[]
c1.append(c[0][0])
for i in range(1,len(c)):
    
    later_point=i
    if c[later_point][1]==c[front_point][1]:
        c1.append(c[later_point][0])
        
    else:
        com.append(c1)
        
       
        c1=[]
        c1.append(c[later_point][0])
    
    if later_point==len(c)-1:
        
        com.append(c1)
        
        
    front_point=later_point
    
ss=0
for i in com:
    ss+=len(i)

#shuffle edges

random.shuffle(edge_possibility_FFN)
plt.plot(edge_possibility_FFN)

#Calculate APWP

start1=time.time()
s1=APWP(edge_position_ffn,edge_possibility_FFN,com)#older version com is wrong
end1=time.time()


#  Barabási-Abert

# read edges

filename='ba.csv'
f=open(filename,"r")
lines=f.readlines()
edge_position_BA=[]
for x in lines:
    node1=int(x.split(' ')[0])
    node2=int(x.split(' ')[1].split('\n')[0])
    edge_position_BA.append((node1,node2))
    
f.close()

columns = defaultdict(list) # each value in each column is appended to a list

# open file to read number of communities

'''
#c = 4: cluster_ba_c=4.csv
#c = 5: cluster_ba_c=5.csv
#c = 6: cluster_ba_c=6.csv
'''

with open('cluster_ba_c=5.csv') as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value 
            columns[k].append(v) # append the value into the appropriate list
                                 # based on column name k

print(len(columns['Id']))
print(columns['modularity_class'])

c=[]
for i in range(len(columns['Id'])):
    c.append([int(columns['Id'][i]),int(columns['modularity_class'][i])])
c=sorted(c,key=lambda l:l[1])

c
com=[]
front_point=0
c1=[]
c1.append(c[0][0])
for i in range(1,len(c)):
    
    later_point=i
    if c[later_point][1]==c[front_point][1]:
        c1.append(c[later_point][0])
        
    else:
        com.append(c1)
        
       
        c1=[]
        c1.append(c[later_point][0])
    
    if later_point==len(c)-1:
        
        com.append(c1)
        
        
    front_point=later_point
    
ss=0
for i in com:
    ss+=len(i)

#To control the edge probabilities in BA is similar in FFN

edge_possibility_BA=[]
for i in range(len(edge_position_BA)):
    edge_possibility_BA.append(edge_possibility_FFN[i])

# calculate APWP

start1=time.time()
s1=APWP(edge_position_BA,edge_possibility_BA,com)
end1=time.time()

#  ER model

# read edges

filename='er.csv'
f=open(filename,"r")
lines=f.readlines()
edge_position_ER=[]
for x in lines:
    node1=int(x.split(' ')[0])
    node2=int(x.split(' ')[1].split('\n')[0])
    edge_position_ER.append((node1,node2))
    
f.close()

columns = defaultdict(list) # each value in each column is appended to a list

# open file to read communities
'''
#c = 4: cluster_er_c=4.csv
#c = 5: cluster_er_c=5.csv
#c = 6: cluster_er_c=6.csv
'''

with open('cluster_er_c=5.csv') as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value 
            columns[k].append(v) # append the value into the appropriate list
                                 # based on column name k


c=[]
for i in range(len(columns['Id'])):
    c.append([int(columns['Id'][i]),int(columns['modularity_class'][i])])
c=sorted(c,key=lambda l:l[1])

com=[]
front_point=0
c1=[]
c1.append(c[0][0])
for i in range(1,len(c)):
    
    later_point=i
    if c[later_point][1]==c[front_point][1]:
        c1.append(c[later_point][0])
        
    else:
        com.append(c1)
        
       
        c1=[]
        c1.append(c[later_point][0])
    
    if later_point==len(c)-1:
        
        com.append(c1)
        
        
    front_point=later_point
    
ss=0
for i in com:
    ss+=len(i)

#To control edge probabilities in ER is similar in FFN and BA

edge_possibility_ER=[]
for i in range(len(edge_possibility_FFN)):
    edge_possibility_ER.append(edge_possibility_FFN[i])
while(len(edge_possibility_ER)<len(edge_position_ER)):
    edge_possibility_ER.append(random.random())
    
# calculate APWP

start1=time.time()
s1=APWP(edge_position_ER,edge_possibility_ER,com)
end1=time.time()

# Small world

# read edges

filename='sw.csv'
f=open(filename,"r")
lines=f.readlines()
edge_position_SW=[]
for x in lines:
    node1=int(x.split(' ')[0])
    node2=int(x.split(' ')[1].split('\n')[0])
    edge_position_SW.append((node1,node2))
    
f.close()

# To control edge probabilities in SW is similar in ER, FFN, and BA

edge_possibility_SW=[]
for i in edge_possibility_ER:
    edge_possibility_SW.append(i)

columns = defaultdict(list) # each value in each column is appended to a list

# open file to read communities
'''
#c = 4: cluster_sw_c=4.csv
#c = 5: cluster_sw_c=5.csv
#c = 6: cluster_sw_c=6.csv
'''
with open('cluster_sw_c=5.csv') as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value 
            columns[k].append(v) # append the value into the appropriate list
                                 # based on column name k

c=[]
for i in range(len(columns['Id'])):
    c.append([int(columns['Id'][i]),int(columns['modularity_class'][i])])
c=sorted(c,key=lambda l:l[1])

com=[]
front_point=0
c1=[]
c1.append(c[0][0])
for i in range(1,len(c)):
    
    later_point=i
    if c[later_point][1]==c[front_point][1]:
        c1.append(c[later_point][0])
        
    else:
        com.append(c1)
        
       
        c1=[]
        c1.append(c[later_point][0])
    
    if later_point==len(c)-1:
        
        com.append(c1)
        
        
    front_point=later_point
    
ss=0
for i in com:
    ss+=len(i)

# calcualte APWP

start1=time.time()
s1=APWP(edge_position_SW,edge_possibility_SW,com)
end1=time.time()

# ____________________________
# CCS graph

import networkx as nx
import matplotlib.pyplot as plt 


# C=5

# generate graph

k=5
l=40
p_in=0.111
p_out=0.01
g_ffn=nx.planted_partition_graph(k,l,p_in,p_out)

edge_position_c_5=[]
   
for m in nx.edges(g_ffn):
        edge_position_c_5.append(m)

# generate communities

com=nx.community.louvain_communities(g_ffn)

#To control edge probabilities similar to SW, BA, FFN, and ER

edge_pos_c_5=[]
for i in edge_possibility_SW:
    edge_pos_c_5.append(i)
while(len(edge_pos_c_5)<len(edge_position_c_5)):
    edge_pos_c_5.append(random.random())

# calculate APWP

start1=time.time()
s1=APWP(edge_position_c_5,edge_pos_c_5,com)
end1=time.time()

# C=4

# generate graph

k=4
l=50
p_in=0.09
p_out=0.01
g_ba=nx.planted_partition_graph(k,l,p_in,p_out)


edge_position_c_ba=[]
   
for m in nx.edges(g_ba):
        edge_position_c_ba.append(m)
edge_possibility_c_ba=[]
for i in range(len(edge_position_c_ba)):
    edge_possibility_c_ba.append(edge_possibility_ER[i])

# generate communities

com=nx.community.louvain_communities(g_ba)

# calcualte APWP

start1=time.time()
s1=APWP(edge_position_c_ba,edge_possibility_c_ba,com)
end1=time.time()

# C=6

# generate graph

k=6
l=34
p_in=0.13
p_out=0.01
g_sw=nx.planted_partition_graph(k,l,p_in,p_out)

# generate communities

com=nx.community.louvain_communities(g_sw)

edge_position_c_sw=[]
   
for m in nx.edges(g_sw):
        edge_position_c_sw.append(m)

# calcuate APWP

start1=time.time()
s1=APWP(edge_position_c_sw,edge_possibility_SW,com)
end1=time.time()

# save data and draw

from matplotlib.patches import Rectangle
species = ("C=4", "C=5", "C=6")

width=0.25
patterns = [ "/" , "\\" , "|" , "-" , "+" , "x", "o", "O", ".", "*" ]
fig, ax = plt.subplots()
x = np.arange(len(species)) 



re1=ax.bar(x+0.1,[195.023,240.317,231.256],width=0.12,label='FFN',hatch='///',color='white',edgecolor='black')
ax.bar_label(re1,size=8)
re2=ax.bar(x+0.25,[76.766,122.843,159.968],width=0.12,label='BA',hatch='|||',color='white',edgecolor='black')
ax.bar_label(re2,size=8)
re3=ax.bar(x+0.4,[82.754,122.283,153.788],width=0.12,label='ER',hatch='--',color='white',edgecolor='black')
ax.bar_label(re3,size=8)
re4=ax.bar(x+0.55,[97.522,140.291,176.599],width=0.12,label='SW',hatch='xx',color='white',edgecolor='black')
ax.bar_label(re4,size=8)
re5=ax.bar(x+0.7,[86.052,125.015,163.547],width=0.12,label='CCS graph',hatch='..',color='white',edgecolor='black')
ax.bar_label(re5,size=8)


ax.set_xticks(x + width, species,size=15)
plt.yticks(fontsize=15)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
          fancybox=True, shadow=True, ncol=5,frameon=False,fontsize=15)
ax.set_ylabel('Time (s)',fontsize=15)
ax.set_title('Computation time in different networks',fontsize=15)
fig.set_figheight(6)
fig.set_figwidth(10)
plt.savefig('partition_time.pdf')

