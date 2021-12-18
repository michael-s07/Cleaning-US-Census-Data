#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import codecademylib3_seaborn
import glob


# In[2]:


file = glob.glob('states*.csv')


# In[3]:


df_list = []
for filename in file:
    data= pd.read_csv(filename)
    df_list.append(data)
df=pd.concat(df_list)
print(df.head())


# In[4]:


df.head()


# In[5]:


df.columns


# In[6]:


df.dtypes


# In[7]:


df.Hispanic = df.Hispanic.str.replace('\D+','', regex=True)
df.White = df.White.str.replace('\D+','', regex=True)
df.Black = df.Black.str.replace('\D+','', regex=True)
df.Native = df.Native.str.replace('\D+','', regex=True)
df.Asian = df.Asian.str.replace('\D+','', regex=True)
df.Pacific = df.Pacific.str.replace('\D+','', regex=True)
df.Income = df.Income.str.replace('\D+','', regex=True)


# In[8]:


df.Hispanic = pd.to_numeric(df.Hispanic)
df.White = pd.to_numeric(df.White)
df.Black = pd.to_numeric(df.Black)
df.Native = pd.to_numeric(df.Native)
df.Asian = pd.to_numeric(df.Asian)
df.Pacific = pd.to_numeric(df.Pacific)
df.Income = pd.to_numeric(df.Income)


# In[9]:


data_split = df.GenderPop.str.split('_')


# In[10]:


df['Men_population']=data_split.str.get(0)
df['Women_population']=data_split.str.get(1)
df.Men_population = df.Men_population.str.replace('M','')
df.Women_population = df.Women_population.str.replace('F','')


# In[11]:


df.Men_population = pd.to_numeric(df.Men_population)
df.Women_population = pd.to_numeric(df.Women_population)


# In[12]:


df.dtypes


# In[13]:


plt.scatter(df.Women_population, df.Income)
plt.xlabel('Income')
plt.ylabel('Women')
plt.show()


# In[14]:


df.Women_population=df.Women_population.fillna(df.TotalPop - df.Men_population)


# In[15]:


df.Women_population


# In[16]:


df.drop_duplicates()


# In[17]:


plt.scatter(df.Women_population, df.Income)
plt.show()


# In[18]:


df.columns


# In[19]:


plt.hist(df.Hispanic)
plt.show()
plt.hist(df.White)
plt.show()
plt.hist(df.Black)
plt.show()
plt.hist(df.Native)
plt.show()
plt.hist(df.Asian)
plt.show()
plt.hist(df.Pacific)
plt.show()


# In[ ]:




