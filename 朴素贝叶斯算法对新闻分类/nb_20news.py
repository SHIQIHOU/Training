from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

def nb_20news():
    """
    用朴素贝叶斯算法对新闻数据进行分类
    :return:
    """
    # 获取数据
    news = fetch_20newsgroups(subset="all")

    # 划分数据集
    x_train, x_test, y_train, y_test = train_test_split(news.data, news.target)

    # 特征工程
    transfer = TfidfVectorizer()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # 朴素贝叶斯算法预估器
    estimator = MultinomialNB()
    estimator.fit(x_train, y_train)

    # 模型评估
    # 真实值和预测值比对
    y_predict = estimator.predict(x_test)
    print("y_predict:\n", y_predict)
    print("直接比对:\n", y_test == y_predict)

    # 计算准确率
    score = estimator.score(x_test, y_test)
    print("准确率为:\n", score)

if __name__ == "__main__":
    nb_20news()