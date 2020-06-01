from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
import pickle
from scipy import sparse
import numpy as np
import pandas as pd

data=pd.read_csv("C:\\Users\\DELL-7000\\Desktop\\论文\\卷积神经网络\\一维卷积神经网络故障分类预测\\数据预处理\\wavelet2.csv")
data=np.array(data)
x=data[:,0:-7]
y=data[:,-7]
                   
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=22)
scaler=StandardScaler(with_mean=False)
x_train=scaler.fit_transform(x_train)
x_test=scaler.transform(x_test)

estimator = RandomForestClassifier()

param_dict = {"n_estimators":[50,120,200,300,500], "max_depth":[1,2,3,4,5,8,13,20,30,40,50,60]}
estimator=GridSearchCV(estimator,param_grid=param_dict,cv=10)
estimator.fit(x_train,y_train)

y_predict=estimator.predict(x_test)
print("y_predict:\n",y_predict)
print("直接比对真实值和预测值:\n",y_test==y_predict)

score=estimator.score(x_test,y_test)
print("准确率为：\n",score)

print("最佳参数：\n",estimator.best_params_)
print("最佳结果：\n",estimator.best_score_)
print("最佳估计器：\n",estimator.best_estimator_)
print("交叉验证结果：\n",estimator.cv_results_)
