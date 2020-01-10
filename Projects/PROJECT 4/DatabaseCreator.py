import sqlite3
import pandas as pd


# Make a database of Excel Sheet
connection = sqlite3.connect("COMPANY_INFO.db")
cursor = connection.cursor()

          
#Creating a Table of Company Names
cursor.execute('''CREATE TABLE COMPANY_INFO
             ([generated_id] INTEGER PRIMARY KEY,
             [START$] text,[END$] text,[REV$] text,[ID] text,
             [NAME] text,[NAME_NATIVE_LANG] text,[ACTIVE] text,[COVERED] text,
             [TICKER] text,[INVESTOR_CONTACT_NAME] text,[HOME_REGION] text,[CUSIP] text,
             [ISIN] text,[SEDOL] text,[VALOREN] text,[EU_CODE] text,[XS_CODE] text,[PROFILE_END_DATE] text,[TICKER_EXCHANGE] text)''')
connection.commit()

cursor.execute('''CREATE TABLE COMPANIES
             ([generated_id] INTEGER PRIMARY KEY,[Company_Name] text,[Company_ID] integer)''')


# ""START$"",""END$"",""REV$"",""ID"",""NAME"",""NAME_NATIVE_LANG"",""ACTIVE"",""COVERED"",""TICKER"",
# ""INVESTOR_CONTACT_NAME"",""HOME_REGION"",""CUSIP"",""ISIN"",""SEDOL"",
# ""VALOREN"",""EU_CODE"",""XS_CODE"",""PROFILE_END_DATE"",""TICKER_EXCHANGE""