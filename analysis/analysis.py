#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# In[2]:


df = pd.read_csv('data_1.csv')


# In[3]:


df.info()


# In[4]:


df.algorithm.value_counts()


# In[5]:


sub_df = df[df.algorithm == 'exact_exponential']
sns.lineplot(x='number_of_nodes', y='time_taken', hue='algorithm', data=df, markers = True)
# plt.title('Exact Exponential Algorithm')
plt.title('Run Time Analysis for All Algorithms')
plt.xlabel('Number of Nodes')
plt.ylabel('Time Taken (seconds)')
plt.show()


# In[6]:


new_df = df.pivot_table(index='number_of_nodes', columns='algorithm', values='number_of_leaf_nodes', aggfunc='mean')

new_df['ratio_2_approximation'] =  new_df['exact_exponential'] / new_df['2_Approximation']
new_df['ratio_priority_bfs'] = new_df['exact_exponential'] / new_df['Priority-BFS']
new_df['ratio_sa'] = new_df['exact_exponential'] / new_df['Simulated_Annealing']


# In[7]:


display(new_df)


# In[8]:


sns.lineplot(data=new_df[['ratio_2_approximation', 'ratio_priority_bfs', 'ratio_sa']], markers='o')

plt.title('Ratio of Exact Exponential to Other Algorithms')
plt.xlabel('Number of Nodes')
plt.ylabel('Ratio')
plt.ylim(1, 1.6)

# Show plot
plt.show()


# In[9]:


new_df.ratio_2_approximation.mean()


# In[10]:


new_df.ratio_priority_bfs.mean()


# In[11]:


new_df.ratio_sa.mean()


# ## Data 2

# In[12]:


df2 = pd.read_csv('data_2.csv')


# In[13]:


# sns.lineplot(x='number_of_nodes', y='time_taken', data=df2[df2.algorithm == 'Priority-BFS'], markers = True)
sns.lineplot(x='number_of_nodes', y='time_taken', hue='algorithm', data=df2, markers = True)
sns.scatterplot(x='number_of_nodes', y='time_taken', data=df2[df2.algorithm == 'Priority-BFS'], markers = True)
plt.title('Priority-BFS and 2-Approximation')
plt.xlabel('Number of Nodes')
plt.ylabel('Time Taken (seconds)')
plt.show()


# In[14]:


df3 = pd.read_csv('data_3.csv')

sns.lineplot(x='number_of_nodes', y='time_taken', hue='algorithm', data=df3, markers = True)
sns.scatterplot(x='number_of_nodes', y='time_taken', data=df3, markers = True)
plt.title('Simulated Annealing Algorithm')
plt.xlabel('Number of Nodes')
plt.ylabel('Time Taken (seconds)')
plt.show()


# In[ ]:




