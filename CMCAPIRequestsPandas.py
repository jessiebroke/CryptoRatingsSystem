
# coding: utf-8

# In[86]:


#API Requests to Coinmarketcap


# In[87]:


import requests
import pandas as pd
import numpy as np
import json
import ijson


# In[88]:


# Make a get request to get the latest position of the international space station from the opennotify api.
#response = requests.get("https://api.coinmarketcap.com/v1/ticker/")

# Find content data type from CMC
#print(type(response.content))

# Print the status code of the response.
#print(response.status_code)


# In[89]:


# Data type is "bytes" in the form of a list with different categories
#data = response.json()

# Format object data into data type "string"
#data_json = json.dumps(data)

# Verify data type is "string"
#print(type(data_json))

# Print JSON string formatted data
#print(data_json)


# In[90]:


def callcmcapi(token_name, column_name):
    response = requests.get('https://api.coinmarketcap.com/v1/ticker/')
    data_p = pd.read_json(response.text)
    data_p = data_p.set_index('id')
    return data_p.loc[[token_name]][[column_name]]
        #return data_p.loc[token_name][column_name]

