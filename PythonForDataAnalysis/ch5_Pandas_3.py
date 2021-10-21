#!/usr/bin/env python
# coding: utf-8

# ## 5.3 기술 통계 계산과 요약

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[3]:


df= pd.DataFrame([[1.4, np.nan],[7.1,-4.5],
                [np.nan, np.nan],[0.75, -1.3]],
                 index=['a','b','c','d'],
                 columns=['one','two'])
df


# In[4]:


df.sum()


# In[5]:


df.sum(axis='columns')


# In[7]:


df.mean(axis='columns',skipna=False)


# In[8]:


df.idxmax()


# In[9]:


df.cumsum()


# In[10]:


df.describe()


# In[11]:


obj= pd.Series(['a','a','b','c']* 4)


# In[12]:


obj.describe()


# ### 상관관계와 공분산

# In[13]:


conda install pandas-datareader


# In[14]:


import pandas_datareader.data as web


# In[15]:


all_data = {ticker: web.get_data_yahoo(ticker)
           for ticker in ['AAPL','IBM','MSFT','GOOG']}
price = pd.DataFrame({ticker: data['Adj Close']
                     for ticker, data in all_data.items()})
volume= pd.DataFrame({ticker: data['Volume']
                     for ticker, data in all_data.items()})


# In[16]:


returns = price.pct_change()
returns.tail()


# In[17]:


returns['MSFT'].corr(returns['IBM'])


# In[18]:


returns['MSFT'].cov(returns['IBM'])


# In[20]:


returns.corr()


# In[21]:


returns.cov()


# In[22]:


returns.corrwith(returns.IBM)


# In[23]:


returns.corrwith(volume)


# ### 유일값, 값 세기, 맴버십

# In[24]:


obj= pd.Series(['c','a','d','a','a','b','b','c','c'])


# In[25]:


uniques = obj.unique()


# In[26]:


uniques


# In[27]:


obj.value_counts()


# In[28]:


pd.value_counts(obj.values,sort=False)


# In[29]:


obj


# In[30]:


mask = obj.isin(['b','c'])
mask


# In[31]:


obj[mask]


# In[32]:


to_match=pd.Series(['c','a','b','b','c','a'])


# In[33]:


unique_vals = pd.Series(['c','b','a'])


# In[35]:


data=pd.DataFrame({'Qu1': [1,3,4,3,4],
                  'Qu2': [2,3,1,2,3],
                  'Qu3': [1,5,2,4,4]})
data


# In[36]:


result = data.apply(pd.value_counts).fillna(0)
result

