#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import csv
bank = pd.read_csv('C:\\Users\\isabe\\Downloads\\bank\\bank.csv', sep = ';')
pd.set_option('display.precision', 2) #format for floating-point values

#creating the graphs
get_ipython().run_line_magic('matplotlib', 'inline')
histogram = bank.hist()


# In[7]:


bank.head()


# In[8]:


bank.tail()


# In[9]:


bank.describe()


# In[10]:


(bank.age >= 30).describe()


# In[15]:


(bank.loan == "no").describe()


# In[17]:


(bank.loan == "yes").describe()


# In[ ]:




