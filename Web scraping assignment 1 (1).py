#!/usr/bin/env python
# coding: utf-8

# In[3]:


from bs4 import BeautifulSoup


# In[4]:


pip install requests


# In[5]:


import requests


# In[13]:


url=("https://www.icc-cricket.com/rankings/mens/player-rankings/odi")


# In[14]:


response=requests.get(url)


# In[15]:


response


# In[16]:


soup=BeautifulSoup(response.text)


# In[17]:


soup


# In[18]:


name=soup.select(".name a")


# In[19]:


name


# In[20]:


team=soup.select(".nationality-logo")


# In[21]:


team


# In[38]:


rating=soup.select(".rating")


# In[39]:


rating


# In[40]:


import pandas


# In[41]:


cricketplayers=pandas.DataFrame(name,columns=["name"])


# In[42]:


cricketplayers


# In[50]:


cricketplayers["rating"]=rating


# In[48]:


cricketplayers["team"]=team


# In[49]:


cricketplayers


# In[53]:


cricketplayers.to_csv("C:\\Users\\aedpu\\OneDrive\\Documents\\Jayapriyan.csv")


# In[ ]:




