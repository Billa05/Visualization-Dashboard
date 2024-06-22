from pymongo import MongoClient


def HeatmapData(data):
    heatmapData=[]

    client = MongoClient("mongodb+srv://workinguse5:Biresh%402005@cluster0.hlgzx3g.mongodb.net/")

    db = client['Blackcoffer']
    collection = db['Dashboard']

    # Create a set to keep track of processed countries and regions to avoid duplicates
    processed_places = set()

    for document in data:
        country = document.get("country")
        region = document.get("region")

        # Skip documents without country or region
        if not country and not region:
            continue

        # Process by country
        if country and country not in processed_places:
            processed_places.add(country)
            filterdata = list(collection.find({"country": country}))
            heatmapData.append(create_data_entry(country, filterdata))

        # Process by region
        if region and region not in processed_places:
            processed_places.add(region)
            filterdata = list(collection.find({"region": region}))
            heatmapData.append(create_data_entry(region, filterdata))

    return heatmapData

def create_data_entry(place, filterdata):
    innerdata = [
        {"x": "Intensity", "y": max([data.get("intensity") for data in filterdata if type(data.get("intensity")) == int])},
        {"x": "Likelihood", "y": max([data.get("likelihood") for data in filterdata if type(data.get("likelihood")) == int])},
        {"x": "Relevance", "y": max([data.get("relevance") for data in filterdata if type(data.get("relevance")) == int])}
    ]
    return {"id": place, "data": innerdata}