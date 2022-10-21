# sourcing
import helper_functions as help_fnc
import psaptemp_largestIndex
import fragmented_indexes
import os
import time

#check calling user is oracle user
who_stream = os.popen('whoami')
user_id = who_stream.read()
if not (help_fnc.isOracleUser(user_id)):
    user_id = user_id.rstrip() #avoiding newline while concatenating
    print(user_id + " is not an oracle user please run the script with an appropriate user")
    quit()
else: 
    user_id = user_id.rstrip() #avoiding newline while concatenating
    print(user_id + " is an appropriate user continuing ...")

time.sleep(1) # seconds sleep

###
#Check if psaptemp is larger than the largest index
###

# run the sql
sql_scriptname = "psaptemp_largestIndex"

if help_fnc.run_sql(sql_scriptname): 
    print("SQL report written to /tmp/" + sql_scriptname)
    time.sleep(1)
    print("")
    print("")
    print("Continuing evaluating results ...")
    print("")
    print("")
# execute the check

print(psaptemp_largestIndex.exec())

sql_scriptname = "fragmented_Indexes"

if help_fnc.run_sql(sql_scriptname): 
    print("SQL report written to /tmp/" + sql_scriptname)
    time.sleep(1)
    print("")
    print("")
    print("Continuing evaluating results ...")
    print("")
    print("")

brspace_command = fragmented_indexes.exec()

if brspace_command == "":
    print("no fragmented indexes found")
else: 
    print("Fragmented indexes found execute the following command to rebuild: " + brspace_command)

