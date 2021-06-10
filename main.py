# -*- coding: utf-8 -*-
# 
# Panda intro video:
# https://www.youtube.com/watch?v=e60ItwlZTKM
#

#################################################################
# import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import csv

#################################################################
def header(msg):
    print('-' * 50)
    print('[ ' + msg + ' ]')


#################################################################
def main():


    #################################################################
    # 2. read text file into a dataframe
    header("2. read text file into a df")

    # Have one place to set the file name to a var. Use the variable
    # everywhere else in the program.
    fn = "data.csv"

    # example row:
    # 2021/3/29,"11:54:7""",,0.98,,0.15,,127.01,,23.03
    # has 9 "," therfor 10 columns/fields
    # date, time, col3, col4, col5, col6, col7, col8, col9, col10
    #
    # ! time has an extra set of "", don't know what that's about,
    # col3 has no values
    # col5 has no values
    # col7 has no values
    # col9 has no values
    #
    # So it makes sense to only operate on 1,2,4,6,8,10

    col_names = ['Date', 'Time', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8', 'col9', 'col10']

    df = pd.read_csv(fn, names=col_names)

    # Print the entire frame, so all of the data in the file, rows x columns.
    # print(df)

    #################################################################
    # 3. Print first 5 or last 3 rows
    # header("3. df.head()")
    # print(df.head())

    # header("3. df.tail(3)")
    # print(df.tail(3))

    #################################################################

    #################################################################
    # 5, statistical summary of each column
    # header("5. df.describe()")
    # print(df.describe())

    #################################################################
    #

    #################################################################
    # 7, Show/slice only the columns of interest
    # header("7. df[[]], show only specific columns")
    # print(df[['Date', 'Time', 'col4', 'col6', 'col8', 'col10']])

    #################################################################
    # 7, Show/slice only the columns of interest, and only a range of rows
    # header("7. df.loc[[]], show only specific columns")
    # print(df.loc[0:15, ['Date', 'Time', 'col4', 'col6', 'col8', 'col10']])

    #################################################################
    # 8, filtering
    header("8. df[(df['col4'] > 0.50) & (df['col4'] < 0.9)], show only specific columns, filtered with condition(s)")
    # print rows where col4 is in range of 0.5 - 0.9
    print(df[(df['col4'] > 0.50) & (df['col4'] < 0.9)])


    # df[(df['col1'] >= 1) & (df['col1'] <=1 )]
    #################################################################
    # 11. iterate over rows
    # header("11. df[df.col4 > 0.50], show only specific columns, filtered with condition")
    # # First 27 rows get removed

    # for index, row in df.iterrows():
    #     if row['col4'] > 0.8 and row['col4'] < 1.0:
    #         print(df.loc[index:index, ['Date', 'Time', 'col4', 'col6', 'col8', 'col10']])


    #################################################################



    #################################################################
    #################################################################
    #################################################################



#################################################################
if __name__ == "__main__":
    main()
