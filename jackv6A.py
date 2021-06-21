# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 17:08:41 2021

@author: Jack
"""

import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import csv

def header(msg):
    print('-' * 50)
    print('[ ' + msg + ' ]')


# fn = "DATALOG2.csv"
# fn = "data_1k_lines.csv"
fn = "DATALOG2.csv"


# 2. read text file into a dataframe
header("2. read text file into a df")


col_names=['DateTime', 'Roll', 'Pitch', 'Direction', 'Temperature'] 


df = pd.read_csv(fn, names=col_names)
#df = pd.read_csv(fn) # read file without assigning col names in the frame


frame3 = pd.DataFrame(df,columns=['DateTime', 'Roll'])


# frame3 = (df['Roll'].astype(float))
# What's the reason you are using the "astype" funcition?


#################################################################
# Panda intro video:
# https://www.youtube.com/watch?v=e60ItwlZTKM

# WATCH THIS ^^^^^^ and do the examples one by one!


# Here is what you want explained in example 11:

# 11. iterate over rows
# header("11. df[df.col4 > 0.50], show only specific columns, filtered with condition")

# for index, row in df.iterrows():
#     if row['col4'] > 0.8 and row['col4'] < 1.0:
#         print(df.loc[index:index, ['Date', 'Time', 'col4', 'col6', 'col8', 'col10']])
#################################################################
for index, row in frame3.iterrows():
    if row['DateTime'] == '2021/4/22 06:33:34"':
        print("Found value in range", df.loc[index:index,['DateTime', 'Roll']])


#for index, row in frame3.iterrows():
 #   if row['Roll'] > 2.0 and row['Roll'] < 2.5:
  #      print("Found value in range", df.loc[index:index,['Roll', 'DateTime']])
