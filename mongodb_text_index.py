import pymongo
from pymongo import MongoClient
from pymongo import TEXT
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
client = MongoClient()
client.drop_database('recipe')
# 建立或者调用一个名为recipe的database
db = client['recipe']
# 建立或调用一个名为posts的collection
foods = db['foods']

foods.insert_one(item1).inserted_id

db.collection_names(include_system_collections=False)

db.foods.find_one()

# 遍历所有数据
cursor = foods.find()
[x for x in cursor]

# %%
# 插入新的一个item
foods.insert_one(item2).inserted_id
# foods.create_index([('ingredients', TEXT)], default_language='english')
# [x for x in foods.find()]
foods.index_information()
[x for x in foods.find({'ingredients': 'cheese'})]

# %%
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
keywords = 'ball toys'#['how','old']
cursor = dialogs.find({'$text': {'$search':keywords}}, {'score':{'$meta':'textScore'}})
[x for x in cursor]
# dialogs.find({'$text': {'$search':keywords}}, {'score':{'$meta':'textScore'}})
# [x for x in cursor.sort([('score', {'$meta':'textScore'})])]

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
[x for x in cursor]

# %% english模式下的中文全文索引
dialogs = db['dialogs_zh_fulltext']
d1 = {
    'text_in': '小 孩 在 那 玩 玩 具',
    'text_out': 'find thank you',
    'keywords_dialog': ['ball', 'toys', 'house'],
}
d2 = {
    'text_in': '小 孩 去 学 校',
    'text_out': 'i am 9',
    'keywords_dialog': ['ball', 'toys', 'car'],
}
dialogs.insert_many([d1,d2])
dialogs.create_index([('text_in', TEXT)], default_language='en')
keywords = '小 孩 学'#['how','old']
cursor = dialogs.find({'$text': {'$search':keywords}}, {'score':{'$meta':'textScore'}})
[x for x in cursor]
