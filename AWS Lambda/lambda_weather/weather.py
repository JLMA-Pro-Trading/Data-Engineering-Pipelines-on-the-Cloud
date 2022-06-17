import requests
from datetime import datetime
import pandas as pd
import config as cfg

def get_weather():
    schema="gans"
    host=cfg.DATABASE_HOST
    user=cfg.DATABASE_USER
    password=cfg.DATABASE_PASSWORD
    port=cfg.DATABASE_PORT
    con = f'mysql+pymysql://{user}:{password}@{host}:{port}/{schema}'
    
    cities_df = pd.read_sql('cities',con=con)
    
    cities = cities_df['city']
    API_key = cfg.WEATHER_API_KEY
    weather = pd.DataFrame(columns=['city_id',
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
                
            weather=weather.append({'city_id': cities_df[cities_df['city']==city].city_id.iloc[0],      
                          'time_utc':x["dt"],
                          'local_time':datetime
                                      .utcfromtimestamp(x["dt"]+
                                                        int(cities_df[cities_df['city']==city].time_zone))
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
    
    weather.to_sql('weathers', 
               if_exists='append', 
               con=con, 
               index=False)
