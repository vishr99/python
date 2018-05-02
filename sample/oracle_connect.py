"""Connect to the Oracle database using python"""


import os
import cx_Oracle
import csv
import time
from datetime import date

# SQL command to extract the report WHATEVER.csv
start_time = time.time()
SQL = ''' SELECT DISTINCT O.ACRONYM ,SI.* from alert.vw_si_data SI JOIN alert.ACCOUNT_MAP M
          ON SI.account_id=m.account_id JOIN ALERT.ORGANIZATION O ON M.CUST_ID = O.ORGANIZATION_ID
           WHERE M.MAP_TYPE = 'GC' AND M.CUST_ID in (7928) and rownum<10001'''

#timestamp

filename_datetime = "REPORT-" + str(date.today()) + ".csv"
print(filename_datetime)
#output_sile
filename = "C:\\Users\\vishal.raut\\Desktop\\" + filename_datetime
FILE = open(filename,"w",newline='');
output = csv.writer(FILE, dialect='excel')

#connection with Oracle DB
print ("Connecting to the Oracle database..")
connection = cx_Oracle.connect('vraut/Apr.2018!@aleprbdb01-m/ALPRCORE.OMGEO.COM')

cursor = connection.cursor()
cursor.execute(SQL)
for row in cursor:
	output.writerow(row)
cursor.close()
connection.close()
FILE.close()


print("END of extraction")
print("--- %s seconds ---" % (time.time() - start_time))

