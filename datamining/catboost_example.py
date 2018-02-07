# coding: utf-8
# pylint: disable = invalid-name, C0111
import json
import lightgbm as lgb
import pandas as pd
from sklearn.metrics import mean_squared_error
from catboost import CatBoostRegressor
import numpy

# dataset = numpy.array([[1,4,5,6],[4,5,6,7],[30,40,50,60],[20,15,85,60]])
# train_labels = [1.2,3.4,9.5,24.5]
# model = CatBoostRegressor(learning_rate=1, depth=6, loss_function='RMSE')
# fit_model = model.fit(dataset, train_labels)
#
# print(fit_model.get_params())

print('Load data...')
df_train = pd.read_csv('/home/tom/data/regression.train', header=None, sep='\t')
df_test = pd.read_csv('/home/tom/data/regression.test', header=None, sep='\t')

y_train = df_train[0].values
y_test = df_test[0].values
X_train = df_train.drop(0, axis=1).values
X_test = df_test.drop(0, axis=1).values

y_train.shape
y_test.shape
X_train.shape
X_test.shape

def func1():
    print('haha')
model = CatBoostRegressor(iterations=500, thread_count=15, train_dir='/home/tom/data/cbm_example')
model.fit(X_train,y_train, eval_set=(X_test,y_test), verbose=True)

model.predict(X_test)

model.get_feature_importance()
