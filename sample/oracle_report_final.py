""" Script to generate oracle report"""


"""Importing all required modules. """

import os
import cx_Oracle
import csv
import time
from datetime import date
import shutil

#logging time start
print("START of process")
print("-------------------------------------")
start_time = time.time()

#sql query declaration
SQL = open("C:\\Users\\vishal.raut\\Desktop\\jpmgcd.sql", 'r').read()
# print(SQL)

# SQL = ''' SELECT DISTINCT O.ACRONYM ,SI.* from alert.vw_si_data SI JOIN alert.ACCOUNT_MAP M
#           ON SI.account_id=m.account_id JOIN ALERT.ORGANIZATION O ON M.CUST_ID = O.ORGANIZATION_ID
#            WHERE M.MAP_TYPE = 'GC' AND M.CUST_ID in (7928) and rownum <1001 '''

#output file name creation
filename_datetime = "DATA_SEARCH_SI_JPMGCD_SI_CONTROLLER_" + str(date.today()) + ".csv"
#filename = "C:\\Users\\vishal.raut\\Desktop\\" + filename_datetime
filename = '\\\omnycsfs01\Applh\\Team Nebula\\Data Search Reports\\' + filename_datetime


#function to generate the header data
def db_fetch_header(SQL,filename_datetime,filename):
    try:
        connection = cx_Oracle.connect( 'vraut/Apr.2018!@aleprbdb01-m/ALPRCORE.OMGEO.COM' )
        print( "Connecting to the Oracle database....\n" )
        print("Connected to the database...Executing the report.......\n")
        cursor = connection.cursor()
        tmp = cursor.execute( SQL )
        columns = [i[0] for i in cursor.description]
        results = tmp.fetchall()
        FILE = open( filename, "w", newline='' );
        output = csv.writer( FILE, dialect='excel' )
        if results:
            output = csv.writer( FILE, dialect='excel')
            output.writerow(columns)
        else:
            cursor.close()
        FILE.close()
    except cx_Oracle.DatabaseError as err:
        print( "Error in header: {0}".format(err))
    except:
        print( "Other errors encountered." )
    finally:
        pass


#function to generate the actual data

def db_fetch_data(SQL,filename_datetime,filename):
    try:
        FILE = open( filename, "a", newline='' );
        output = csv.writer( FILE, dialect='excel' )
        connection = cx_Oracle.connect( 'vraut/Apr.2018!@aleprbdb01-m/ALPRCORE.OMGEO.COM' )
        cursor = connection.cursor()
        cursor.execute( SQL )
        for row in cursor:
            output.writerow( row )
        cursor.close()
        #connection.close()
        FILE.close()
        print( "Process completed in %s seconds ---" % (time.time() - start_time) )
    except cx_Oracle.DatabaseError as err:
        print( "Error in data fetch: {0}".format( err ) )
    except:
        print("Other errors encountered.")
    finally:
        print( "-------------------------------------" )
        print("END of process")



#excecute the functions
db_fetch_header(SQL,filename_datetime,filename)
db_fetch_data(SQL,filename_datetime,filename)

#In case putting the file on shared drive directly is not possible then copying it manually from desktop to shared drive
# target_dest = '\\\omnycsfs01\Applh\\Team Nebula\\Data Search Reports\\'
# shutil.copy(filename,target_dest)