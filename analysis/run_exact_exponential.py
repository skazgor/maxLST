#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
import re
program = "./exact_exponential"


# In[5]:


print('algorithm,file_name,number_of_nodes,number_of_leaf_nodes,time_taken')
algorithm = 'exact_exponential'

for i in range(1,33):
    file_path = f"random_graph_{i}.txt"
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




