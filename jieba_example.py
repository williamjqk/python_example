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
