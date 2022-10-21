#cleanup header
#imports
from pathlib import Path
from ast import increment_lineno
import os
import datetime as dt
import re
import shutil
import csv
import pandas as pd
import sys

#Functions
def cleanup_csv (file_path):
    # strip spaces from csv
    # Read csv file into dataframe
    ### sep '\s*,\s*' - remove all spaces while reading
    ### https://stackoverflow.com/questions/14885908/strip-white-spaces-from-csv-file
    df = pd.read_csv(file_path, sep='\s*;\s*', engine = 'python')
    # Remove "---" row from header
    df.drop(0, inplace=True)
    #filename without ext
    pathname = os.path.dirname(file_path)
    filename = os.path.splitext(os.path.basename(file_path))[0]
    extension = os.path.splitext(os.path.basename(file_path))[1]
    helper_name = filename.split("_")
    result_name = pathname + "/" + helper_name[2] + "/" + helper_name[0] + "_" + helper_name[1][0:8] + extension
    #print(helper_name[1][0:8])
    #result_file_name = helper_name[0] + 
    # write to csv
    df.to_csv(result_name, sep=';' , index=False )
    print(result_name + " written")
    #move to cleaned
    move_target = pathname + "/cleaned/" + helper_name[0] + "_" + helper_name[1][0:8] + "_" + helper_name[2] + extension
    shutil.move(file_path, move_target)

# get file directory
dir_path = os.path.dirname(os.path.realpath(__file__))
#csv_data_dir = "/usr/sap/depot/scripts/oracle_po_performance/csv/"
csv_source_dir = dir_path + "/csv/"
csv_files = os.listdir(csv_source_dir)
#perform cleanup
for file in csv_files:
    if not os.path.splitext(os.path.basename(file))[1] == ".csv": # file should be csv
        print(file + " is not an csv file, skipping ...")
        continue
    if not len(file.split("_")) == 3: # file shoud have exact 2 underscores
        print(file + "has no valid filename value 'script_YYYMMDD_SID.csv' ")
        continue
    file_path = csv_source_dir + file
    #print("File to be cleanes= " + file_path)
    cleanup_csv(file_path)
exit()