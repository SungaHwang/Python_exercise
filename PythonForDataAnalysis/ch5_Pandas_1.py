#!/usr/bin/env python
# coding: utf-8

# # Pandas

# In[1]:


import pandas as pd


# In[16]:


import numpy as np


# In[2]:


from pandas import Series, DataFrame


# ## 5.1 pandas 자료구조 소개

# ### Series

# In[3]:


obj = pd.Series([4,7,-5,3])


# In[4]:


obj


# In[5]:


obj.values


# In[6]:


obj.index


# In[7]:


obj2 = pd.Series([4,7,-5,3], index=['d','b','a','c'])


# In[8]:


obj2


# In[9]:


obj2.index


# In[10]:


obj2['a']


# In[11]:


obj2['d']=6


# In[12]:


obj2[['c','a','d']]


# In[13]:


obj2[obj2>0]


# In[14]:


obj2*2


# In[17]:


np.exp(obj2)


# In[18]:


'b' in obj2


# In[19]:


'e' in obj2


# In[20]:


sdata = {'Ohio':35000, 'Texas':71000, 'Oregon':16000, 'Utah':5000}


# In[21]:


obj3 = pd.Series(sdata)


# In[22]:


obj3


# In[23]:


states = ['California','Ohio','Oregon','Texas']


# In[24]:


obj4 = pd.Series(sdata, index=states)


# In[25]:


obj4


# In[26]:


pd.isnull(obj4)


# In[27]:


pd.notnull(obj4)


# In[28]:


obj4.isnull()


# In[29]:


obj3 + obj4


# In[30]:


obj4.name = 'population'


# In[31]:


obj4.index.name = 'state'


# In[32]:


obj4


# In[33]:


obj


# In[34]:


obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']


# In[35]:


obj


# ### DataFrame

# In[37]:


data = {'state': ['Ohio','Ohio','Ohio','Nevada','Nevada','Nevada'],
       'year': [2000,2001,2002,2001,2002,2003],
       'pop':[1.5,1.7,3.6,2.4,2.9,3.2]}


# In[38]:


frame = pd.DataFrame(data)


# In[39]:


frame


# In[40]:


frame.head()


# In[42]:


pd.DataFrame(data,columns=['year','state','pop'])


# In[51]:


frame2 =pd.DataFrame(data,columns=['year','state','pop','debt'],
                    index =['one','two','three','four',
                           'five','six'])


# In[52]:


frame2


# In[53]:


frame2.columns


# In[54]:


frame2['state']


# In[59]:


frame2.year


# In[56]:


frame2.loc['three']


# In[57]:


frame2['debt'] =16.5


# In[58]:


frame2


# In[60]:


frame2['debt']=np.arange(6.)


# In[61]:


frame2


# In[62]:


val = pd.Series([-1.2,-1.5,-1.7], index=['two','four','five'])


# In[63]:


frame2['debt']=val


# In[64]:


frame2


# In[65]:


frame2['eastern']=frame.state =='Ohio'


# In[66]:


frame2


# In[67]:


del frame2['eastern']


# In[68]:


frame2.columns


# In[69]:


pop = {'Nevada': {2001: 2.4, 2002: 2.9},
      'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}


# In[70]:


frame3 = pd.DataFrame(pop)


# In[71]:


frame3


# In[72]:


frame3.T


# In[73]:


pd.DataFrame(pop,index=[2001,2002,2003])


# In[77]:


pdata = {'Ohio':frame3['Ohio'][:-1],
        'Nevada': frame3['Nevada'][:2]}


# In[83]:


pd.DataFrame(pdata)


# In[84]:


frame3.index.name = 'year'; frame3.columns.name = 'state'


# In[85]:


frame3


# In[86]:


frame3.values


# In[87]:


frame2.values


# ### 색인 객체

# In[88]:


obj = pd.Series(range(3),index=['a','b','c'])


# In[89]:


index = obj.index


# In[90]:


index


# In[91]:


index[1:]


# In[93]:


labels = pd.Index(np.arange(3))


# In[94]:


labels


# In[95]:


obj2 = pd.Series([1.5,-2.5,0], index=labels)


# In[96]:


obj2


# In[97]:


obj2.index is labels


# In[98]:


frame3


# In[99]:


frame3.columns


# In[100]:


'Ohio' in frame3.columns


# In[101]:


2003 in frame3.index


# In[102]:


dup_labels = pd.Index(['foo','foo','bar','bar'])


# In[103]:


dup_labels

