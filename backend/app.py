import random
import os
from dotenv import load_dotenv
from flask import Flask, request, g
from pymongo import MongoClient
from HeatMap import HeatmapData
from PieChart import PiechartData
from LineChart import LinechartData
from SactterChart import ScatterchartData
from Choropleth import ChoroplethData
from copy import deepcopy
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
    collection = db['Dashboard']
    data = collection.find()
    
    if not request.args:
        return(
            {
            "heatmap":HeatmapData(deepcopy(data)),
            "piechart":PiechartData(deepcopy(data),keyword="pestle"),
            "linechart":LinechartData(deepcopy(data),keyword="topic"),
            "scatterchart":ScatterchartData(deepcopy(data),keyword="sector"),
            "choropleth":ChoroplethData(deepcopy(data),keyword="intensity")
            }
        )

    else:
        filters = {
            "heatmap":HeatmapData(data=data)
        }

        filter_pie_keys = ['source', 'topic', 'sector', 'insight', 'region', 'country', 'pestle']
        pie_values=[]
        for key in filter_pie_keys:
            value = request.args.get(key)
            if value:
                pie_values.append(value)
        filters["piechart"] = PiechartData(data=data,keyword=random.choice(pie_values))

        
        filter_choropleth_keys=['intensity','relevance','likelihood']
        choropleth_values=[]
        for key in filter_choropleth_keys:
            value = request.args.get(key)
            if value:
                choropleth_values.append(value)
        filters["choropleth"]=ChoroplethData(data=data,keyword=random.choice(choropleth_values))
        
        
        filter_scatter_keys=['country','topic','sector','pestle']
        scatter_values=[]
        for key in filter_scatter_keys:
            value = request.args.get(key)
            if value:
                scatter_values.append(value)
        filters['scatter'] = ScatterchartData(data=data,keyword=random.choice(scatter_values))
        
        
        filter_line_keys=['topic','pestle','insight','sector',]
        line_values=[]
        for key in filter_line_keys:
            value=request.args.get(key)
            if value:
                line_values.append(value)
        if not request.args.get("country"):
            filters['line'] = LinechartData(data=data,keyword=random.choice(line_values))
        else:
            filters['line'] = LinechartData(data=data,keyword=random.choice(line_values),country=request.args.get("country"))
            
        return filters
    
if __name__ == '__main__':
    app.run(debug=True)
