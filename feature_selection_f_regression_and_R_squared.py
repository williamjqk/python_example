# %%
# 主要内容来自:
# https://stats.stackexchange.com/questions/204141/difference-between-selecting-features-based-on-f-regression-and-based-on-r2
# mtcars数据来自:
# http://hamelg.blogspot.com/2015/11/python-for-data-analysis-part-16.html
import pandas as pd
import numpy as np
from sklearn import feature_selection
from sklearn.linear_model import LinearRegression

#....load mtcars dataset into a pandas dataframe called "df", not shown here for conciseness
# only using these numerical columns as features ['mpg', 'disp', 'drat', 'wt']
# using this column as the label:  ['qsec']
from ggplot import mtcars
columns = ['mpg', 'disp', 'drat', 'wt']
df = mtcars

# %%

model = feature_selection.SelectKBest(score_func=feature_selection.f_regression,\
                                      k=4)

results = model.fit(df[columns], df['qsec'])

print( results.scores_)
print( results.pvalues_)

# Using just correlation coefficient:

columns = ['mpg', 'disp', 'drat', 'wt']
for col in columns:
    lm = LinearRegression(fit_intercept=True)
    lm.fit(df[[col]], df['qsec'])
    print( lm.score(df[[col]], df['qsec']))

# 不能独立的看f_regression或r-squared的打分, 因为特征之间可能是相关的


# %%
