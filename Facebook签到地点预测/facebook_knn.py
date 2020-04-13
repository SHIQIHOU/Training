from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
import pandas as pd


def facebook_knn():
    """
    KNN算法预测Facebook用户的签到地点
    :return:
    """
    # 获取数据
    data = pd.read_csv("train.csv")

    # 处理数据
    # 缩小数据以方便计算
    data = data.query("x > 2 & x < 2.5 & y > 1 & y < 1.5")

    # 对时间戳进行处理
    time_value = pd.to_datetime(data['time'], unit = 's')
    time_value = pd.DatetimeIndex(time_value)

    # 选取时间中的日、小时、星期几作为新特征
    data['day'] = time_value.day
    data['hour'] = time_value.hour
    data['weekday'] = time_value.weekday


    # 删除签到数量过少的地点
    place_count = data.groupby('place_id').count()['row_id']
    place_new = data['place_id'].isin(place_count[place_count > 3].index.values)
    data_final = data[place_new]

    # 获取特征值和目标值
    x = data_final[['x', 'y', 'accuracy', 'day', 'weekday', 'hour']]
    y = data_final['place_id']

    # 进行训练集和测试集的数据分割
    x_train, x_test, y_train, y_test = train_test_split(x, y)

    # 标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # KNN算法处理
    estimator = KNeighborsClassifier()
    param_dict = {'n_neighbors': [3, 5, 7, 9]}
    estimator = GridSearchCV(estimator, param_grid=param_dict, cv=3)
    estimator.fit(x_train, y_train)

    score = estimator.score(x_test, y_test)
    print('测试集的准确率：', score)
    print('最佳参数为：', estimator.best_params_)
    print('最佳验证集结果为：', estimator.best_score_)
    print('最佳估计器为：', estimator.best_estimator_)

if __name__=='__main__':
    facebook_knn()

