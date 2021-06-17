"""
Created on Fri Jun  4 06:47:24 2021

@author: Jack
>>>I'm having trouble with the for oop at the bottom. It Run it and see what it gives you. The value of value does not change although it must  scroll though every
>>>value in the data file. Le me know when you get a chance.

"""

import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import csv

def header(msg):
    print('-' * 50)
    print('[ ' + msg + ' ]')


# 2. read text file into a dataframe
header("2. read text file into a df")
fn = "DATALOG2.csv"
col_names=['DateTime', 'Roll', 'Pitch', 'Direction', 'Temperature'] 
df = pd.read_csv('DATALOG2.csv', names=col_names)
#df = pd.read_csv(fn)
print(df)


# 3. Print first 5 or last 3 rows
#header("3. df.head()")
#print(df.head())
#header("3. df.tail(3)")
#print(df.tail(3))

frame2 = pd.DataFrame(df,columns=['DateTime','Roll','Pitch'])
print (frame2)

frame3 = pd.DataFrame(df,columns=['Roll'])

#frame3.loc[7658]

#frame2.loc[1620577]
#frame2.T
#print(frame2) 
frame3 = (df['Roll'].astype(float))

for value in frame3: 
    i  = 0
    while i >= 0:
        print(i)
        i += 1       
        if (2.5 > value > 2.0):
            print('Found')
            print(value)
            #print(i)
            print(frame3.loc[i])
                #break
        else:
            print ('Not Found')    
            print(value)
           #print(i)
