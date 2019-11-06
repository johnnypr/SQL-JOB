import sqlite3
import pandas as pd
from pandas import DataFrame

# Connect to the database 
connection = sqlite3.connect("INDUSTRYCODES.db")
cursor = connection.cursor()


read_companies = pd.read_csv (r'/Users/johnnyperez/Desktop/SQL JOB/Excel Sheets/PROJECT 2/Excel Parser/data.csv')
read_companies.to_sql('DATA', connection, if_exists='append', index = False) 


df = DataFrame(cursor.fetchall(), columns=['company_name','company_id'])
print (df)