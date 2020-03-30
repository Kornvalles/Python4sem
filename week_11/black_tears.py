import pymysql as sql
import pandas as pd
from sqlalchemy import create_engine

# Connection to the database
cnx = sql.Connect(user='dev', password='ax2',host='127.0.0.1',port=3307,db='black_tears')

# Cursor to interact with database
cursor = cnx.cursor()

crime = pd.read_csv('SacramentocrimeJanuary2006.csv')

con_str = 'mysql+pymysql://dev:ax2@localhost:3307/black_tears'
engine = create_engine(con_str)
connection = engine.raw_connection()

crime = crime.applymap(str)
crime.to_sql('Crime',con=engine, if_exists='append', index=False)