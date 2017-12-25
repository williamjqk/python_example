from queue import Queue as Q
# from queue import PriorityQueue as Q

import copy

q1 = Q()

def printQueue(q):
    while not q.empty():
        print( (q.get()),)
    print( '')

q1.put((5,'s'))
q1.put((2,'e'))
q1.put((0,'a'))
q1.put((0,'z'))
# printQueue(copy.copy(q1))
# print( 'second')

q2 = Q()
q2.queue = copy.deepcopy(q1.queue)
printQueue(copy.copy(q1))

print( 'second')
printQueue(copy.copy(q2))

# %%
import json
qa = []
while not q1.empty():
    qa.append(q1.get())
with open('test_mba_json.json', 'w') as f:
    json.dump(qa, f, sort_keys=True, ensure_ascii=False, indent=2, separators=(',', ': '))

# %% 自定义高级队列
# https://stackoverflow.com/questions/16506429/check-if-element-is-already-in-a-queue
# 自定义去重队列
class SetQueue(Queue.Queue):
    def _init(self, maxsize):
        self.queue = set()
    def _put(self, item):
        self.queue.add(item)
    def _get(self):
        return self.queue.pop()
# 自定义优先级去重队列
class OrderedSetQueue(Queue.Queue):
    def _init(self, maxsize):
        self.queue = OrderedSet()
    def _put(self, item):
        self.queue.add(item)
    def _get(self):
        return self.queue.pop()
# 自定义可查看队列
class CheckableQueue(Queue.Queue): # or OrderedSetQueue
    def __contains__(self, item):
        with self.mutex:
            return item in self.queue
# 安全调用
with my_queue.mutex:
    if x not in my_queue:
        my_queue.put(x)
