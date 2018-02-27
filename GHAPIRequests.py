
# coding: utf-8

# In[ ]:


import requests
import pandas as pd
import numpy as np
import json
import ijson


# In[ ]:


#r = requests.get('https://api.github.com/repos/bitcoin/bitcoin')
#print(response.status_code)
#www.restapitutorial.com/httpstatuscodes.html
#print(type(response.content))
#print(response.content)


# In[ ]:


#read request data as type 'dict' into variable called data
#data = r.json()


# In[ ]:


#convert 'dict' information in variable data to datatype 'Series'
#github = pd.Series(data)


# In[ ]:



#Current GitHub release version date
#githubrelease = github.loc["pushed_at"]
#print("GitHub Release:",githubrelease)


# In[ ]:


#Current GitHub star
#githubstars = github.loc["stargazers_count"]
#print("GitHub Stars:",githubstars)


# In[ ]:


def callghapi(token_repository, parameter_name):
    #Expand dictionary of GitHub respositories for all crypto and reference specific URL by token_repository param
    response = requests.get('https://api.github.com/repos/bitcoin/bitcoin')
    data = response.json()
    data_s = pd.Series(data)
    return data_s.loc[parameter_name]

