# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 18:40:36 2021

@author: Jack
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 05:52:59 2021

@author: Jack I.
"""

import pandas as pd
import numpy as np
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows

# wb = load_workbook('D:/DataFileForSeismometer/Seismograph_Data.xlsx')
wb = load_workbook('./Seismograph_Data.xlsx')
ws = wb.active

col_names=['Date Time', 'Roll', 'Pitch', 'Direction Angle', 'Temperature']
# df = pd.read_csv('D:/DataFileForSeismometer/DATALOG2.csv', names=col_names, low_memory=False, encoding='utf-8', dtype={"Data Time": str, "Roll": str, "Pitch": str, "Direction Angle": str, "Temperature": str})
df = pd.read_csv('./DATALOG1.csv', names=col_names, low_memory=False, encoding='utf-8', dtype={"Data Time": str, "Roll": str, "Pitch": str, "Direction Angle": str, "Temperature": str})

#print(df)

#col_names=['Date Time', 'Roll', 'Pitch', 'Direction Angle', 'Temperature']
#df = pd.read_csv ('D:/DataFileForSeismometer/DATALOG2.csv', low_memory=False, names=col_names)
#df_1 = pd.DataFrame(df,columns=['Date Time', 'Roll', 'Pitch'])

df_1= df["Roll"]

#print(df_2)

#print(df_2.abs())
#df_1 = df_1.replace(np.nan, 'N/A', regex=True)

#df1['Count'] = 1
#df2 = df1.groupby(['DISTRICT', 'YEAR']).count()['Count'].unstack(level=0)

#print(df2)

#df2.drop(columns='N/A', inplace=True)
rows = dataframe_to_rows(df_1)
for r_idx, row in enumerate(rows,2):
   for c_idx, value in enumerate (row,1):
      ws.cell(row=r_idx, column=c_idx, value=value)

df1['Roll'].abs()

print(df1['Roll'].abs())
#wb.save('Seismograph_Data2.xlsx')
