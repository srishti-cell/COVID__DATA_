#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotly.subplots import make_subplots
from datetime import datetime


# In[2]:


covid_df = pd.read_csv('raw_data.csv')


# In[3]:


covid_df.head(10)


# In[4]:


covid_df.info()


# In[5]:


covid_df.describe()


# In[7]:


covid_df.count()


# In[10]:


covid_df.isnull().sum()


# In[12]:


sns.heatmap(covid_df.isnull())
plt.show()


# In[14]:


covid_df.groupby('location').sum()


# In[17]:


covid_df.groupby('location')['total_cases'].sum().sort_values(ascending= False)


# In[18]:


covid_df.groupby('location')['total_cases','total_deaths'].sum()


# In[23]:


3covid_df[covid_df.total_cases < 10]


# In[25]:


# in which region max no. of cases confirmed
covid_df.groupby('location').total_cases.sum().sort_values(ascending = False).head(27)


# In[28]:


# in whuc region mini no. of deaths
covid_df.groupby('location').total_deaths.sum().sort_values(ascending = True).head(67)


# In[31]:


# how many confirmed, deaths & recovered cases
covid_df[covid_df.location == 'India']


# In[32]:


covid_df[covid_df.location == 'United States']


# In[33]:


covid_df.sort_values(by = ['total_cases'],ascending = True).head(50)


# In[36]:


covid_df.sort_values(by = ['human_development_index'] , ascending = False)


# In[ ]:




