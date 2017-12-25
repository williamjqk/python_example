# %%
%matplotlib inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# df_train = pd.read_csv('./regression.train', header=None, sep='\t')
df_train = pd.read_csv('~/Downloads/1199.csv', header=None, sep=',', nrows=None, usecols=range(5))

mean_df = df_train.mean()
var_df = df_train.var()
# 用画出均值方差应该没有用seaborn的箱线图好
# mean_df.plot()
# var_df.plot()


df_part = df_train.iloc[:, [1,2,]]
# df_part = df_train.iloc[0:20,1:20]

np.core.defchararray.encode(np.array(df_train.iloc[:,0], dtype=np.str))

fig, ax = plt.subplots(figsize=(12, 8))
sns.boxplot(ax=ax, data=df_part )#


fig, ax = plt.subplots(figsize=(12, 8))
sns.violinplot(ax=ax, data=df_part )# **violin_options
