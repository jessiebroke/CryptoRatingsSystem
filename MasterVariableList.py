
# coding: utf-8

# In[1]:


import requests
import pandas as pd
import numpy as np
import json
import ijson
from CMCAPIRequestsPandas import *
from GHAPIRequests import *


# In[2]:


#Defining all variables for use by CMC API
#https://api.coinmarketcap.com/v1/ticker/

cmcid = "id"; #all lower-case name of crypto
cmcname = "name"; #case-sensitive name of crypto
cmcsymbol = "symbol"; #ticker symbol of crypto
cmcrank= "rank"; #rank by largest Market Cap
cmcpriceusd = "price_usd" #price in USD
cmcpricebtc = "price_btc" #price in BTC
cmcdailyvol = "24h_volume_usd" #daily volume in USD
cmcmarketcap = "market_cap_usd" #total market cap
cmcavailsupp = "available_supply" #total available supply in current circulation
cmctotalsupp = "total_supply" #total available supply currently
cmcmaxsupp = "max_supply" #maximum possibly supply circulation
cmchourchg = "percent_change_1h" #1 hour percent change
cmcdailychg = "percent_change_24h" #24 hour percent change
cmcweeklychg = "percent_change_7d" #1 week percent change
cmclastupdate = "last_updated" #not sure yet

#Defining all variables for use by GitHub API
#https://api.github.com/repos/bitcoin/bitcoin

ghid = "id"
ghname = "name"
ghrelease = "pushed_at"
ghstars = "stargazers_count"
ghforks = "forks_count"
ghlanguage = "language"
ghopenissues = "open_issues_count"
ghsubcount = "subscribers_count"


# In[3]:


#Makes call to CMCAPIRequests to return row data as well as the specific value.
callcmcapi("bitcoin", cmcpriceusd)


# In[4]:


#Makes call to GHAPIRequests to return Series data as well as specific value.
callghapi("bitcoin", ghname)

