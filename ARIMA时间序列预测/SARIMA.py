import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import tushare as ts
import datetime
from statsmodels.graphics.api import qqplot
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima_model import ARIMA
import statsmodels.api as sm
import statsmodels.tsa.stattools as st
from itertools import product

data=pd.read_excel('无线市场空间data.xlsx')
data=data['3G亚太规模']
data=data[8:]
data=pd.Series(data)
data.index = pd.Index(pd.date_range(start = '2001-1-1', end = '2019-12-1', freq = 'QS-JAN'))

data_log=np.log(data)
"""data_log_diff1=data_log.diff(1)
data_log_diff1_new=data_log_diff1.dropna(inplace=True)
data_log_diff1_4=data_log_diff1-data_log_diff1.shift(4)
data_log_diff1_4_new=data_log_diff1_4.dropna()

fig=plt.figure(figsize=(12,8))
ax=fig.add_subplot(111)
data_log_diff1_4_new.plot(ax=ax)

plot_acf(data_log_diff1_4_new, lags=30)
plot_pacf(data_log_diff1_4_new, lags=30)
plt.show()"""

ps=range(2,7)
d=1
qs=range(0,5)
Ps=range(0,2)
D=1
Qs=range(0,2)
s=4

parameters=product(ps, qs, Ps, Qs)
parameters_list=list(parameters)

def optimizeSARIMA(parameters_list, d, D, s):
    results = []
    best_aic = float("inf")
    for param in parameters_list:
        try:
            model = sm.tsa.statespace.SARIMAX(data, order=(param[0], param[1], param[2]), seasonal_order=(param[2], D, param[3], s)).fit(disp=-1)
        except:
            continue
        aic = model.aic
        if aic < best_aic:
            best_model = model
            best_aic = aic
            best_param = param
        results.append([param, model.aic])
    result_table = pd.DataFrame(results)
    result_table.columns = ['parameters', 'aic']
    result_table = result_table.sort_values(by='aic', ascending=True).reset_index(drop=True)

    return result_table

result_table = optimizeSARIMA(parameters_list, d, D, s)
  
p, q, P, Q = result_table.parameters[0]

model=sm.tsa.statespace.SARIMAX(data, order=(p, d, q), seasonal_order=(P, D, Q, s)).fit(disp=-1)

resid = model.resid
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111)
fig = qqplot(resid, line='q', ax=ax, fit=True)
plt.show()

predict_sarima = model.predict(start=0, end=85)
#predict_sarima = np.power(np.e, predict_sarima)
plt.figure(figsize=(24,8))
orig = plt.plot(data, color = 'blue', label = 'Original')
predict = plt.plot(predict_sarima, color = 'red', label = 'Predict')
plt.legend(loc='best')
plt.show()
