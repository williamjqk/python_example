import os
from pymongo import MongoClient
import json
from datetime import datetime
import re

DATA_PATH = 'turing_xhj.json'
name = 'xhj_turing'
doc_format = '{{"source": "{}", "timestamp": "{}", "text_in": "{}", "text_out": "{}"}}'

# 删除特定name的MongoDB
def del_mongodb(name=None, DATA_PATH=None):
    client = MongoClient()
    client.drop_database(name)

# 根据DATA_PATH的数据文件建立数据库
def build_mongodb(name=None, DATA_PATH=None):
    if not name or not DATA_PATH:
        raise Exception('Need name and data path')
    client = MongoClient()
    db = client[name]
    coll = db[name]
    strtime = datetime.now().strftime('%Y%m%d-%H%M%S')
    # with open(DATA_PATH, 'r') as f:
    #     pairs_l = json.load(f)
    #     items_l = [doc_format.format('xhj_turing',strtime,x[0],x[1]) for x in pairs_l]
    with open(DATA_PATH, 'r') as f:
        pairs_l = json.load(f)
        items_l = [{'source':'xhj_turing', 'timestamp':strtime, "text_in":x[0], "text_out":x[1], } for x in pairs_l]
        coll.insert_many(items_l)
    print(coll.count())
    # coll.count()
    # json.loads('{"1":1}')
    # dict1 = json.loads(items_l[1])
    # dict1

if __name__ == '__main__':
    del_mongodb(name, DATA_PATH)
    build_mongodb(name, DATA_PATH)
