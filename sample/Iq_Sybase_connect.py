"""This module will connect to the sybase database."""
import ctypes
import sqlanydb
import pyodbc
# Create a connection object, then use it to create a cursor
con = sqlanydb.connect(uid = "vraut" ,pwd = "Mar21Pass" , host = "10.70.142.125:2066" , dbn = "IQPROD")

# Execute a SQL string
sql = "SELECT * FROM dummy"
cursor = con.cursor()
cursor.execute(sql)

# Get a cursor description which contains column names
desc = cursor.description
print(len(desc))


pyodbc.