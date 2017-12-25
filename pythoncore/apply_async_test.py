# https://stackoverflow.com/questions/12483512/python-multiprocessing-apply-async-only-uses-one-process
# https://morvanzhou.github.io/tutorials/python-basic/multiprocessing/5-pool/

from multiprocessing.pool import ThreadPool

def func1():
    with ThreadPool(processes=1) as pool:
        def func2():
            print('2')
            def func3(x):
                print(x*x)
            pool.apply_async(func3, (12,))
        func2()
        return 1

func1()

# %%
import os
from multiprocessing.pool import ThreadPool
import time

def func4(x):
    print( "Working in Process #%d" % (os.getpid()))
    with open('ttt1.txt', 'w') as f:
        f.write(f"{x*x}")

with ThreadPool(1) as pool:
    pool.apply_async(func4, (11,))
    # pool.map_async(func4, (11,))
    # res = pool.apply_async(func4, (11,))
    # res.get()
print(111)

# %%
import os
from multiprocessing.pool import ThreadPool

def func5(x):
    print( "Working in Process #%d" % (os.getpid()))
    print(x*x)

pool = ThreadPool(4)

for i in range(5):
    pool.apply_async(func5, (i,))

# %%
import os
from multiprocessing import Pool
import time

def func6(x):
    print( "Working in Process #%d" % (os.getpid()))


with Pool(1) as pool:
    res = pool.apply_async(func6, (11,))
    print(res)
    print(res.get())

print(111)

# %%
import os
from multiprocessing.pool import ThreadPool
import time

def func7(x):
    return x*x


with ThreadPool(4) as pool:
    res_l = []
    for i in range(5):
        res_l.append(pool.apply_async(func7, (i,)))
    print(res_l)

print(111)

# %%
# https://jingsam.github.io/2015/12/31/multiprocessing.html
import os
import time
import multiprocessing
from multiprocessing.pool import ThreadPool
def func8(x):
    print(f"IN pool: {x*x}")
    return x*x

multiprocessing.freeze_support()
pool = multiprocessing.Pool()
cpus = multiprocessing.cpu_count()
results = []
for i in range(cpus):
    result = pool.apply_async(func8, args=(i,))
    results.append(result)
pool.close()
pool.join()
for result in results:
    print(result.get())
