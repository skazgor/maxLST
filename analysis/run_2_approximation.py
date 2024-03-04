#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
import re
program = "./2_appx"


# In[4]:


print('algorithm,file_name,number_of_nodes,number_of_leaf_nodes,time_taken')
algorithm = '2_Approximation'

for file_prefix in ['complete_grid_graph_', 'incomplete_grid_graph_', 'random_d_regular_graph_', 'random_graph_', 'scale_free_graph_']:
    for i in range(1,11):
        file_path = f"{file_prefix}{i}.txt"
        command = f"{program} < {file_path}"
        output = os.popen(command).read()

        time_taken_match = re.search(r"Time taken: (\d+) milliseconds", output)
        leaf_count_match = re.search(r"Leaf count: (\d+)", output)

        time_taken = int(time_taken_match.group(1)) if time_taken_match else None
        leaf_count = int(leaf_count_match.group(1)) if leaf_count_match else None


        with open(file_path, 'r') as file:
            first_line = file.readline()
            number_of_nodes = int(first_line.split()[0])
        

        print(f'{algorithm},{file_path},{number_of_nodes},{leaf_count},{time_taken/1000}')


# In[ ]:




