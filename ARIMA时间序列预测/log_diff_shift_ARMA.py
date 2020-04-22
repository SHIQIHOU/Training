import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import tushare as ts
import datetime
from statsmodels.graphics.api import qqplot
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima_model import ARMA
import statsmodels.api as sm
import statsmodels.tsa.stattools as st
from itertools import product

data=pd.read_excel('无线市场空间data.xlsx')
data=data['亚太整体规模']
data=data[8:]
data=pd.Series(data)
data.index = pd.Index(pd.date_range(start = '2001-1-1', end = '2019-12-1', freq = 'QS-JAN'))

data_log=np.log(data)
data_log_diff1=data_log.diff(1)
data_log_diff1_new=data_log_diff1.dropna(inplace=True)
data_log_diff1_4=data_log_diff1-data_log_diff1.shift(4)
data_log_diff1_4_new=data_log_diff1_4.dropna()

fig=plt.figure(figsize=(12,8))
ax=fig.add_subplot(111)
data_log_diff1_4_new.plot(ax=ax)

plot_acf(data_log_diff1_4_new, lags=30)
plot_pacf(data_log_diff1_4_new, lags=30)
plt.show()

p=range(2,7)
q=range(0,7)
parameters=product(p,q)
parameters_list=list(parameters)

def optimizeARMA(parameters_list):
    results = []
    best_aic = float("inf")
    for param in parameters_list:
        try:
            model = ARMA(data_log_diff1_4_new, (param[0], param[1])).fit()
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

result_table = optimizeARMA(parameters_list)
    
p, q = result_table.parameters[0]

model20=ARMA(data_log_diff1_4_new, (p,q)).fit()

resid = model20.resid
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111)
fig = qqplot(resid, line='q', ax=ax, fit=True)
plt.show()

predict_arma = model20.predict(start=0, end=100)
data_log_diff1_recover_4 = predict_arma.add(data_log_diff1.shift(4))
data_log_recover_diff1 = data_log_diff1_recover_4.add(data_log.shift(1))
data_log_recover_diff1 = data_log_recover_diff1.dropna()
predict_arma = np.power(np.e, data_log_recover_diff1)
plt.figure(figsize=(24,8))
orig = plt.plot(data, color = 'blue', label = 'Original')
predict = plt.plot(predict_arma, color = 'red', label = 'Predict')
plt.legend(loc='best')
plt.show()
