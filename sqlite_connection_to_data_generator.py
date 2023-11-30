import sqlite3
import pandas as pd

# Read the csv file into a pandas dataframe
df = pd.read_csv('my_data.csv')


# Create a connection to the sqlite database
conn = sqlite3.connect('data_connector.db')

# Write the dataframe to a table in the database
df.to_sql('my_table', conn, if_exists='replace', index=False)

# Close the connection to the database
conn.close()