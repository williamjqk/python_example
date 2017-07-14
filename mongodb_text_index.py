import pymongo
from pymongo import MongoClient
from pymongo import TEXT
import jieba # 中文分词工具,下面的例子会用到
import pprint # pretty print 工具包, 用这个打印格式更整洁
# 这是两个自定义了两个条目,作为下面程序的用例
item1 = {
    'name': "Burger",
    'ingredients': [
        "bread",
        "cheese",
        "tomato",
        "beef"
    ]
}
item2 = {
    'name': 'Pizza',
    'ingredients': [
        'cheese',
        'bacon',
        'flour',
        'pepper'
    ]
}
# 初始化一个client实例
client = MongoClient()
client.drop_database('recipe')
client.drop_database('db')
# 建立或者调用一个名为recipe的database
db = client['recipe']
# 建立或调用一个名为posts的collection
foods = db['foods']
# 把item1条目插入到foods
foods.insert_one(item1).inserted_id
# 列出数据库db下的所用的collection的名称
db.collection_names(include_system_collections=False)
# 随机找出foods中的一个条目(也就是一个document)
db.foods.find_one()

# 遍历foods钟所有的数据
cursor = foods.find()
pprint.pprint([x for x in cursor])

# %%
# 插入新的一个item
foods.insert_one(item2).inserted_id
foods.index_information()
pprint.pprint([x for x in foods.find({'ingredients': 'cheese'})])

# %%
# 英文全文搜索(full text search)用例
dialogs = db['dialogs']
d1 = {
    'text_in': 'this ball and this ball are toys in the house',
    'text_out': 'find thank you',
    'keywords_dialog': ['ball', 'toys', 'house'],
}
d2 = {
    'text_in': 'this ball is a toys in the house this is a car and a space boat computer is a hammer',
    'text_out': 'i am 9',
    'keywords_dialog': ['ball', 'toys', 'car'],
}
dialogs.insert_many([d1,d2])
dialogs.create_index([('text_in', TEXT)], default_language='en')
keywords = 'ball toys'
cursor = dialogs.find({'$text': {'$search':keywords}}, {'score':{'$meta':'textScore'}})
pprint.pprint([x for x in cursor])


# %% keywords index关键词索引
# 关键词索引是强'与'条件(Hard AND)
dialogs_zh = db['dialogs_zh']
d1_zh = {
    'text_in': '小孩在那玩玩具',
    'text_out': 'find thank you',
    'keywords_dialog': ['小', '孩', '玩'],
}
d2_zh = {
    'text_in': '小孩去学校',
    'text_out': 'i am 9',
    'keywords_dialog': ['小', '孩', '学'],
}
dialogs_zh.insert_many([d1_zh,d2_zh])
dialogs_zh.create_index([('keywords_dialog', pymongo.ASCENDING)])
keywords_zh = ['小', '孩', '学']
cursor = dialogs_zh.find({'keywords_dialog': {'$all': keywords_zh}})
pprint.pprint([x for x in cursor])

# %% english模式下的中文全文索引
dialogs = db['dialogs_zh_fulltext']
d1 = {
    'text_in': '你 早上 吃 的 什么 ?',
    'text_out': '我 吃 的 鸡蛋',
}
d2 = {
    'text_in': '你 今天 准备 去 哪 ?',
    'text_out': '我 要 回家',
}
dialogs.insert_many([d1,d2])
dialogs.create_index([('text_in', TEXT)], default_language='en')
keywords = ' '.join(jieba.lcut('你今天早上去哪了?'))
print('keywords: {}'.format(keywords))
cursor = dialogs.find({'$text': {'$search':keywords}}, {'score':{'$meta':'textScore'}})
for x in cursor.sort([('score', {'$meta':'textScore'})]):
    pprint.pprint(x)
