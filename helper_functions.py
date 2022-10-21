import os
import time

# check if if user is an oracle user (naming convention oraxxx)
def isOracleUser(user_id):
    s = "oraxs1"
    if not(len(s) == 6 and s.find("ora",0,3) == 0) :
        return False
        #(f" {s} is not an oracle user")
    else:
        return True
        #(f"Ok go, {s} is an Oracle User")

# run sqlfile
def run_sql(sqlname):
    sql_command = "sqlplus / as sysdba @./sql/"+ sqlname + ".sql"
    print("executing " + sql_command + " ...")
    time.sleep(1)
    #execute sql_command
    os.system(sql_command)
    time.sleep(1)
    #TODO: evaluate sqlexecution
    print("SQL executed correctly ....")
    print("")
    print("") 
    return True

