#!/usr/bin/env python
# coding: utf-8

# ## 4.6 난수 생성

# In[3]:


import numpy as np


# In[4]:


samples = np.random.normal(size=(4,4)) #표준정규분포


# In[5]:


samples


# In[6]:


from random import normalvariate


# In[7]:


N =1000000


# In[13]:


get_ipython().run_line_magic('timeit', 'np.random.normal(size=N)')


# In[14]:


np.random.seed(1234)


# In[15]:


rng = np.random.RandomState(1234)


# In[16]:


rng.randn(10)


# ## 4.7 계단 오르내리기 예제

# In[17]:


import random
position = 0
walk = [position]
steps= 1000
for i in range(steps):
    step = 1 if random.randint(0,1) else -1
    position += step
    walk.append(position)


# In[20]:


nsteps = 1000


# In[21]:


draws = np.random.randint(0,2,size=nsteps)


# In[22]:


steps = np.where(draws>0,1,-1)


# In[23]:


walk = steps.cumsum()


# In[24]:


walk.min()


# In[25]:


walk.max()


# In[26]:


(np.abs(walk)>= 10).argmax()


# ### 한 번에 시뮬레이션하기

# In[27]:


nwalks = 5000


# In[29]:


nsteps = 1000


# In[30]:


draws = np.random.randint(0,2,size=(nwalks,nsteps)) #0또는1


# In[31]:


steps = np.where(draws>0,1,-1)


# In[32]:


walks = steps.cumsum(1)


# In[33]:


walks


# In[34]:


walks.max()


# In[35]:


walks.min()


# In[36]:


hits30 = (np.abs(walks)>=30).any(1)


# In[37]:


hits30


# In[38]:


hits30.sum()

