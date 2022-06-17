import pandas as pd
import requests
import sqlalchemy
import config as cfg



schema="gans"
host=cfg.DATABASE_HOST
user=cfg.DATABASE_USER
password=cfg.DATABASE_PASSWORD
port=cfg.DATABASE_PORT
con = f'mysql+pymysql://{user}:{password}@{host}:{port}/{schema}'

path='/Users/jlma/Documents/Curso de Data Science/5-Data Engineer/Project3/Project3_TEAM4_Repo/WBS_Project3/Data Collection Scripts/'

#cities_df = pd.read_csv(path+'cities.csv')
#cities_df.to_sql('cities', 
#              if_exists='append', 
#              con=con, 
#              index=False)

#weather = pd.read_csv(path+'weather.csv')
#weather.to_sql('weathers', 
#              if_exists='append', 
#              con=con, 
#              index=False)

#airports = pd.read_csv(path+'airports.csv')
#airports.to_sql('airports', 
#              if_exists='append', 
#              con=con, 
#              index=False)

#flights = pd.read_csv(path+'flights.csv')
#flights.to_sql('flights', 
#              if_exists='append', 
#              con=con, 
#              index=False)