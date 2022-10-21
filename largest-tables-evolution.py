import csv
import os
import pandas as pd
import numpy as np
import csv


sid = "XA4"

#Functions
def evaluate_csv(file):
    filename_no_ext = os.path.splitext(os.path.basename(file))[0] #separate filename from path
    datevalue = filename_no_ext.split("_")[1] #split filename and extract date
    #open alreadyavaluated dates
    print(file)
    #if date is already evaluated - skip
    
    df = pd.read_csv(file)
    print("debug")
    
    
    

    # evaluate csv file - write into resultfile
    
    #store csvdate in separate list (file)

# get file directory
dir_path = os.path.dirname(os.path.realpath(__file__))
#csv_data_dir = "/usr/sap/depot/scripts/oracle_po_performance/csv/"
csv_source_dir = dir_path + "\\csv\\" + sid + "\\"
csv_files = os.listdir(csv_source_dir)
for file in csv_files:
    if not file[-4:]==".csv": #skip non csv
        print(file + " Skipped")
        continue
    if not file[:13]=="largestTables": # skip non largest tables files
        print(file + " Skipped")
        continue
    evaluate_csv(csv_source_dir + file)

print("debug")










