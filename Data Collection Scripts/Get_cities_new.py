import geocoder
import pandas as pd

wc = pd.read_csv('world_cities.csv')
countries= pd.read_csv('EuroCitiesPopulation15_.csv').country
cities = pd.read_csv('EuroCitiesPopulation15_.csv').name

city_id=[]
for co,ci in zip(countries,cities):
    city_id=city_id+[(wc.set_index('country').loc[co].set_index('name').loc[ci].geonameid)]
    
    
lat=[]
lng=[]
population=[]
country_code=[]
time_zone=[]
east=[]
south=[]
north=[]
west=[]

for c in city_id:

    # DATA COLLECTION:

    g = geocoder.geonames(c, method='details', key='jlma_ve84')
    lat             = lat+[(g.geojson['features'][0]['properties']['lat'])]
    lng             = lng+[(g.geojson['features'][0]['properties']['lng'])]
    population      = population+[(g.geojson['features'][0]['properties']['population'])]
    country_code    = country_code+[(g.geojson['features'][0]['properties']['country_code'])]
    time_zone       = time_zone+[3600*(g.geojson['features'][0]['properties']['raw']['timezone']['gmtOffset'])]
    east            = east+[(g.geojson['features'][0]['properties']['raw']['bbox']['east'])]
    south           = south+[(g.geojson['features'][0]['properties']['raw']['bbox']['south'])]
    north           = north+[(g.geojson['features'][0]['properties']['raw']['bbox']['north'])]
    west            = west+[(g.geojson['features'][0]['properties']['raw']['bbox']['west'])]  
    
cities_dic = {'city_id': city_id,
              'city': cities, 
              'country':countries, 
              'Code': country_code, 
              'Population': population, 
              'Time_Zone': time_zone, 
              'Latitud': lat, 
              'Logitud': lng, 
              'East': east, 
              'South': south, 
              'North': north, 
              'West': west}
cities_df  = pd.DataFrame.from_dict(cities_dic)
cities_df.to_csv('cities.csv', index=False) 
