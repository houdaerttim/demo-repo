import isOracleUser as isOra
import os
import time
import datetime as dt
import re
import shutil
import csv

#check userid is oracle user
#TODO: move to upper
who_stream = os.popen('whoami')
user_id = who_stream.read()
user_id = user_id.rstrip()
sid = ""
print(user_id)
if not (isOra.isOracleUser(user_id)):
    print(user_id + " is not an oracle user please run the script with an appropriate user")
    quit()
else: 
    print(user_id + " is an appropriate user continuing ...")
    sid = user_id[-3:]
time.sleep(1) # seconds sleep