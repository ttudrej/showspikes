#12 June 21: I need to make this code work. I'll check out the other code later. In the mean time I keep getting this erro message as follows
#TypeError: '>' not supported between instances of 'str' and 'float'
#I tried to rectify the problem with no success.
#The problem is in the for loop. Let me know when you get a chance.



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
col_names=['Date Time', 'Roll', 'Pitch', 'Direction', 'Temperature'] 
df = pd.read_csv('DATALOG2.csv', names=col_names)
#df = pd.read_csv(fn)
print(df)


# 3. Print first 5 or last 3 rows
#header("3. df.head()")
#print(df.head())
#header("3. df.tail(3)")
#print(df.tail(3))

frame2 = pd.DataFrame(df,columns=['Date Time','Roll','Pitch'])
print (frame2)

frame3 = pd.DataFrame(df,columns=['Roll'])

frame3.loc[7658]

#frame2.loc[1620577]
#frame2.T
#print(frame2) 
frame3 = (df['Roll'].astype(float))

for x in 'Roll':                #pgs. 47, 48 in 2018 Wes McKinny book
    if (x > 1.00) & (x < 3.00):
        print('Found')
        print(x)
        print(frame3.loc[x])
        #break
    else:
        print ('Not Found')    
        print(x)
        print(frame3.loc[x])

#################################################################
if __name__ == "__main__":
    main()
