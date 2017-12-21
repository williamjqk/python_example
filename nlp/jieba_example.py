'''
jieba 导入词典后的效果测试
'''
import jieba
import jieba.posseg as pseg
jieba.lcut('李小福是创新办主任也是云计算方面的专家')

# jieba.load_userdict('sougou-dic.txt')
jieba.add_word('财源宝', freq=150, tag='nz')
pseg.lcut('财源宝贝好')
# 像'财源'和'宝贝'这两个词, 在120-150之间,
# 财源宝 120 nz, 就分不了词
# 财源宝 120 nz, 就能分出这个词

pseg.lcut('我想买理财产品')
pseg.lcut('什么是上升通道')
pseg.lcut('刘德华是谁')
pseg.lcut('中国的首都城市是北京')

# %% 停用词
import jieba
import jieba.analyse

jieba.analyse.set_stop_words('stop_words.txt')
# stop_words.txt:
# --------
# 是
# 什么
# 怎么
# --------
jieba.analyse.extract_tags('中国的首都城市是北京什么')

# %% jieba.analyse.extract_tags()会默认去除一些停用词，
# 像“操你妈”这种词它是默认为停用词的，有时候这并不方便，
# 我们可以人为的手动处理停用词
jieba.analyse.extract_tags('hello 你好 fuck')

sent1 = jieba.analyse.extract_tags('债权变现有效期是什么')
sent2 = jieba.analyse.extract_tags('债权变现是什么')
sent3 = jieba.analyse.extract_tags('债权变现的有效期是什么')
from difflib import SequenceMatcher
SequenceMatcher(None, sent1, sent2).ratio()

SequenceMatcher(None, jieba.lcut('债权变现有效期是什么'), jieba.lcut('债权变现是什么')).ratio()

def sequence_sim_without_stop_words(sent1, sent2):
    sent1in = jieba.analyse.extract_tags(sent1)
    sent2in = jieba.analyse.extract_tags(sent2)
    print(sent1in,sent2in)
    return SequenceMatcher(None, sent1in, sent2in).ratio()
sequence_sim_without_stop_words('股票','股票基金')

def jaccard_basic(synonym_vector1, synonym_vector2):
    count_intersection = list(set(synonym_vector1).intersection(set(synonym_vector2)))
    count_union = list(set(synonym_vector1).union(set(synonym_vector2)))
    sim = len(count_intersection)/len(count_union)
    return sim
def jaccard_sim_without_stop_words(sent1, sent2):
    sent1in = jieba.analyse.extract_tags(sent1)
    sent2in = jieba.analyse.extract_tags(sent2)
    print(sent1in, sent2in)
    return jaccard_basic(sent1in, sent2in)
jieba.lcut('')
{}.fromkeys(['a','b'])
with open('stop_words.txt','r') as f:
    stop_words = {}.fromkeys(f.read().splitlines())
