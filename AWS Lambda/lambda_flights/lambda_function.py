import json
import requests
from datetime import datetime
import pandas as pd
import sqlalchemy
import flights

def lambda_handler(event, context):
      
    flights.get_flights()

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
