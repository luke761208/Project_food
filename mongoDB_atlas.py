import pymongo
import pandas as pd
import csv

# 貼上剛剛複製的連線程式碼
client = pymongo.MongoClient("mongodb+srv://lukelee:cfb101@cluster0.lfpkd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.food
test = db.test
import json

data = pd.read_csv('fda_cleaning.csv',encoding = 'UTF-8')
data_json = json.loads(data.to_json(orient='records'))
test.insert_many(data_json) # test為前項步驟1的collection名稱
                            # 多筆資料輸入記得要用insert_many的方式

client.close() #關閉連線