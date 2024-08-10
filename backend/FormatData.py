from pymongo import MongoClient
from HeatMap import HeatmapData
from PieChart import PiechartData
from LineChart import LinechartData
from SactterChart import ScatterchartData
from Choropleth import ChoroplethData
from copy import deepcopy


def filterdata():
    client = MongoClient("mongodb+srv://workinguse5:Biresh%402005@cluster0.hlgzx3g.mongodb.net/")
    db = client['Blackcoffer']
    collection = db['Dashboard']
    new_collection = db['FormatedData']
    data = collection.find()

    filters = [{
            "filter":"Heatmap",
            "data":HeatmapData(data=deepcopy(data))
        }]

    filter_pie_keys = ['source', 'topic', 'sector', 'insight', 'region', 'country', 'pestle']
    for key in filter_pie_keys:
        res = {"filter":f"pie_{key}",
            "data":PiechartData(data=deepcopy(data),keyword=key)}
        filters.append(res);
        


    
    filter_choropleth_keys=['intensity','relevance','likelihood']
    for key in filter_choropleth_keys:
        res={"filter":f"choropleth_{key}",
             "data":ChoroplethData(data=deepcopy(data),keyword=key)}
        filters.append(res)
    
    
    filter_scatter_keys=['country','topic','sector','pestle']
    for key in filter_scatter_keys:
        res = {"filter":f"scatter_{key}",
               "data":ScatterchartData(data=deepcopy(data),keyword=key)}
        filters.append(res)
    
    
    filter_line_keys=['topic','pestle','insight','sector']
    countries = ['Venezuela', 'Norway', 'Poland', 'Cyprus', 'Nigeria', 'Burkina Faso', 'Belize', 'Saudi Arabia', 'Niger', 'United Arab Emirates', 'Kazakhstan', 'Turkey', 'Egypt', 'Azerbaijan', 'Denmark', 'Ghana', 'Ukraine', 'United Kingdom', 'Argentina', 'South Africa', 'Austria', 'Russia', 'Estonia', 'Spain', 'Liberia', 'Germany', 'Greece', 'Angola', 'Brazil', 'Iran', 'Oman', 'Libya', 'Kuwait', 'Jordan', 'Hungary', 'India', 'Syria', 'Qatar', 'Canada', 'Morocco', 'Algeria', 'Japan', 'Malaysia', 'Pakistan', 'China', 'Gabon', 'United States of America', 'South Sudan', 'Australia', 'Iraq', 'Indonesia', 'Colombia', 'Lebanon', 'Ethiopia', 'Mexico', 'Mali']
    for key in filter_line_keys:
        res = {"filter":f"line_{key}",
                "data":LinechartData(data=deepcopy(data),keyword=key)}
        filters.append(res)
        for country in countries:
            res = {"filter": f"line_{key}_{country}",
                    "data":LinechartData(data=deepcopy(data),keyword=key,country=country)}
            filters.append(res)
        
    new_collection.insert_many(filters)

if __name__ == '__main__':
    filterdata()
