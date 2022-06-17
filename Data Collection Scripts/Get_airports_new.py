import requests
import datetime
import pandas as pd
import numpy as np

cities_df = pd.read_csv('cities.csv')
cities = cities_df['city']

airports = pd.DataFrame(columns=['city','city_id','lat','lon','icao','iata','name'])


for city in cities:
    lat = float(cities_df.loc[cities_df['city']==city]['Latitud'])
    lon = float(cities_df.loc[cities_df['city']==city]['Logitud'])

    url = f"https://aerodatabox.p.rapidapi.com/airports/search/location/{lat}/{lon}/km/50/16"
    
    querystring = {"withFlightInfoOnly":"0"}
    
    headers = {
            	"X-RapidAPI-Key": "2ef471dfcbmshec01fd033aae0e3p10a740jsn9a6d81f2bead",
            	"X-RapidAPI-Host": "aerodatabox.p.rapidapi.com"
            }
    
    response = requests.request("GET", url, headers=headers)#, params=querystring)
    print('Status code',response.status_code)
    airp_js = response.json()
    
    for a in airp_js["items"]:
        airports = airports.append({'city':city,
                      'city_id': cities_df[cities_df['city']==city].city_id.iloc[0],
                      'lat':a["location"]["lat"],
                      'lon':a["location"]["lon"],
                      'icao':a["icao"],
                      'iata':a["iata"],
                      'name':a["name"]
                      }
                      ,ignore_index=True)

        
airports.to_csv('airports_new.csv', index=False)
