#!/usr/bin/env python
#coding:utf-8
import os,sys,shutil
import pymongo

reload(sys)
sys.setdefaultencoding( "utf-8" )

connection = pymongo.MongoClient("localhost",27017)
mydb = connection.Spider # new a database
comment = mydb.Comment # new a table
clencomment = mydb.CleanComment

cdbs = comment.find({}).sort([('date', -1)])

f = open('sentence.txt','a')

for item in cdbs:
    body = item['body'] + '\n'
    if len(body) > 15 and len(body) < 50:
       f.write(body)
















