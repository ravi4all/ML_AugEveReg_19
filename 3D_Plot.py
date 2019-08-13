
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#get_ipython().magic('matplotlib inline')


# In[2]:


data = pd.read_csv('data/student.csv')


# In[3]:


math = data['Math'].values
read = data['Reading'].values
write = data['Writing'].values


# In[5]:


fig = plt.figure(figsize=(15,8))
ax = Axes3D(fig)
ax.scatter(math,read,write,color='red')

plt.show()
