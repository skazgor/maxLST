#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv('data_4.csv')


# In[3]:


df.info()


# In[4]:


df.number_of_nodes.value_counts()


# In[5]:


df.algorithm.value_counts()


# In[6]:


scale_free_df = df[df.file_name.str.startswith('scale')]
random_df = df[df.file_name.str.startswith('random_graph')]
complete_df = df[df.file_name.str.startswith('complete')]
incomplete_df = df[df.file_name.str.startswith('incomplete')]
d_regular = df[df.file_name.str.startswith('random_d')]


# In[7]:


random_df.info()


# In[8]:


sns.lineplot(data=random_df, x='number_of_nodes', y='number_of_leaf_nodes', hue='algorithm')
plt.title('Number of Nodes and Number of Leaf Nodes for random graph')
plt.show()


# In[9]:


sns.lineplot(data=complete_df, x='number_of_nodes', y='number_of_leaf_nodes', hue='algorithm')
plt.title('Number of Nodes and Number of Leaf Nodes for complete grid graph')
plt.show()


# In[10]:


sns.lineplot(data=incomplete_df, x='number_of_nodes', y='number_of_leaf_nodes', hue='algorithm')
plt.title('Number of Nodes and Number of Leaf Nodes for incomplete grid graph')
plt.show()


# In[11]:


sns.lineplot(data=d_regular, x='number_of_nodes', y='number_of_leaf_nodes', hue='algorithm')
plt.title('Number of Nodes and Number of Leaf Nodes for d-regular graph')
plt.show()


# In[12]:


pivot_df = scale_free_df.pivot_table(index='algorithm', values='number_of_leaf_nodes', aggfunc='mean')
plt.show()


# In[13]:


pivot_df


# In[14]:


plt.figure(figsize=(20, 6))
ax = pivot_df.plot(kind='bar')
plt.xlabel('Algorithm')
plt.ylabel('Mean Number of Leaf Nodes')
plt.title('Scale-free network of size 100')
ax.set_ylim(60, 80)
plt.show()


# In[ ]:




