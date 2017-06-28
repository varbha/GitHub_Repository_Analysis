
# coding: utf-8

# 
# 
# <h1 style="font-size:30px;color:black;text-align:center">                   An analysis of the most popular repos on Github[incomplete]</h1>
# <img src="https://kanbanize.com/blog/wp-content/uploads/2014/11/GitHub.jpg" alt="github" width=50% height=50%>
# <hr>
# _Areas of focus include: Type of repo, Size, Metrics of popularity, Languages used, Level of activity_
# 
# _Data Source: https://www.kaggle.com/chasewillden/topstarredopensourceprojects _
# 

# In[224]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('default')


# In[225]:

git_df = pd.read_csv("topstarredopensourceprojects/TopStaredRepositories.csv", parse_dates=['Last Update Date'], dayfirst=True)
git_df.head()


# In[226]:

git_df.info()


# ### 1. Popular Repositories
# **Determining what constitutes a popular repository by extracting the range of maximum and minimum starred repositories**

# In[227]:

git_df_max = git_df['Number of Stars'].str.contains('k').all()
git_df_max


# In[228]:

git_df['Number of Stars']=git_df['Number of Stars'].str.replace('k','').astype(float)


# In[229]:

git_df.head()


# In[230]:

git_df.tail()


# In[231]:

max_stars=git_df['Number of Stars'].max()
min_stars=git_df['Number of Stars'].min()
mean_stars= git_df['Number of Stars'].mean()
print(max_stars,min_stars, mean_stars)


# #### Most popular repo- 290,000 stars
# #### Least popular repo- 6400 stars
# #### Average rating of repos- 13,000 stars

# In[232]:

popular_repos= git_df[git_df['Number of Stars'] > 51.0]


# In[233]:

popular_repos.head(13)


# ### Here we see that freeCodeCamp tops the list with 290,000 stars to its repository.
# <hr>
# ### The above list lists all repos that have > 51,000 stars
# #### A few more observations can be derived from this list:
# <ol>
# <li>5 of the most popular repos are frameworks</li>
# <li>The third, fifth and seventh most popular repos are educational, and instructive in nature.</li>
# <li>JavaScript is the major code in most of the most popular repos</li>
# <li>Most frameworks listed are for web-based development, highlighting the importance of this sector</li>

# In[245]:

x=git_df['Language'].value_counts()
x.head()


# In[279]:

get_ipython().magic('matplotlib inline')
plt.figure()
x.plot(kind='barh',figsize=(15,10),grid=True, label='Number of repositories',legend='No of repos',title='No of repositories vs language used')


# In[294]:

get_ipython().magic('matplotlib inline')
x[:5].plot.pie(label="Use of the top 5 languages",fontsize=20,figsize=(10,10))


# In[ ]:



