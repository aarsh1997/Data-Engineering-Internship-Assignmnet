#!/usr/bin/env python
# coding: utf-8

# Importing **Pandas** Library

# In[1]:


import pandas as pd


# Importing **HTML Table** into a DataFrame

# In[2]:


dfs = pd.read_html('https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population', header = 0)


# Checking length of **dfs** object

# In[3]:


len(dfs)


# Selecting **List of United States Cities by Population** TABLE

# In[4]:


dfsfull = dfs[4]


# Displaying the **TABLE**

# In[5]:


dfsfull


# Converting **Scraped TABLE** into **CSV** and naming it as **webscrapfull.csv**

# In[6]:


dfsfull.to_csv(r'C:\Users\AARSH\Desktop\Web Scraping' + '\\webscrapfull.csv', index=False)


# Creating **New DataFrame** displaying First 10 rows from **Scraped TABLE**

# In[8]:


dfsnew = pd.DataFrame(dfs[4].head(10))


# Displaying **New TABLE**

# In[9]:


dfsnew


# Generating **Demonym** Variable

# In[10]:


Demonym = ['New Yorker', 'Angeleno', 'Chicagoan', 'Houstonian', 'Phoenician', 'Philadelphian', 'San Antonian', 'San Diegan', 'Dallasite', 'San Josean/Josefino']


# Adding **Demonym** Column to **New TABLE**

# In[12]:


dfsnew['Demonym'] = Demonym


# Displaying **New TABLE** with **Demonym** Column Added

# In[13]:


dfsnew


# Importing **Numpy** Library

# In[14]:


import numpy as np


# Ideally there is no perfect population density, as population density equals to No. of People divided by the Total Land Area which may vary from city to city

# Adding New Column **Density_Check** based on **2016 Population Density**

# In[16]:


dfsnew['Density_Check'] = np.where(dfsnew['2016 population density']>='7000', 'Bad', 'Good')


# Displaying **New TABLE** with **Density_Check** Column Added

# In[17]:


dfsnew


# Converting **New TABLE** into **CSV** and naming it as **webscrapnew.csv**

# In[24]:


dfsnew.to_csv(r'C:\Users\AARSH\Desktop\Web Scraping' + '\\webscrapenew.csv', index=False)


# Importing **Matplot** Library

# In[18]:


import matplotlib.pyplot as plt


# Importing **Seaborn** Library

# In[19]:


import seaborn as sns


# Importing **NLTK** Library

# In[20]:


import nltk


# In[21]:


from nltk.corpus import stopwords


# Importing **webscrapenew** CSV file and storing it in a pandas dataframe **New**

# In[25]:


New = pd.read_csv('webscrapenew.csv')


# Verifying number of rows & columns in the **New** DataFrame

# In[26]:


New.shape


# Plotting **Count Plot** for **2016 Population Density** and **2016 Land Area**

# In[43]:


sns.countplot(y='2016 population density', hue = '2016 land area', data=New)

