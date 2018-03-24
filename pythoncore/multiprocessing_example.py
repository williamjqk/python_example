# %% NOTE： 最简单的一个多进程程序，1个主进程，2个子进程，打印PID
import os
import multiprocessing as mp
from multiprocessing import Process, Queue

def print_pid():
    id_h = os.getpid()
    print(f"pid: {id_h}")

p1 = Process(target=print_pid)
p2 = Process(target=print_pid)

print(f"pid: {os.getpid()}")
p1.start()
p2.start()

# %% NOTE：试验一个单向的Queue
import os, time, random
import multiprocessing as mp
import random
from multiprocessing import Process, Queue

def get_number(name, q):
    for i in range(5):
        num = q.get()
        print(f"name: {name}, pid: {os.getpid()}, number: {num}")
        time.sleep(random.random())

def put_number(name, q):
    for i in range(5):
        num = i**2
        q.put(num)
        print(f"name: {name}, pid: {os.getpid()}, number: {num}")
        time.sleep(random.random())

q = Queue()
p1 = Process(target=get_number, args=("GET", q))
p1.start()
put_number("PUT", q)

# %% concurrent
import os
import time
from concurrent.futures import ProcessPoolExecutor
def func():
    time.sleep(1)
    for i in range(3):
        print(f"{os.getpid()}: {i}")
    return os.getpid()

with ProcessPoolExecutor(3) as executor:
    futs = {executor.submit(func) for i in range(3)}

futs
