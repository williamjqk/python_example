## 爬虫
- crawler/scrapy_recursive_sites_example.py: 递归的爬取下一页

## 数据库
- database/build_mongodb_for_conversation.py: 包括从数据文件批量建立数据库, 和删除数据库
- database/build_mongodb_from_xlsx.py: 从excel建立mongo数据库，包含pandas.io.json的使用
- database/mongodb_text_index.py: MongoDB的快速使用, 全文搜索的使用. 使用mongodb自带的全文索引（中文情况不好用）

## data mining, feature engineering, modeling
- datamining/feature_selection_f_regression_and_R_squared.py: 用f值、r2值选择特征的例子
- datamining/feature_selection_sklearn_example.py: 数据挖掘之特征选择，sklearn官网的例子
- datamining/mlxtend_stackcv.py: 一个哥们写的配合sklearn、xgboost使用的stacking工具包，端到端pipeline
- datamining/pandas_example.py: pandas的例子groupby、head、rank
- datamining/preparing_numeric_data.py: 使用mtcar数据做例子，展示数据预处理的过程
- datamining/rank_gauss.r: kaggle porto_seguro上有人提供的rank gauss程序(使用到inverse error function)
- datamining/rank_gauss.py: python版本的rank gauss normalization

## NLP
- nlp/gensim_jieba_example_1.py: 在gensim_workflow.py的基础上对中文进行处理、稀疏向量映射和相似度计算
- nlp/gensim_jieba_example_2.py: 在gensim_jieba_example_1.py的基础上对全量的语句集处理、局部语料的tfidf相似度计算
- nlp/gensim_workflow.py: 一个老外写的计算语言similarity的例子
- nlp/jieba_example.py: jieba的使用例子，包括带停用词分词、计算语句相似度等


## stackoverflow
- stackoverflow/...: 回答过的stackoverflow，脚本名就是问题

## deep learning, tensorflow, keras
- tensorflow/tf17_dropout_morvan.py: 有tensorboard使用，存成2个不同的文件夹
