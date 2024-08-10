from pymongo import MongoClient

client = MongoClient("mongodb+srv://workinguse5:Biresh%402005@cluster0.hlgzx3g.mongodb.net/")
db = client['Blackcoffer']
collection = db['FormatedData']

print(collection.find({"filter":"heatmap"})[0]["data"])
