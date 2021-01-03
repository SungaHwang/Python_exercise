#!/usr/bin/env python
# coding: utf-8

# ## 5.2 핵심 기능

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# ### 재색인

# In[3]:


obj= pd. Series([4.5, 7.2, -5.3, 3.6], index= ['d','b','a','c'])
obj


# In[4]:


obj2= obj.reindex(['a','b','c','d','e'])
obj2


# In[5]:


obj3= pd.Series(['blue','purple','yellow'], index=[0,2,4])
obj3


# In[6]:


obj3.reindex(range(6),method='ffill')


# In[7]:


frame= pd.DataFrame(np.arange(9).reshape((3,3)),
                   index=['a','c','d'],
                   columns=['Ohio','Texas','California'])
frame


# In[8]:


frame2 =frame.reindex(['a','b','c','d'])
frame2


# In[9]:


states = ['Texas','Utah','California']


# In[10]:


frame.reindex(columns=states)


# ### 하나의 로우나 칼럼 삭제하기

# In[12]:


obj= pd.Series(np.arange(5.),index=['a','b','c','d','e'])
obj


# In[14]:


new_obj= obj.drop('c')
new_obj


# In[15]:


obj.drop(['d','c'])


# In[16]:


data= pd.DataFrame(np.arange(16).reshape((4,4)),
                  index=['Ohio','Colorado','Utah','New York'],
                  columns=['one','two','three','four'])
data


# In[17]:


data.drop(['Colorado','Ohio'])


# In[18]:


data.drop('two',axis=1)


# In[20]:


data.drop(['two','four'],axis='columns')


# ### 색인하기, 선택하기, 거르기

# In[21]:


obj= pd.Series(np.arange(4.),index=['a','b','c','d'])
obj


# In[23]:


obj['b']


# In[25]:


obj[1]


# In[26]:


obj[2:4]


# In[27]:


obj[['b','a','d']]


# In[28]:


obj[[1,3]]


# In[29]:


obj[obj<2]


# In[30]:


obj['b':'c']


# ### 정수 색인

# In[32]:


ser=pd.Series(np.arange(3.))
ser


# In[33]:


ser2=pd.Series(np.arange(3.),index=['a','b','c'])
ser2[-1]


# In[34]:


ser[:1]


# In[35]:


ser.loc[:1]


# In[36]:


ser.iloc[:1]


# ### 산술 연산과 데이터 정렬

# In[37]:


s1= pd.Series([7.3,-2.5,3.4,1.5], index=['a','c','d','e'])


# In[38]:


s2= pd.Series([-2.1,3.6,-1.5,4,3.1],index=['a','c','e','f','g'])


# In[41]:


s1


# In[40]:


s2


# In[42]:


s1+s2


# In[45]:


arr= np.arange(12.).reshape((3,4))
arr


# In[46]:


arr[0]


# In[47]:


arr-arr[0]


# In[48]:


frame=pd.DataFrame(np.arange(12.).reshape((4,3)),
                  columns=list('bde'),
                  index=['Utah','Ohio','Texas','Oregon'])


# In[51]:


series= frame.iloc[0]


# In[52]:


frame


# In[53]:


frame - series


# In[55]:


series2= pd.Series(range(3), index=['b','e','f'])


# In[56]:


frame+series2


# In[58]:


series3 =frame['d']


# In[59]:


frame


# In[60]:


series3


# In[61]:


frame.sub(series3, axis='index')


# ### 함수 적용과 매핑

# In[62]:


frame = pd.DataFrame(np.random.randn(4,3),columns=list('bcd'),
                    index=['Utah','Ohio','Texas','Oregon'])
frame


# In[63]:


np.abs(frame)


# ### 정렬과 순위

# In[67]:


obj = pd.Series(range(4),index=['d','a','b','c'])


# In[68]:


obj.sort_index()


# In[69]:


frame= pd.DataFrame(np.arange(8).reshape((2,4)),
                   index=['three','one'],
                   columns=['d','a','b','c'])


# In[70]:


frame.sort_index()


# In[71]:


frame.sort_index(axis=1)


# In[72]:


frame.sort_index(axis=1,ascending=False)


# In[73]:


obj= pd.Series([4,7,-3,2])


# In[74]:


obj.sort_values()


# In[75]:


obj=pd.Series([4,np.nan,7,np.nan,-3,2])


# In[76]:


obj.sort_values()


# In[77]:


frame=pd.DataFrame({'b':[4,7,-3,2], 'a':[0,1,0,1]})
frame


# In[78]:


frame.sort_values(by='b')


# In[80]:


obj=pd.Series([7,-5,7,4,2,0,4])


# In[81]:


obj.rank()


# In[82]:


obj.rank(method='first')


# In[83]:


obj.rank(ascending=False, method='max')


# In[84]:


frame=pd.DataFrame({'b':[4.3,7,-3,2],'a':[0,1,0,1],
                   'c':[-2,5,8,-2.5]})
frame


# In[85]:


frame.rank(axis='columns')


# ### 중복 색인

# In[86]:


obj=pd.Series(range(5), index=['a','a','b','b','c'])
obj


# In[88]:


obj.index.is_unique


# In[89]:


obj['a']


# In[90]:


df=pd.DataFrame(np.random.randn(4,3), index=['a','a','b','b'])
df


# In[91]:


df.loc['b']

