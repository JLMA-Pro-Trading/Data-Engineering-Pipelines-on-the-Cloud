import requests
from datetime import datetime
import pandas as pd

#path = '..\Data\\'

cities_df = pd.read_csv('cities.csv')

cities = cities_df['city']
API_key = "689dc025ff4484f013a9e17b1395e687"
weather = pd.DataFrame(columns=['city',
                                'city_id',
                                'time_utc',
                                'local_time',
                                'temperature',
                                'humidity',
                                'cloudiness_pc',
                                'wind_speed',
                                'precipitation_prob',
                                'rain_volume',
                                'snow_volume'])
    
for city in cities:
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_key}&units=metric"
    
    response = requests.get(url)
    js = response.json()
   
    for x in js["list"]:
        try:
            rain_vol = x["rain"]["3h"]
        except KeyError as e1:
            #print('I got a KeyError - reason "%s"' % str(e1))
            rain_vol = 0
            
        try:
            snow_vol = x["snow"]["3h"]
        except KeyError as e2:
            #print('I got a KeyError - reason "%s"' % str(e2))
            snow_vol = 0
            
        weather=weather.append({'city':city,
                      'city_id': cities_df[cities_df['city']==city].city_id.iloc[0],      
                      'time_utc':x["dt"],
                      'local_time':datetime
                                  .utcfromtimestamp(x["dt"]+
                                                    int(cities_df[cities_df['city']==city].Time_Zone))
                                  .strftime('%Y-%m-%d %H:%M:%S'),
                      'temperature':x["main"]["temp"],
                      'humidity':x["main"]["humidity"],
                      'cloudiness_pc':x["clouds"]["all"],
                      'wind_speed':x["wind"]["speed"],
                      'precipitation_prob':x["pop"],
                      'rain_volume':rain_vol,#x["rain"]["3h"],
                      'snow_volume':snow_vol#x["snow"]["3h"]
                      }
                     ,ignore_index=True)

weather.to_csv('weather.csv', index=False)



