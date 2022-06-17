import requests
import datetime
import pandas   as pd
import numpy    as np
import config   as cfg

def get_flights():
    schema="gans"
    host=cfg.DATABASE_HOST
    user=cfg.DATABASE_USER
    password=cfg.DATABASE_PASSWORD
    port=cfg.DATABASE_PORT
    con = f'mysql+pymysql://{user}:{password}@{host}:{port}/{schema}'

    #airports= pd.read_sql('airports',con=con)

    flights = pd.DataFrame(columns=['icao','date','hour_day','num_of_arriv','num_of_depart'])

    hour_day= ['00-01','02-03','03-04','04-05','05-06','06-07','07-08','08-09','09-10','10-11','11-12',
            '12-13','13-14','14-15','15-16','16-17','17-18','18-19','19-20','20-21','21-22','22-23','23-00']

    air=['LPPR']

    for a_icao in air:# airpotrs['icao']:

        date = (datetime.date.today() + datetime.timedelta(days=1)).strftime('%Y-%m-%d') 
        t1=['00:00','12:00']
        t2=['11:59','23:59']
        
        headers = {
            "X-RapidAPI-Host": "aerodatabox.p.rapidapi.com",
            "X-RapidAPI-Key": cfg.RAPIDAPI_KEY
        }
        flight_js = list()
        for i in range(2):
            url = f"https://aerodatabox.p.rapidapi.com/flights/airports/icao/{a_icao}/{date}T{t1[i]}/{date}T{t2[i]}"
            
            response = requests.request("GET", url, headers=headers)
            print('Status code',response.status_code)
            if response.status_code!=200:
                print("ERROR to communcate with the flights API")
                break
            else:
                temp_flight_js = response.json()
                flight_js.append(temp_flight_js)
            
        # CALCULATE THE ARRIVAL AND DEPARTURES CATEGORIES OF THE DAY:
        
        def getTime(list, json, f_js, arrORdep):
            from datetime import datetime
            [date,time_]=(f_js[list][arrORdep][json]['movement']['scheduledTimeLocal']).split()
            [time_,summerdelta]= time_.split('+')
            time_=datetime.strptime(time_,'%H:%M').time()
            return time_
        
        def getTrafficPerHour(listOfFlights):
            arrivalsPerHour = [0]*24
            for i in range(len(listOfFlights)):
                h_a = listOfFlights[i].hour
                arrivalsPerHour[h_a] +=1
            return arrivalsPerHour

        a_times_series = []; d_times_series = []
        for i_list in range(len(flight_js)):
            for i_json_a,i_json_d in zip((range(len(flight_js[i_list]['arrivals']))),(range(len(flight_js[i_list]['departures'])))):
                a_times_series.append(getTime(i_list, i_json_a,flight_js,'arrivals'))
                d_times_series.append(getTime(i_list, i_json_d,flight_js,'departures'))

        a_l= getTrafficPerHour(a_times_series)        
        d_l= getTrafficPerHour(d_times_series)

        # CREATE THE DATAFRAME OF ARRIVAL & DEPARTURE FLIGHTS PER: AIRPORT,DAY,HOUR:

        for a,d,c in zip(a_l,d_l,hour_day):
            flights = flights.append({'icao':a_icao,
                            'date':date,
                            'hour_day':c,
                            'num_of_arriv':a,
                            'num_of_depart':d
                            }
                            ,ignore_index=True)

        # PUSH THE FLIGHTS DATA TO THE DATABASE:

        flights.to_sql('flights', 
                    if_exists='append', 
                    con=con, 
                    index=False)
