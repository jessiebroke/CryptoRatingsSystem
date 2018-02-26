
# coding: utf-8

# In[207]:


#API Requests to Coinmarketcap


# In[208]:


import requests
import pandas as pd
import numpy as np
import json
import ijson


# In[209]:


# Make a get request to get the latest position of the international space station from the opennotify api.
#response = requests.get("https://api.coinmarketcap.com/v1/ticker/")

# Print the status code of the response.
#print(response.status_code)


# In[210]:


# Find content data type from CMC
#print(type(response.content))

# Data type is "bytes" in the form of a list with different categories
#data = response.json()

# Format object data into data type "string"
#data_json = json.dumps(data)

# Verify data type is "string"
#print(type(data_json))

# Print JSON string formatted data
#print(data_json)

#prints all information in data
#print(data)


# In[211]:


#tokens = pd.Series(data)
#list(tokens)
tokens = pd.read_json(data_json)

tokens.index = tokens["id"]
    
    #tokens['id']
    #list(tokens)
    #list(tokens.columns.values)


# In[212]:


#tokens.loc["bitcoin","total_supply"]

def callcmcapi(tokenname, column):
    
    response = requests.get("https://api.coinmarketcap.com/v1/ticker/")
    
    data = response.json()
    
    tokens = pd.read_json(data_json)

    tokens.index = tokens["id"]
    
    #cmcrowdata = tokens.loc[tokenname]
    
    cmcvalue = tokens.loc[tokenname, column]
        
    return cmcvalue;

#use a dict


# In[213]:


#callcmcapi("bitcoin","max_supply")

