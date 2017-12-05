#!/usr/bin/env python
# coding:utf-8

import os,sys,jieba
from bayes import *
from kMeans import *
from sklearn import feature_extraction

reload(sys)
sys.setdefaultencoding( "utf-8" )

sens = open('sentence.txt','r').readlines()

sentencList = []

for line in sens:
    seg_list = jieba.cut(line)
    seg_listnew = []
    for seg in seg_list:
        seg_listnew.append(seg)
    sentencList.append(seg_listnew)

wordList = createVocabList(sentencList)

# sen1 = '感谢京东一直的努力，从默默无语到现在国人众知，我相信京东会越走越强大！永远支持京东商城！很好用，我的理财都是在京东做的'
# sen2 = '很好用，我的理财都是在京东做的'

# seg1 = jieba.cut(sen1)
# seg1List = []
# for word in seg1:
#     seg1List.append(word)


# seg2 = jieba.cut(sen2)
# seg2List = []
# for word in seg2:
#     seg2List.append(word)    

# voc1 = bagOfWords2VecMN(wordList,seg1List)    
# voc2 = bagOfWords2VecMN(wordList,seg2List)   

# print sum(voc1)
# print sum(voc2)

# print gen_sim(array(voc1),array(voc2)) 

def culate(docs_matrix):
    column_sum = [ float(len(np.nonzero(docs_matrix[:,i])[0])) for i in range(docs_matrix.shape[1]) ]
    column_sum = np.array(column_sum)
    column_sum = docs_matrix.shape[0] / column_sum
    idf =  np.log(column_sum)
    idf =  np.diag(idf)
    # 请仔细想想，根绝IDF的定义，计算词的IDF并不依赖于某个文档，所以我们提前计算好。
    # 注意一下计算都是矩阵运算，不是单个变量的运算。
    for doc_v in docs_matrix:
        if doc_v.sum() == 0:
            doc_v = doc_v / 1
        else:
            doc_v = doc_v / (doc_v.sum())
        tfidf = np.dot(docs_matrix,idf)
        return tfidf

dataSet = []

for line in sentencList:
    vec = bagOfWords2VecMN(wordList,line)
    dataSet.append(vec)     

dataSet = array(dataSet)

tfidf = culate(dataSet)

print type(tfidf)
print tfidf

centroids, clusterAssment = kCharMeans(dataSet=dataSet,k=4)

print centroids
print '********'
print clusterAssment







