# %%
# http://scikit-learn.org/stable/modules/feature_selection.html
# 特征选择的目的是对样本数据的特征进行选择,降维, 同时提高估计器的精度, 加速高维数据集上的性能.

# 移除低方差的特征
from sklearn.feature_selection import VarianceThreshold
X = [[0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 1, 1]]
sel = VarianceThreshold(threshold=0.8*(1-0.8))
sel.fit_transform(X)

# %%
# 单变量特征选择
# 这种方法根据单个变量自身的统计检验来选择, 我们可以选出Chi2最好的n个, 也可以
# 选出F-test最好的前10%, 都可以, sklearn满足你. 这个过程可以看作估计器的预处理
# 阶段.
# 一般用卡方检验选择, 通常对于理解数据有较好的效果（但对特征优化、提高泛化能力来说不一定有效）
# 下面这些指标作为输入, 返回单变量打分和p-value
# For regression: f_regression, mutual_info_regression
# For classification: chi2, f_classif, mutual_info_classif
# F-test类方法估计两随机变量线性依赖度. mutual info类方法能捕捉任意种类
# 的统计独立性, 但由于这类方法是非参数的, 它需要跟多的样本才能精确.
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
iris = load_iris()
X, y = iris.data, iris.target
X.shape

X_new = SelectKBest(chi2, k=2).fit_transform(X, y)
X_new.shape

# %%
