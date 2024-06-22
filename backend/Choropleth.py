def ChoroplethData(data, keyword):
    highestValues = {}
    
    for doc in data:
        value = doc.get(keyword)
        if value:  # Ensure there's a value for the keyword
            country = doc.get("country", "")
            if country == "United States of America":
                country_code = "USA"
            elif country == "":
                country_code = "UNKNOWN"  # Set to UNKNOWN if country is empty
            else:
                country_code = country[0:3].upper()
            
            # Check if this country's initial is already encountered and if the current value is higher
            if country_code in highestValues:
                if value > highestValues[country_code]["value"]:
                    highestValues[country_code] = {"id": country_code, "value": value}
            else:
                highestValues[country_code] = {"id": country_code, "value": value}
                
    # Convert the dictionary to the list format required
    formattedData = list(highestValues.values())
    
    return formattedData