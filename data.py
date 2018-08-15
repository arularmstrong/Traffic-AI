
# coding: utf-8

# In[1]:


import pandas as pd
import datetime


# In[2]:


currentDate=datetime.datetime.now().strftime ("%Y%m%d")
dataUrl="https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20170101&end="+currentDate
data=pd.read_html(dataUrl,header=None)
dataSet=data[0].loc[:, ~data[0].columns.str.contains('^Unnamed')]
print(dataSet)
dataSet.to_csv('./data/train.csv', encoding='utf-8', index=False)

