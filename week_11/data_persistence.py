# insert, update, delete
from __future__ import print_function

import pymysql
from decimal import Decimal
from datetime import datetime, date, timedelta
import pandas as pd
from sqlalchemy import create_engine #sqlalchemy helped convert strings to dates seamlessly

#cnx = pymysql.connect(user='dev', password='ax2',host='127.0.0.1',port=3307,db='test') 
con_str = 'mysql+pymysql://dev:ax2@localhost:3307/test'
engine = create_engine(con_str)

df = pd.read_csv('cars.csv')

#df = df.applymap(str)
df.to_sql('cars',con=engine, if_exists='append', index = False)
print(engine)