#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gensim import corpora, models, similarities
import time
import jieba
import json
import numpy as np
from scipy import sparse
from itertools import chain

t0=time()

# keywords have been extracted and stopwords removed.

xhj=[
    '股票有哪些蓝筹股',
    '债权变现的有效期',
    '债权变现是什么',
]

with open('turing_xhj.json') as f:
    xhj_l = json.load(f)
xhj = [x[0] for x in xhj_l]

tweets = [jieba.lcut(x) for x in xhj]

dictionary = corpora.Dictionary(tweets)
dictionary.save('/tmp/tweets.dict') # store the dictionary, for future reference

raw_corpus = [dictionary.doc2bow(t) for t in tweets]

corpora.MmCorpus.serialize('/tmp/tweets.mm', raw_corpus) # store to disk

dictionary = corpora.Dictionary.load('/tmp/tweets.dict')

corpus = corpora.MmCorpus('/tmp/tweets.mm')

tfidf = models.TfidfModel(corpus) # step 1 -- initialize a model

corpus_tfidf = tfidf[corpus]

# index = similarities.MatrixSimilarity(tfidf[corpus])
# index.save('/tmp/deerwester.index')
# index = similarities.MatrixSimilarity.load('/tmp/deerwester.index')


# print sims
# print list(enumerate(sims))
# sims = sorted(enumerate(sims), key=lambda item: item[1])
# print sims # print sorted (document number, similarity score) 2-tuples
# %%
tfidf[dictionary.doc2bow(['你','是','谁'])]
tfidf[dictionary.doc2bow(['债权变现','的','有效期'])]
# %%
def sent2sparse_vec(raw_sent,length):
    raw_words = jieba.lcut(raw_sent)
    vec = dictionary.doc2bow(raw_words)

    tfidf_mid = tfidf[vec]

    ii=[0 for i,_ in enumerate(tfidf_mid)]
    jj=[j for j,_ in tfidf_mid]
    data=[d for _,d in tfidf_mid]

    return sparse.csr_matrix((data,(ii,jj)),shape=(1,length))

print(tfidf)

# %% 如果全量的gensim速度慢就用scipy.sparse这个
s_vec1 = sent2sparse_vec('债权变现有效期是什么',100)
s_vec2 = sent2sparse_vec('债权变现的有效期',100)
s_vec1.dot(s_vec2.transpose()).A

# %% 计算局部的tfidf的完整程序
from gensim import corpora, models, similarities
import time
import jieba
t0 = time.time()
sent_l=[
    '股票有哪些蓝筹股',
    '债权变现的有效期',
    '债权变现是什么',
    '股票是什么',
    '你是谁',
    '芝麻开花节节高'
]
tweets = [jieba.lcut(x) for x in sent_l]

dictionary = corpora.Dictionary(tweets)
raw_corpus = [dictionary.doc2bow(t) for t in tweets]
corpus = raw_corpus

tfidf = models.TfidfModel(corpus) # step 1 -- initialize a model
corpus_tfidf = tfidf[corpus]
query = tfidf[dictionary.doc2bow(['债权变现','有效期','是','什么'])]
index = similarities.Similarity('./index',corpus_tfidf,num_features=400,norm='l2')
print(index[query])
print(f"COST TIME: {time.time()-t0}")

from itertools import chain
''.join(chain(*[x for x in jieba.lcut('债权变现是什么') if x != '什么']))
