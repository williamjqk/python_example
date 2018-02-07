## 爬虫
- crawler/scrapy_recursive_sites_example.py: 递归的爬取下一页

## 数据库
- database/build_mongodb_for_conversation.py: 包括从数据文件批量建立数据库, 和删除数据库
- database/build_mongodb_from_xlsx.py: 从excel建立mongo数据库，包含pandas.io.json的使用
- database/mongodb_text_index.py: MongoDB的快速使用, 全文搜索的使用. 使用mongodb自带的全文索引（中文情况不好用）
- database/neo_test: 测试图数据库neo, py2neo的使用

## data mining, feature engineering, modeling
- datamining/feature_selection_f_regression_and_R_squared.py: 用f值、r2值选择特征的例子
- datamining/feature_selection_sklearn_example.py: 数据挖掘之特征选择，sklearn官网的例子
- datamining/mlxtend_stackcv.py: 一个哥们写的配合sklearn、xgboost使用的stacking工具包，端到端pipeline
- datamining/pandas_example.py: pandas的例子groupby、head、rank
- datamining/preparing_numeric_data.py: 使用mtcar数据做例子，展示数据预处理的过程
- datamining/rank_gauss.r: kaggle porto_seguro上有人提供的rank gauss程序(使用到inverse error function)
- datamining/rank_gauss.py: python版本的rank gauss normalization

- datamining/lgb_example_categorical_feature.py: 使用lgb的categorical_feature这个功能
- datamining/lgb_example_max_bin.py: 测试lgb的max_bin的例子
- datamining/lgb_example_with_async_pool.py: 测试lgb调用callbacks和pool.apply_async
- datamining/lgb_example.py: 官方的lgb的例子，regression.train和regression.test是对应的数据
- datamining/regression.test: lgb官方的regression数据的测试集
- datamining/regression.train: lgb官方的regression数据的训练集

- datamining/feature_survey_a_lot.py: 探索量化5号机特征的情况

- datamining/catboost_example.py: catboost使用的例子

- datamining/pd_test.py: 测试pandas和numpy的一些操作
- datamining/ppmoney_autoscaler_test.py: 测试云飞core里的autoscaler

## NLP
- nlp/gensim_jieba_example_1.py: 在gensim_workflow.py的基础上对中文进行处理、稀疏向量映射和相似度计算
- nlp/gensim_jieba_example_2.py: 在gensim_jieba_example_1.py的基础上对全量的语句集处理、局部语料的tfidf相似度计算
- nlp/gensim_workflow.py: 一个老外写的计算语言similarity的例子
- nlp/jieba_example.py: jieba的使用例子，包括带停用词分词、计算语句相似度等

## 跟python内核、python特有的语法相关的语句
- apply_async_test.py: 自己相关的线程+异步的例子，涉及到量化5号的用例
- async_await.py: 有一个简单的print("111111")例子，还有一个async/aiohttp爬网页的例子
- asyncio_test.py: 网上的一个例子，python3.5+版本的新用法
- decrator_test.py: 使用修饰器的例子
- yield_test.py: 测试协程yield
- queue_copy.py: 测试不同种类的队列
- ttt1.txt: apply_async_test.py使用到的测试文件


## stackoverflow
- stackoverflow/...: 回答过的stackoverflow，脚本名就是问题

## deep learning, tensorflow, keras
- tensorflow/tf17_dropout_morvan.py: 有tensorboard使用，存成2个不同的文件夹
- keras_mnist_test.py: 用keras搭建2维卷积网络
- keras_squential_model.py: 用Sequential()搭建model的例子
- tf_test.py: 测试tensorflow相关的一些简单操作
- tensorflow/capsulenet_on_mnist.py: 别人用keras实现的hinton的capsuleNet

## visualization
- plot_test.py: 测试matplotlib相关的一些操作
