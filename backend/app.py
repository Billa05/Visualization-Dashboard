import random
import os
from dotenv import load_dotenv
from flask import Flask, request, g
from pymongo import MongoClient
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)

def get_db():
    if 'db' not in g:
        g.client = MongoClient(os.getenv('mongo_uri'))
        g.db = g.client['Blackcoffer']
    return g.db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'client'):
        g.client.close()
    
@app.route('/',methods=['GET'])
def ReturnFIlterData():
    db = get_db()
    collection = db['FormatedData']
    data = collection.find()
    
    if not request.args:
        return(
            {
            "heatmap":collection.find({"filter":"Heatmap"})[0]["data"],
            "piechart":collection.find({"filter":"pie_pestle"})[0]["data"],
            "linechart":collection.find({"filter":"line_topic"})[0]["data"],
            "scatterchart":collection.find({"filter":"scatter_sector"})[0]["data"],
            "choropleth":collection.find({"filter":"choropleth_intensity"})[0]["data"]
            }
        )

    else:
        filters = {
            "heatmap":collection.find({"filter":"Heatmap"})[0]["data"]
        }

        filter_pie_keys = ['source', 'topic', 'sector', 'insight', 'region', 'country', 'pestle']
        pie_values=[]
        for key in filter_pie_keys:
            value = request.args.get(key)
            if value:
                pie_values.append(value)
        keyword=random.choice(pie_values)
        filters["piechart"] = collection.find({"filter":f"pie_{keyword}"})[0]["data"]

        
        filter_choropleth_keys=['intensity','relevance','likelihood']
        choropleth_values=[]
        for key in filter_choropleth_keys:
            value = request.args.get(key)
            if value:
                choropleth_values.append(value)
        keyword=random.choice(choropleth_values)
        filters["choropleth"]=collection.find({"filter":f"choropleth_{keyword}"})[0]["data"]
        
        
        filter_scatter_keys=['country','topic','sector','pestle']
        scatter_values=[]
        for key in filter_scatter_keys:
            value = request.args.get(key)
            if value:
                scatter_values.append(value)
        keyword=random.choice(scatter_values)
        filters['scatter'] = collection.find({"filter":f"scatter_{keyword}"})[0]["data"]
        
        
        filter_line_keys=['topic','pestle','insight','sector',]
        line_values=[]
        for key in filter_line_keys:
            value=request.args.get(key)
            if value:
                line_values.append(value)
        if not request.args.get("country"):
            keyword=random.choice(line_values)
            filters['line'] = collection.find({"filter":f"line_{keyword}"})[0]["data"]
        else:
            keyword=random.choice(line_values)
            filters['line'] = collection.find({"filter":f"line_{keyword}_{request.args.get('country')}"})[0]["data"]
            
        return filters
    
if __name__ == '__main__':
    app.run(debug=True)
