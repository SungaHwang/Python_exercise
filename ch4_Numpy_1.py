#!/usr/bin/env python
# coding: utf-8

# # 4.1 Numpy ndarray: 다차원 배열 객체

# In[6]:


import numpy as np


# In[2]:


data = np.random.randn(2, 3)


# In[3]:


data


# In[4]:


data * 10


# In[5]:


data + data


# ### ndarray 생성하기

# In[7]:


data1 = [6,7.5,8,0,1]


# In[8]:


arr1 = np.array(data1)


# In[9]:


arr1


# In[11]:


data2 = [[1,2,3,4],[5,6,7,8]]


# In[12]:


arr2 = np.array(data2)


# In[13]:


arr2


# In[14]:


arr2.ndim


# In[15]:


arr2.shape


# In[16]:


arr1.dtype


# In[17]:


arr2.dtype


# In[18]:


np.zeros(10)


# In[19]:


np.zeros((3, 6))


# In[20]:


np.zeros((2,3,2))


# In[21]:


np.arange(15)


# ### ndarray의 dtype

# In[22]:


arr1 = np.array([1,2,3],dtype=np.float64)


# In[23]:


arr2 = np.array([1,2,3],dtype=np.int32)


# In[24]:


arr1.dtype


# In[25]:


arr2.dtype


# In[26]:


arr = np.array([1,2,3,4,5])


# In[27]:


arr.dtype


# In[28]:


float_arr = arr.astype(np.float64)


# In[29]:


float_arr.dtype


# In[52]:


arr = np.array([3.7,-1.2,-2.6,0.5,12.9,10.1])


# In[31]:


arr


# In[32]:


arr.astype(np.int32)


# In[33]:


numeric_strings =np.array(['1.25','-9.6','42'],dtype=np.string_)


# In[34]:


numeric_strings.astype(float)


# In[35]:


int_array = np.arange(10)


# In[37]:


calibers = np.array([.22, .270, .357, .380, .44, .50], dtype=np.float64)


# In[38]:


int_array.astype(calibers.dtype)


# In[39]:


empty_unit32 = np.empty(8, dtype='u4')


# In[40]:


empty_unit32


# ### NumPy 배열의 산술 연산

# In[56]:


arr = np.array([[1.,2.,3.],[4.,5.,6.]])


# In[57]:


arr


# In[43]:


arr*arr


# In[44]:


arr -arr


# In[46]:


1/arr


# In[47]:


arr **0.5


# In[58]:


arr2 = np.array([[0.,4., 1.],[7.,2.,12.]])


# In[59]:


arr2


# In[60]:


arr2 > arr


# ### 색인과 슬라이싱 기초

# In[61]:


arr = np.arange(10)


# In[62]:


arr


# In[63]:


arr[5]


# In[64]:


arr[5:8]


# In[65]:


arr[5:8] = 12


# In[66]:


arr


# In[67]:


arr_slice = arr[5:8]


# In[68]:


arr_slice


# In[69]:


arr_slice[1] = 12345


# In[70]:


arr


# In[71]:


arr_slice[:] =64


# In[72]:


arr


# In[73]:


arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])


# In[74]:


arr2d[2]


# In[75]:


arr2d[0][2]


# In[76]:


arr2d[0,2]


# In[79]:


arr3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])


# In[80]:


arr3d


# In[81]:


arr3d[0]


# In[82]:


old_values = arr3d[0].copy()


# In[83]:


arr3d[0] = 42


# In[84]:


arr3d


# In[85]:


arr3d[0] = old_values


# In[86]:


arr3d


# In[87]:


arr3d[1,0]


# In[88]:


x= arr3d[1]


# In[89]:


x


# In[90]:


x[0]


# In[91]:


arr


# In[92]:


arr[1:6]


# In[93]:


arr2d


# In[94]:


arr2d[:2]


# In[95]:


arr2d[:2, 1:]


# In[96]:


arr2d[1,:2]


# In[97]:


arr2d[:2,2]


# In[98]:


arr2d[:,:1]


# In[99]:


arr2d[:2,1:]=0


# In[100]:


arr2d


# ### 불리언값으로 선택하기

# In[102]:


names = np.array(['Bob','Joe','Will','Bob','Will','Joe','Joe'])


# In[103]:


data = np.random.randn(7,4)


# In[104]:


names


# In[105]:


data


# In[106]:


names == 'Bob'


# In[107]:


data[names == 'Bob']


# In[108]:


data[names == 'Bob', 2:]


# In[109]:


data[names == 'Bob', 3]


# In[110]:


names != 'Bob'


# In[111]:


data[~(names == 'Bob')]


# In[112]:


cond =names == 'Bob'


# In[113]:


data[~cond]


# In[114]:


mask = (names=='Bob')|(names == 'Will')


# In[115]:


mask


# In[116]:


data[mask]


# In[117]:


data[data<0] =0


# In[118]:


data


# In[119]:


data[names != 'Joe']=7


# In[120]:


data


# ### 팬시 색인

# In[121]:


arr = np.empty((8,4))


# In[122]:


for i in range(8):
    arr[i]=i


# In[123]:


arr


# In[124]:


arr[[4,3,0,6]]


# In[125]:


arr[[-3, -5, -7]]


# In[126]:


arr = np.arange(32).reshape((8,4))


# In[127]:


arr


# In[128]:


arr[[1,5,7,2],[0,3,1,2]]


# In[129]:


arr[[1,5,7,2]][:,[0,3,1,2]]


# ### 배열 전치와 축 바꾸기

# In[130]:


arr = np.arange(15).reshape((3,5))


# In[131]:


arr


# In[132]:


arr.T


# In[133]:


arr = np.random.randn(6,3)


# In[134]:


arr


# In[135]:


np.dot(arr.T,arr)


# In[136]:


arr = np.arange(16).reshape((2,2,4))


# In[137]:


arr


# In[138]:


arr.transpose((1,0,2))


# In[139]:


arr


# In[140]:


arr.swapaxes(1,2)


# In[ ]:




