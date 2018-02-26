
# coding: utf-8

# In[29]:


import requests
import pandas as pd
import numpy as np
import json
import ijson
from CMCAPIRequests import *


# In[30]:


#Defining all variables for use by CMC

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


# In[31]:


dfreturn = 0;

dfreturn = callcmcapi("bitcoin", "max_supply")

