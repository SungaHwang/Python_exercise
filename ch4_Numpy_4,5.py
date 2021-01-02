#!/usr/bin/env python
# coding: utf-8

# ## 4.4 배열 데이터의 파일 입출력

# In[2]:


import numpy as np


# In[3]:


arr = np.arange(10)


# In[4]:


np.save('some_array',arr)


# In[5]:


np.load('some_array.npy')


# In[6]:


np.savez('array_archive.npz',a=arr,b=arr)


# In[7]:


arch = np.load('array_archive.npz')


# In[8]:


arch['b']


# In[9]:


np.savez_compressed('arrays_compressed.npz',a=arr,b=arr)


# ## 4.5 선형대수

# In[10]:


x = np.array([[1.,2.,3.],[4.,5.,6.]])


# In[11]:


y = np.array([[6.,23.],[-1,7],[8,9]])


# In[12]:


x


# In[13]:


y


# In[14]:


x.dot(y)


# In[15]:


np.dot(x,y)


# In[16]:


np.dot(x,np.ones(3))


# In[17]:


x @ np.ones(3)


# In[22]:


from numpy.linalg import inv, qr


# In[23]:


X = np.random.randn(5,5)


# In[24]:


mat = X.T.dot(X)


# In[25]:


inv(mat)


# In[26]:


mat.dot(inv(mat))


# In[27]:


q, r = qr(mat)


# In[28]:


r

