import os
import pandas as pd
import time
import datetime

import mysql.connector
from sqlalchemy import create_engine
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt


'''
year_folder
    day_csv_file
'''

csv_path = "D:\__DUMP__\\raw_data\\"

'''
select max(date) from test_metadata;
select min(date) from test_metadata;


# TODO get into one nested comprehension list
folder_list = sorted([os.path.join(csv_path, folder) for folder in os.listdir(csv_path)])
first_date = sorted([os.path.split(file)[1][:-4] for file in os.listdir(folder_list[0])])[0]
last_date = sorted([os.path.split(file)[1][:-4] for file in os.listdir(folder_list[-1])])[-1]

print(first_date, last_date)
first_date = datetime.datetime.strptime(first_date, "%Y-%m-%d")
last_date = datetime.datetime.strptime(last_date, "%Y-%m-%d")
print(first_date, last_date)

# https://pandas.pydata.org/pandas-docs/stable/timeseries.html
days = pd.date_range(start=first_date, end=last_date)  # lenght = 1908
print(days)
'''

engine = create_engine('mysql+mysqlconnector://root:bartolo@localhost:3306/test_db', echo=False)

query_1 = "SELECT * FROM test_metadata"

df = pd.read_sql(sql=query_1, con=engine)

# print(df.dtypes)
# print(df.shape)

# first plot
# plt.figure()
# df.boxplot(column='n_row', return_type='axes')
# plt.show()

n_hard_disk = df['n_row'].values

# media min y max
print(n_hard_disk.mean(), n_hard_disk.min(), n_hard_disk.max())

query_min = "SELECT meta.date FROM test_metadata AS meta WHERE meta.n_row is 0"
query_max = "SELECT meta.date FROM test_metadata AS meta WHERE meta.n_row is 102323"


'''
# from pandas to numpy
dates, n_hard_disks = df['date'].values, df['n_row'].values

print(n_hard_disks.shape)

ptos = range(0, n_hard_disks.shape[0])  # rows - cols

print(type(ptos))
print(ptos)
mean = n_hard_disks.mean()

print(mean)
'''
