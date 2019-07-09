#!/usr/bin/env python
# coding: utf-8

# In[8]:


from urllib.request import urlopen# Load CSV using Pandas
from pandas import read_csv
filename = 'pima-indians-diabetes.data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
print(data.shape)
data.head()


# In[10]:


#look at the raw data
peek=data.head(20)
print(peek)


# In[11]:


#shape of data
shape=data.shape
print(shape)


# In[12]:


types =data.dtypes
print (types)


# In[13]:


description =data.describe()
print(description)


# In[15]:


class_counts=data.groupby('class').size()
print(class_counts)


# In[17]:


correlations=data.corr (method='pearson')
print (correlations)


# In[18]:


skew =data.skew()
print(skew)


# In[20]:


from matplotlib import pyplot
data.hist()
pyplot.show()


# In[21]:


data.plot(kind='density', subplots=True, layout=(3,3), sharex=False)
pyplot.show()


# In[22]:


data.plot(kind='box', subplots=True, layout=(3,3), sharex=False, sharey=False)
pyplot.show()


# In[24]:


import numpy as np
correlations = data.corr()
# plot correlation matrix
fig = pyplot.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(correlations, vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = np.arange(0,9,1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(names)
ax.set_yticklabels(names)
pyplot.show()


# In[25]:


fig = pyplot.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(correlations, vmin=-1, vmax=1)
fig.colorbar(cax)
pyplot.show()


# In[27]:


from matplotlib import pyplot
from pandas import read_csv
from pandas.plotting import scatter_matrix
scatter_matrix(data)
pyplot.show()


# In[ ]:




