import os
from pymongo import MongoClient
import json
from datetime import datetime
import re
import numpy as np
import pandas as pd
from difflib import SequenceMatcher


DATA_PATH = '/Users/fhr/Downloads/10jqka.xlsx'
db_name = 'ppmoney_xiaoP'
coll_name = 'conceptplate'
doc_format = '{{"category": "{}", "name": "{}", "code": "{}"}}'

client = MongoClient()
db = client[db_name]
coll = db[coll_name]

xls = pd.ExcelFile(DATA_PATH)
ncols = xls.book.sheet_by_index(0).ncols
df = xls.parse(0, converters={i : str for i in range(ncols)})
df.dtypes

len(df)

items_l = [{'category':df.iloc[i,15], 'name':df.iloc[i,2], "code":df.iloc[i,1]} for i in range(len(df))]
coll.insert_many(items_l)
print(f'BUILD concept plate of {coll.count()} stocks')

cursor = coll.find({'category': '一带一路'})
[x for x in cursor]
[{k:v for k,v in x.items() if k != '_id'} for x in cursor]
coll.distinct('category')

len(coll.distinct('category'))

cate_l = coll.distinct('category')
cate_l = [x.lower() for x in cate_l]
[SequenceMatcher(None, x, '概念').ratio() for x in cate_l]

re.sub('概念|板块|主营','','马云概念板块')

def choose_categ(sent_in, cate_l, th=0.5):
    s1 = re.sub('概念','',sent_in)
    sc_l = np.array([SequenceMatcher(None, re.sub('概念','',x), s1).ratio() for x in cate_l])
    max_ind = sc_l.argmax()
    print(sc_l)
    print(max_ind)
    if sc_l[max_ind] > th:
        return cate_l[max_ind]
    return None

SequenceMatcher(None, 'OLED', 'OLED').ratio()
choose_categ('OLED', cate_l)

def get_concept_stocks(categ_h, coll_h):
    cursor = coll_h.find({'category': categ_h})
    df = pd.DataFrame(list(cursor))
    del df['_id']
    return df

get_concept_stocks('一带一路', coll)


data = [{'state': 'Florida',
         'shortname': 'FL',
         'info': {
              'governor': 'Rick Scott'
         },
         'counties': [{'name': 'Dade', 'population': 12345},
                     {'name': 'Broward', 'population': 40000},
                     {'name': 'Palm Beach', 'population': 60000}]},
        {'state': 'Ohio',
         'shortname': 'OH',
         'info': {
              'governor': 'John Kasich'
         },
         'counties': [{'name': 'Summit', 'population': 1234},
                      {'name': 'Cuyahoga', 'population': 1337}]}]
from pandas.io.json import json_normalize
result = json_normalize(data, 'counties', ['state', 'shortname',
                                          ['info', 'governor']])


res = {'基金要点':{},
        '查询基金净值':{},
        '符合净值条件的基金':[
            {'股票代码':'003816.OF', '净值日期':'2017-07-25', '单位净值':110.26},
            {'股票代码':'003836.OF', '净值日期':'2017-07-25', '单位净值':210.26},
            {'股票代码':'003846.OF', '净值日期':'2017-07-25', '单位净值':310.26},
            {'股票代码':'003856.OF', '净值日期':'2017-07-25', '单位净值':410.26},
            {'股票代码':'003866.OF', '净值日期':'2017-07-25', '单位净值':510.26},
            {'股票代码':'003876.OF', '净值日期':'2017-07-25', '单位净值':610.26},
            {'股票代码':'003886.OF', '净值日期':'2017-07-25', '单位净值':710.26},
        ]
}
json_normalize(res,'符合净值条件的基金')

#
#
# # 删除特定name的MongoDB
# def del_mongodb(name=None, DATA_PATH=None):
#     client = MongoClient()
#     client.drop_database(name)
#
# # 根据DATA_PATH的数据文件建立数据库
# def build_mongodb(name=None, DATA_PATH=None):
#     if not name or not DATA_PATH:
#         raise Exception('Need name and data path')
#     client = MongoClient()
#     db = client[name]
#     coll = db[name]
#     strtime = datetime.now().strftime('%Y%m%d-%H%M%S')
#     # with open(DATA_PATH, 'r') as f:
#     #     pairs_l = json.load(f)
#     #     items_l = [doc_format.format('xhj_turing',strtime,x[0],x[1]) for x in pairs_l]
#     with open(DATA_PATH, 'r') as f:
#         pairs_l = json.load(f)
#         items_l = [{'source':'xhj_turing', 'timestamp':strtime, "text_in":x[0], "text_out":x[1], } for x in pairs_l]
#         coll.insert_many(items_l)
#     print(coll.count())
#     # coll.count()
#     # json.loads('{"1":1}')
#     # dict1 = json.loads(items_l[1])
#     # dict1
#
# if __name__ == '__main__':
#     del_mongodb(name, DATA_PATH)
#     build_mongodb(name, DATA_PATH)
