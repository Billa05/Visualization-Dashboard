import json
from pymongo import MongoClient

with open('jsondata.json') as f:
    data = json.load(f)

client = MongoClient("mongodb+srv://workinguse5:Biresh%402005@cluster0.hlgzx3g.mongodb.net/")

db = client['Blackcoffer']
collection = db['Dashboard']

collection.insert_many(data)
