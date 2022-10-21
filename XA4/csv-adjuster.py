import csv
import pandas as pd
import shutil
file_name = "spaceTablespaces_20221019.csv"
separator = ','
df = pd.read_csv(file_name, sep='\s*'+ separator + '\s*', engine = 'python')
result_name = file_name + ".new"
df.to_csv(result_name, sep=';' , index=False )
shutil.move(result_name, file_name)