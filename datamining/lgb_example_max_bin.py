# %%
# https://github.com/Microsoft/LightGBM/issues/435
import lightgbm as lgb
import numpy as np

x_tr_sc = np.random.randn(10000, 500)
x_te_sc = np.random.randn(100, 500)
y_tr_sc = np.random.randn(10000)
y_te_sc = np.random.randn(100)

max_bin = 2
lgb_train = lgb.Dataset(x_tr_sc, y_tr_sc, free_raw_data=False, max_bin=max_bin)
lgb_eval = lgb.Dataset(x_te_sc, y_te_sc, free_raw_data=False, max_bin=max_bin)

params = {
    'task': 'train',
    'boosting_type': 'gbdt',
    'objective': 'regression_l2',
    'metric': ['l2'],
    'num_leaves': 31,
    'learning_rate': 0.3,
    'feature_fraction': 0.7,
    'bagging_fraction': 0.9,
    'bagging_freq': 5,
    'verbose': 0,
    'num_threads': 10,
    'min_data_in_leaf': 100
}

def feval(preds, train_data):
    pass
    return 'metric', 0, True

evals_result = {}
gbm = lgb.train(
    params,
    lgb_train,
    num_boost_round=5,
    valid_sets=[lgb_train, lgb_eval],
    feval=feval,
    evals_result=evals_result)

prediction = gbm.predict(x_te_sc)
pred_leaf = gbm.predict(x_te_sc, pred_leaf=True)

print max((prediction - gbm._Booster__inner_predict_buffer[1]) / prediction)

global_pred = gbm._Booster__inner_predict_buffer[1]

print np.where(np.abs(global_pred - prediction) >= 1e-8)[0][:10]
# %%
