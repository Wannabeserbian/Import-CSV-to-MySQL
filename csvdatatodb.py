import pandas as pd
import glob
import os
from sqlalchemy import create_engine

list_of_files = glob.glob('./csv files/*.csv')
latest_file = max(list_of_files, key=os.path.getctime)
print(latest_file)


column_names = ['country','sp_rating','moodys_rating','fitch_rating','dbrs_rating','te_rating']

dataframe = pd.read_csv(latest_file, header = None, names = column_names)
# Drop Headers from csv file
dataframe.drop([0], inplace = True)
print(dataframe)

# Change USERNAME,PASSWORD and DB_NAME with your username , password and DB_NAME
engine = create_engine('mysql://USERNAME:PASSWORD@localhost/DB_NAME')
with engine.connect() as conn, conn.begin():
    print('Connection with engine is opened')
    # Change TABLE_NAME with a name of your choice
    dataframe.to_sql('TABLE_NAME', conn, if_exists='replace', index=True)
    print('Table successfully created')

conn.close()
print('Connection closed')

