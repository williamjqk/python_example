# %% simple example
from PPMoney.core.preprocessing import AutoScaler
import numpy as np
scaler = AutoScaler()
example_matrix = np.random.randn(5,3)
scaler.fit(example_matrix)
scaler.transform(example_matrix)

# %% example np.nan
from PPMoney.core.preprocessing import AutoScaler
import numpy as np
a1 = np.zeros((5,1))
a2 = np.hstack((a1, np.random.randn(5,3)))
# a2[4,0] = 2 # 这个scaler真的
print(a2)
scaler = AutoScaler()
scaler.fit(a2)
print(scaler.transform(a2))
