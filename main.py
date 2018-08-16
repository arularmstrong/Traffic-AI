
# coding: utf-8

# In[ ]:


from fbprophet import Prophet
import pandas as pd
import numpy as np
from stockstats import StockDataFrame as sdf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


# In[ ]:


dataSet=pd.read_csv('./data/train.csv')
dataSet=dataSet.rename(columns={'Date':'ds','Close**':'y'})
prophetData=sdf.retype(dataSet)
prophet=prophetData.loc[:,['ds','y']]


# In[ ]:


model=Prophet(yearly_seasonality=False, daily_seasonality=False)
model.fit(prophet)

def predictor(currentDate):
    dateFormat = "%Y-%m-%d"
    dateFix = datetime.strptime('2018-08-14', dateFormat)
    period = currentDate - dateFix
    future = model.make_future_dataframe(periods=period.days)
    forecast = model.predict(future)
    prediction=forecast[['ds','yhat']].tail()
    value=prediction.iloc[4]['yhat']
    return value


# In[ ]:


initMoney=6350
MONEY=initMoney
valueList=[]
for i in range(7):
    value=predictor(datetime.today() + timedelta(days=i))
    valueList.append(value)
    print(valueList)
day=valueList.index(min(valueList))
investDate=datetime.today() + timedelta(days=day)
print("invest on "+ str(investDate))
initMoney=MONEY-min(valueList)
print(initMoney)
i=1
valueList=[]
gain=0
while True:
    value=predictor(investDate + timedelta(days=i))
    print(value)
    valueList.append(value)
    if(value>MONEY):
        bounty=max(valueList)
        day=valueList.index(max(valueList))
        gain+=bounty-MONEY
        print(str(gain)+ " earned")
        initMoney=MONEY
        print("trade on "+ str(investDate + timedelta(days=day+1)))
    i+=1

