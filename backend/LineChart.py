from pymongo import MongoClient
import random

client = MongoClient("mongodb+srv://workinguse5:Biresh%402005@cluster0.hlgzx3g.mongodb.net/")
db = client['Blackcoffer']
collection = db['Dashboard']

import json

def LinechartData(data, keyword, country=None):
    FormattedData = []
    
    
    countries = []
    if country == None:
        for doc in data:
            if doc["country"]:
                countries.append(doc["country"])
            elif doc["country"] == "":
                countries.append("undefined_country")
    else:
        countries.append(country)

    for id in set(countries):
        CountryFilter=collection.find({"country":id})
        XYdata=[]
        words = []
        for i in CountryFilter:
            word = i[keyword]
            if word and word not in words:
                words.append(word)
                WordFilter=collection.find({keyword:word})
                yearlist=[]
                for j in WordFilter:
                    if j["start_year"] or j["end_year"]:
                        yearlist.append(j["start_year"]) if j["start_year"] else yearlist.append(j["end_year"])
                    else:
                        yearlist.append(random.randint(2016,2024))
                xydata={
                    "x":word,
                    "y":random.choice(yearlist)
                }
                XYdata.append(xydata)
        formatdata = {
            "id":id,
            "color":f"hsl({random.randint(70,300)},70%,50%)",
            "data":XYdata
            
        }
        FormattedData.append(formatdata)
    return FormattedData
                
                