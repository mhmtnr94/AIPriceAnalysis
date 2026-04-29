import pandas as pd
import sqlite3

# 1. Read the Excel file (Updated file name)
df = pd.read_excel('sales.xlsx')

# 2. DATA CLEANING
df_clean = df[df['Quantity'] > 0].copy()
df_clean['UnitPrice'] = df_clean['UnitPrice'].fillna(5000.0)
df_clean['TotalRevenue'] = df_clean['Quantity'] * df_clean['UnitPrice']

# 3. SAVE TO SQL DATABASE
# Create a connection to SQLite database (it creates the file if it doesn't exist)
conn = sqlite3.connect('sales_database.db')

# Write the DataFrame to a SQL table named 'sales_table'
df_clean.to_sql('sales_table', conn, if_exists='replace', index=False)

# Close the connection
conn.close()

print("Data successfully cleaned and saved to 'sales_database.db'!")