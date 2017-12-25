%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

plt.axis([0, 10, 0, 1])
plt.ion()

for i in range(10):
    y = np.random.random()
    plt.scatter(i, y)
    plt.pause(0.05)

# %%
import numpy as np
import time
from IPython import display
import matplotlib.pyplot as plt

x = []
y = []
for i in range(10):
    x = np.append(x, i)
    y = np.append(y, i**2)
    plt.gca().cla()
    plt.plot(x,y,label='test')
    plt.legend()
    plt.draw()
    # display.clear_output(wait=True)
    # display.display(plt.gcf())
    time.sleep(0.3)

# %% color map
import matplotlib as mpl
import matplotlib.cm as cm

norm = mpl.colors.Normalize(vmin=-20, vmax=10)
cmap = cm.hot
x = 0.3

m = cm.ScalarMappable(norm=norm, cmap=cmap)
print(m.to_rgba(x))
plt.plot([1,2,3],[2,3,4],color=m.to_rgba(x))

# while True:
#     plt.pause(0.05)
