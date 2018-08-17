import os
import humanfriendly as hf
import pandas as pd
import time
import datetime

# raw_data = "..\\raw_data\\"
raw_data = "D:\__DUMP__\\raw_data\\"


def print_df_info(data):
    print("{0:}\n{0:}".format("-" * 80))
    print("Dataframe info:\n")
    data.info(memory_usage='deep')

    # print("Row number: {0:}".format(data.shape[0]))
    # print("Column number: {0}".format(data.shape[1]))
    # print("{0:}".format("-" * 80))
    # print("Columns and the number of non-NAN values:\n{0:}"
    #       .format(data.count()))
    # print("Columns dtypes: {0}".format(data.dtypes))

    # print(data.head(1))
    # header = data.columns.values.tolist()
    # for att in header:
    #     print(att)

    print("{0:}\n{0:}".format("-" * 80))


def get_files(folder):
    for item in os.listdir(folder):
        full_path = os.path.join(folder, item)
        if os.path.isfile(full_path):
            yield full_path
        elif os.path.isdir(full_path):
            yield from get_files(full_path)


def process_files(folder_list):
    '''
    METHOD 1 --> mem 4.1Gb to 1.3Gb to 621 MB  within time range of 60'' tops
    file reduced 393mb original 740mb (year 2013 with auto index 430mb)

    METHOD 2 --> mem 4.1Gb to 1.3Gb to 621 MB  within time range of 70'' tops
    file reduced 393mb original 740mb (year 2013 with auto index 430mb)

    df_yearly = pd.concat((pd.read_csv(f, sep=",", encoding="latin1", header=0)
                           for f in csv_list))
    '''

    df_year = pd.DataFrame()  # contains all year data
    df_day_list = []  # contains csv dataframes for each day in a year
    df_metada = pd.DataFrame()

    it = time.time()

    for i, folder in enumerate(folder_list, start=1):

        for csv in get_files(folder):

            '''
            metadata
                date - index
                size
                n_att
                header
                n_row
                time_stamp
            '''
            # df = pd.read_csv(csv, sep=",", encoding="latin1", header=0)

            df = pd.read_csv(csv, sep=",", encoding="latin1")

            df_day_list.append(df)
            print("csv nº {0:} processed".format(str(i).zfill(3)))

    df_yearly = pd.concat(df_day_list)

    ft = time.time()

    return ft-it, df_year


# max 366 therefore simplest way is using list comprehension
folder_list = sorted([os.path.join(raw_data, csv)
                      for csv in os.listdir(raw_data)])

process_files(folder_list)

# print(csv_list[0])  # just 2013

# print(csv_list)
# time_stamp = datetime.datetime.now()
# print(time_stamp.hour, time_stamp.minute, time_stamp.second)


# print("total time {0:}".format(hf.format_timespan(ft - it)))
# print_df_info(df_yearly)
#
# # get rid of NAN columns // del df_raw and df_clean
# df_yearly = df_yearly.dropna(axis=1, how='all')
# print_df_info(df_yearly)
#
# # assigned the right type to columns
# right_dtypes = {"date": "datetime64", "failure": "bool"}
# df_yearly = df_yearly.astype(right_dtypes)
#
# index_columns = ['date', 'serial_number']
# df_yearly.set_index(index_columns, inplace=True)
# print_df_info(df_yearly)
#
# # save to csv unified by year
# path_csv_cleaned = "D:\__dataset__\\Backblaze hard disk - db\\__DATA CSV__\\clean"
# df_yearly.to_csv(path_csv_cleaned + "\\2013_cleaned.csv", sep=",", encoding="latin1")

# *******************************************************************************
