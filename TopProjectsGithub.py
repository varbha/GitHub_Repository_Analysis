
# coding: utf-8

# # An analysis of the most popular repos on Github
# <img src="https://kanbanize.com/blog/wp-content/uploads/2014/11/GitHub.jpg" alt="github">
# _Areas of focus include: Type of repo, Size, Metrics of popularity, Languages used, Level of activity_
# <hr>
# _Data Source: https://www.kaggle.com/chasewillden/topstarredopensourceprojects _
# 

# In[1]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[4]:

git_df = pd.read_csv("topstarredopensourceprojects/TopStaredRepositories.csv")
git_df.head()


# In[17]:

git_df.info()


# ### 1. Popular Repositories
# **Determining what constitutes a popular repository by extracting the range of maximum and minimum starred repositories**

# In[10]:

git_df_max = git_df['Number of Stars'].str.contains('k').all()
git_df_max


# In[27]:

git_df['Number of Stars']=git_df['Number of Stars'].str.replace('k','').astype(float)


# In[28]:

git_df.head()


# In[45]:

max_stars=git_df['Number of Stars'].max()
min_stars=git_df['Number of Stars'].min()
mean_stars= git_df['Number of Stars'].mean()
print(max_stars,min_stars, mean_stars)


# In[47]:

popular_repos= git_df[git_df['Number of Stars'] > 51.0]


# In[52]:

popular_repos.head(13)


# In[ ]:



