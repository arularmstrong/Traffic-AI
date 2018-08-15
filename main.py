
# coding: utf-8

# In[82]:


from fbprophet import Prophet
import pandas as pd
import numpy as np
from stockstats import StockDataFrame as sdf
import matplotlib.pyplot as plt


# In[121]:


dataSet=pd.read_csv('./data/train.csv')
dataSet=dataSet.rename(columns={'Date':'ds','Close**':'y'})
prophetData=sdf.retype(dataSet)
prophetData.head()


# In[122]:


prophet=prophetData.loc[:,['ds','y']]
prophet.head()


# In[123]:


model=Prophet(yearly_seasonality=False, daily_seasonality=False)
model.fit(prophet)


# In[124]:


future = model.make_future_dataframe(periods=2)
future.tail()


# In[125]:


forecast = model.predict(future)
prediction=forecast[['ds','yhat']].tail()
value=prediction.iloc[4]['yhat']
forecast[['ds','yhat']].tail()

