#!/usr/bin/env python
# coding: utf-8

# ## 4.2 유니버설 함수: 배열의 각 원소를 빠르게 처리하는 함수

# In[3]:


import numpy as np


# In[4]:


arr = np.arange(10)


# In[5]:


arr


# In[6]:


np.sqrt(arr)


# In[7]:


np.exp(arr)


# In[9]:


x = np.random.randn(8)


# In[10]:


y = np.random.randn(8)


# In[11]:


x


# In[12]:


y


# In[13]:


np.maximum(x,y)


# In[14]:


arr = np.random.randn(7) * 5


# In[15]:


arr


# In[16]:


remainder, whole_part = np.modf(arr)


# In[17]:


remainder


# In[18]:


whole_part


# In[19]:


arr


# In[20]:


np.sqrt(arr)


# In[21]:


np.sqrt(arr,arr)


# ## 4.3 배열을 이용한 배열지향 프로그래밍

# In[22]:


points = np.arange(-5, 5, 0.01)


# In[23]:


xs, ys = np.meshgrid(points,points)


# In[24]:


ys


# In[25]:


z = np.sqrt(xs**2+ys**2)


# In[26]:


z


# In[27]:


import matplotlib.pyplot as plt


# In[28]:


plt.imshow(z, cmap = plt.cm.gray); plt.colorbar()


# In[30]:


plt.title("Image plot of $\sqrt{x^2+y^2}$ for a grid of values")


# ### 배열 연산으로 조건절 표현하기

# In[31]:


xarr = np.array([1.1,1.2,1.3,1.4,1.5])


# In[32]:


yarr = np.array([2.1,2.2,2.3,2.4,2.5])


# In[33]:


cond = np.array([True, False, True, True, False])


# In[35]:


result = [(x if c else y)
          for x,y,c in zip(xarr,yarr,cond)]


# In[36]:


result


# In[37]:


result = np.where(cond, xarr, yarr)


# In[38]:


result


# In[39]:


arr = np.random.randn(4,4)


# In[40]:


arr


# In[41]:


arr > 0


# In[42]:


np.where (arr>0,2,-2)


# In[43]:


np.where(arr>0,2,arr)


# ### 수학 메서드와 통계 메서드

# In[45]:


arr = np.random.randn(5,4)


# In[46]:


arr


# In[47]:


arr.mean()


# In[48]:


np.mean(arr)


# In[49]:


arr.sum()


# In[50]:


arr.mean(axis=1)


# In[51]:


arr.sum(axis=0)


# In[52]:


arr = np.array([0,1,2,3,4,5,6,7])


# In[53]:


arr.cumsum()


# In[54]:


arr = np.array([[0,1,2],[3,4,5],[6,7,8]])


# In[55]:


arr


# In[56]:


arr.cumsum(axis=0)


# In[58]:


arr.cumprod(axis=1)


# ### 불리언 배열을 위한 메서드

# In[59]:


arr = np.random.randn(100)


# In[60]:


(arr>0).sum()


# In[61]:


bools = np.array([False, False, True, False])


# In[62]:


bools.any()


# In[63]:


bools.all()


# ### 정렬

# In[64]:


arr = np.random.randn(6)


# In[65]:


arr


# In[66]:


arr.sort()


# In[67]:


arr


# In[69]:


arr = np.random.randn(5,3)


# In[70]:


arr


# In[71]:


arr.sort(1)


# In[72]:


arr


# In[73]:


large_arr = np.random.randn(1000)


# In[74]:


large_arr.sort()


# In[75]:


large_arr[int(0.05*len(large_arr))] #5%분위수


# ### 집합 관련 함수

# In[76]:


names = np.array(['Bob','Joe','Will','Bob','Will','Joe','Joe'])


# In[77]:


np.unique(names)


# In[78]:


ints = np.array([3,3,3,2,2,1,1,4,4])


# In[79]:


np.unique(ints)


# In[80]:


sorted(set(names))


# In[81]:


values = np.array([6,0,0,3,2,5,6])


# In[82]:


np.in1d(values,[2,3,6])


# In[ ]:




