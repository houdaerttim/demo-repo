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

#Variables
csv_data_dir = "c:\\Lokaal\\SCRIPTS\\python\\python_po\\csv\\"
csv_source_file_name = "redologsPerHour_20221012T090308_XA4.csv"
file_path = csv_data_dir + csv_source_file_name

def cleanup_csv (file_path):
    # strip spaces from csv
    # Read csv file into dataframe
    ### sep '\s*,\s*' - remove all spaces while reading
    ### https://stackoverflow.com/questions/14885908/strip-white-spaces-from-csv-file
    df = pd.read_csv(file_path, sep='\s*,\s*')
    # Remove "---" row from header
    df.drop(0, inplace=True)
    #filename without ext
    pathname = os.path.dirname(file_path)
    filename = os.path.splitext(os.path.basename(file_path))[0]
    extension = os.path.splitext(os.path.basename(file_path))[1]
    helper_name = filename.split("_")
    result_name = pathname + "\\" + helper_name[0] + "_" + helper_name[1][0:8] + "_" + helper_name[2] + extension
    print(helper_name)
    #result_file_name = helper_name[0] + 
    # write to csv
    df.to_csv(result_name, index=False)

#run
cleanup_csv(file_path)