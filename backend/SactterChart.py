from pymongo import MongoClient

client = MongoClient("mongodb+srv://workinguse5:Biresh%402005@cluster0.hlgzx3g.mongodb.net/")
db = client['Blackcoffer']
collection = db['Dashboard']

def ScatterchartData(data,keyword):
    FormattedData=[]
    
    keywordlist = [doc.get(keyword) for doc in data if doc.get(keyword)]
    
    for word in set(keywordlist):
        wordFilter = collection.find({keyword:word})
        datalist = []
        for w in wordFilter:
            if w.get("intensity") and w.get("relevance"):
                innerdata={
                    "x":w.get("intensity"),
                    "y":w.get("relevance")
                }
                datalist.append(innerdata)
        formatdata={
            "id":word,
            "data":datalist
        }
        FormattedData.append(formatdata)
    return FormattedData
        
        
            
