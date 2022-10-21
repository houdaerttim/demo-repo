import isOracleUser as isOra
import os
import time
import datetime as dt
import re
import shutil
import csv

# Initialize
# TODO: read from list
list_scripts = ["redologsPerHour", "largestTables", "SystemStatisticsLGWR", "spaceTablespaces", "fragmentedIndexes"]

#check userid is oracle user
#TODO: move to upper
who_stream = os.popen('whoami')
user_id = who_stream.read()
sid = ""
user_id = user_id.rstrip()
if not (isOra.isOracleUser(user_id)):
    print(user_id + " is not an oracle user please run the script with an appropriate user")
    quit()
else: 
    print(user_id + " is an appropriate user continuing ...")
    sid = user_id[-3:]
time.sleep(1) # seconds sleep

def run_sql(scriptname):
    sql_command = "sqlplus / as sysdba @./sql/"+ scriptname + ".sql"
    print("executing " + sql_command + " ...")
    time.sleep(1)
    #execute sql_command
    os.system(sql_command)
    time.sleep(1)
    #TODO: evaluate sqlexecution
    print("SQL executed correctly ....")
    return True

def move_rename_csv(scriptname, sid):
    ## Variables
    # Original csvname in /tmp
    csv_name = "/tmp/" + scriptname + ".csv"
    # Get Timestamp
    now = dt.datetime.now()
    timeStamp =  now.strftime("%Y%m%d"+"T"+"%H%M%S")
    new_csv_name = "/usr/sap/depot/scripts/oracle_po_performance/csv/" + scriptname + "_" +timeStamp + "_" + sid.upper() + ".csv"
    # Execute
    print("Copying results to " + new_csv_name + " ...")
    shutil.copy(csv_name, new_csv_name)
    return True

# Run scripts
for scriptname in list_scripts:
    if run_sql(scriptname): 
        print("SQL report written to /tmp/" + scriptname + ".csv")
    else:
        print("An error has occured, exiting...") 
        exit()
    if move_rename_csv(scriptname, sid):
        print(scriptname + "script is executed and csv copied ...")
    else:
        print("An error has occured, exiting...") 
        exit()