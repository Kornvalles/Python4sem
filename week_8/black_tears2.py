import datetime as date
import pandas as pd
import pymysql as sql
from sqlalchemy import create_engine

con_str = 'mysql+pymysql://dev:ax2@localhost:3307/black_tears'
engine = create_engine(con_str)
connection = engine.raw_connection()

# Find antallet af crimes mellem to givne datoer i 2006
def find_crimes(start_date: date, end_date: date):
    df = pd.read_sql_table("Crime", con=engine)
    df['cdatetime'] = pd.to_datetime(df['cdatetime'])
    mask = (df['cdatetime'] > pd.Timestamp(start_date)) & (df['cdatetime'] <= pd.Timestamp(end_date))
    df = df.loc[mask]
    return df.to_dict('records')


found = find_crimes(date.datetime(2006,1,1,22),date.datetime(2006,1,1,23))
print(len(found))