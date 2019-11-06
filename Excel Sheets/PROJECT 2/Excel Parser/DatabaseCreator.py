import sqlite3
import pandas as pd


# Make a database of Excel Sheet
connection = sqlite3.connect(".db")
cursor = connection.cursor()

          
#Creating a Table of Company Names
cursor.execute('''CREATE TABLE COMPANIES
             ([generated_id] INTEGER PRIMARY KEY,[Company_Name] text,[Company_ID] integer)''')
connection.commit()



 
