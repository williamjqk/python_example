# coding: utf-8
# pylint: disable = invalid-name, C0111
import json
import lightgbm as lgb
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
%matplotlib inline

# load or create your dataset
print('Load data...')
df_train = pd.read_csv('/home/tom/data/regression.train', header=None, sep='\t')
df_test = pd.read_csv('/home/tom/data/regression.test', header=None, sep='\t')
# df_train = pd.read_csv('./regression.train', header=None, sep='\t')
# df_test = pd.read_csv('./regression.test', header=None, sep='\t')

col = 21 + 1
df_train[df_train.columns[col]] *= 100.0
df_test[df_test.columns[col]] *= 100.0
df_train[df_train.columns[21]] *= 1
df_test[df_test.columns[21]] *= 1

test_np = np.array([[1.,2.,3.,4,5],[4.,5.,6.,7,8]])
test_np[:,[0,1,3,4]] *= 2
test_np

y_train = df_train[0].values
y_test = df_test[0].values
X_train = df_train.drop(0, axis=1).values
X_test = df_test.drop(0, axis=1).values

y_train.shape
y_test.shape
X_train.shape
X_test.shape

df1 = pd.DataFrame(X_train)
from pandas.tools.plotting import scatter_matrix
# scatter_matrix(df1.iloc[:,19:23],   # Make a scatter matrix of 6 columns
#                figsize=(10, 10),   # Set plot size
#                diagonal='kde')     # Show distribution estimates on diagonal
# scatter_matrix(df_train.iloc[:,[0,19,20,21,22,23,24]],   # Make a scatter matrix of 6 columns
            #    figsize=(10, 10),   # Set plot size
            #    diagonal='kde')     # Show distribution estimates on diagonal

pd.DataFrame(X_test).iloc[:,15:22]

# create dataset for lightgbm
max_bin = 63 # 31 # 15 # 255
lgb_train = lgb.Dataset(X_train, y_train, max_bin=max_bin)
lgb_eval = lgb.Dataset(X_test, y_test, reference=lgb_train, max_bin=max_bin)


# specify your configurations as a dict
params = {
    'task': 'train',
    'boosting_type': 'gbdt',
    'objective': 'regression',
    # 'metric': {'l2', 'auc'},
    'metric': {'auc','l2'},
    'num_leaves': 31,
    'learning_rate': 0.05,
    'feature_fraction': 0.9,
    'bagging_fraction': 0.8,
    'bagging_freq': 5,
    'verbose': 0,
    'min_lr': 0.01,
    # 'max_bin': 2,
}


print('Start training...')
# train
import time
t0 = time.time()
gbm = lgb.train(params,
                lgb_train,
                num_boost_round=200,# 20
                valid_sets=lgb_eval,
                categorical_feature=[20,21],
                early_stopping_rounds=10)

print(f"COST {time.time()-t0} seconds")

X_test.shape
gbm.feature_importance()
gbm.feature_importance('gain')

pd.DataFrame(X_test).iloc[:,15:22]

# %%
print('Save model...')
# save model to file
gbm.save_model('model.txt')

print('Start predicting...')
# predict
y_pred = gbm.predict(X_test, num_iteration=gbm.best_iteration)
# eval
print('The rmse of prediction is:', mean_squared_error(y_test, y_pred) ** 0.5)

print('Dump model to JSON...')
# dump model to json (and save to file)
model_json = gbm.dump_model()

with open('model.json', 'w+') as f:
    json.dump(model_json, f, indent=4)


print('Feature names:', gbm.feature_name())

print('Calculate feature importances...')
# feature importances
print('Feature importances:', list(gbm.feature_importance()))
