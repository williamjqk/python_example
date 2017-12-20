# https://www.kaggle.com/c/porto-seguro-safe-driver-prediction/discussion/44629#255552
import numpy as np
from scipy.special import erfinv
import pandas as pd

# this is not correct
# def rank_gauss(X):
#     # create the list of unique values in X and sort them
#     sorted_items = sorted(set(X))
#     # Rank each of the values in linspace (0,1)
#     sorted_ranks = {}
#     rank = 0
#     for i in sorted_items:
#         sorted_ranks[i] = rank/len(sorted_items)
#         rank+=1
#     # Create a list of normalized X values
#     normalized_X = []
#     for i in X:
#         normalized_X.append(sorted_ranks[i])
#     # Apply erfinv on the ranks
#     normalized_X = erfinv(np.array(normalized_X))
#     # subtract the means from the results
#     normalized_X = normalized_X - np.mean(normalized_X)
#     return normalized_X

def rank_gauss(x):
    # x is numpy vector
    N = x.shape[0]
    temp = x.argsort()
    rank_x = temp.argsort() / N
    rank_x -= rank_x.mean()
    rank_x *= 2 # rank_x.max(), rank_x.min() should be in (-1, 1)
    efi_x = erfinv(rank_x) # np.sqrt(2)*erfinv(rank_x)
    efi_x -= efi_x.mean()
    return efi_x

# %%
# for rank see https://stackoverflow.com/questions/5284646/rank-items-in-an-array-using-python-numpy
x = np.random.rand(500)
pd.Series(x).hist()
plt.show()

N = x.shape[0]
temp = x.argsort()
rank_x = temp.argsort() / N * 1.99999 - 0.99999 # rank_x.max(), rank_x.min()
# rank_x -= rank_x.mean()
efi_x = np.sqrt(2)*erfinv(rank_x)
efi_x -= efi_x.mean()

pd.Series(efi_x).hist()
plt.show()

# %%
x = np.random.rand(500)
pd.Series(x).hist()
plt.show()

N = x.shape[0]
temp = x.argsort()
# rank_x = temp.argsort() / N * 1.99 - 0.99
rank_x = temp.argsort() / N
rank_x -= rank_x.mean()
rank_x *= 2 # rank_x.max(), rank_x.min()
# efi_x = np.sqrt(2)*erfinv(rank_x)
efi_x = erfinv(rank_x)
efi_x -= efi_x.mean()

pd.Series(efi_x).hist()
plt.show()

# %% a self-contained example
import numpy as np
import pandas as pd
from scipy.special import erfinv
import matplotlib.pyplot as plt

def rank_gauss(x):
    # x is numpy vector
    N = x.shape[0]
    temp = x.argsort()
    rank_x = temp.argsort() / N
    rank_x -= rank_x.mean()
    rank_x *= 2 # rank_x.max(), rank_x.min() should be in (-1, 1)
    efi_x = erfinv(rank_x) # np.sqrt(2)*erfinv(rank_x)
    efi_x -= efi_x.mean()
    return efi_x

x = np.random.rand(5000)
# histogram test: the histogram of rank_gauss should be gauss-liked and centered
pd.Series(x).hist()
plt.show()
pd.Series(rank_gauss(x)).hist()
plt.show()

efi_x = rank_gauss(x)
efi_x.min(), efi_x.max()
