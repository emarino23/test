import pandas as pd
import sys, os

ROOT_DIR = os.path.dirname(__file__)
FILE_PATH = os.path.join(ROOT_DIR,"tablas.xlsx")
df = pd.read_excel (FILE_PATH) #place "r" before the path string to address special character, such as '\'. Don't forget to put the file name at the end of the path + '.xlsx'
print (df)