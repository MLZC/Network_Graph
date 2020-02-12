#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


csv_data=pd.read_csv("./Edges_separate.csv")


# In[5]:


source=np.array(csv_data['Source']).reshape(-1,1)
target=np.array(csv_data['Target']).reshape(-1,1)


# In[6]:


edges=np.concatenate((source,target),axis=1)


# In[7]:


G=nx.Graph()


# In[8]:


G.add_edges_from(edges)


# In[9]:


print("The Graph has %d number of nodes!" % G.number_of_nodes())
print("The Graph has %d number of edges!" % G.number_of_edges())
print("The Graph has %d number of selfloops!" % G.number_of_selfloops())


# In[ ]:


nx.draw(G, with_labels=True)
plt.savefig("Graph.png")
plt.show()

