import sqlite3
import pandas as pd
from pandas import DataFrame

# Connect to the database 
connection = sqlite3.connect("COMPANY_INFO.db")
cursor = connection.cursor()


read_companies = pd.read_csv (r'/Users/johnnyperez/Desktop/SQL JOB/Projects/PROJECT 4/fixed_CSV.csv')
read_companies.to_sql('COMPANY_INFO', connection, if_exists='append', index = False) 

df = DataFrame(cursor.fetchall(), columns=['START$','END$','REV$','ID','NAME',
'NAME_NATIVE_LANG','ACTIVE','COVERED','TICKER','INVESTOR_CONTACT_NAME','HOME_REGION','CUSIP',
'ISIN','SEDOL','VALOREN','EU_CODE','XS_CODE','PROFILE_END_DATE','TICKER_EXCHANGE'])
print(df)
