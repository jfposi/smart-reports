import os
import re
from zipfile import ZipFile
import time
import humanfriendly as hf
import shutil
import os
import wget
import requests
from bs4 import BeautifulSoup
import time

# TODO improve the code, e.g: get the folder names from the csv name (RT app)
# TODO create a log system
# TODO improve the cli msg
# TODO try / catch in everything


raw_data = "..\\raw_data\\"  # TODO delete it just to avoid indexing in pycharm


# clean_data = "..\\clean_data\\"  # not used for now
# raw_data = "D:\__DUMP__\\raw_data\\"


def fetch_files():
    url = "https://www.backblaze.com/b2/hard-drive-test-data.html"

    if os.path.isdir(raw_data):
        print("folder raw_data already created")
    else:
        os.mkdir(raw_data, 755)  # TODO check permissions out
        print("folder raw_data created")

    web = requests.get(url)
    soup = BeautifulSoup(web.content, 'html.parser')
    files = [link.get('href') for link in soup.findAll('a', attrs={'href': re.compile("data.+\.zip")})]

    it = time.time()

    for i, f in enumerate(files, start=1):
        filename = wget.download(f, out=raw_data)
        print("file {0:}/{1:} downloaded".format(str(i).zfill(2), len(files)))

    ft = time.time()

    return len(files), ft - it


def unzip_files(zip_list):
    ''' execution time --> ZIP nº: 0001 processed in 21.04 seconds '''

    tt = 0

    for i, file in enumerate(zip_list, start=1):
        file_name, file_ext = os.path.splitext(file)

        it = time.time()

        with ZipFile(file, "r") as fzip:
            fzip.extractall(raw_data + os.path.split(file_name)[1])

        ft = time.time()
        tt += ft - it
        print("ZIP nº: {0:} processed in {1:}"
              .format(str(i).zfill(3), hf.format_timespan(ft - it)))

        # print(file)
        os.remove(file)  # there is no need to keep it

    return tt


def set_up_dirs(first_year=2013, last_year=2018):
    for year in range(first_year, last_year + 1, 1):

        folder_path = raw_data + "\\" + str(year) + "\\"

        if os.path.isdir(folder_path):
            print("folder for year {0:} already created".format(str(year)))
        else:
            os.mkdir(folder_path, 755)  # TODO check permissions out
            print("folder for year {0:} created".format(str(year)))


def get_files(folder):
    for item in os.listdir(folder):
        full_path = os.path.join(folder, item)
        if os.path.isfile(full_path):
            yield full_path
        elif os.path.isdir(full_path):
            yield from get_files(full_path)


def sort_files(folder_list):
    '''
    csv file names are based on dates E.g: 2016-01-24.csv
    csv in one location sorted by year
    https://pythex.org/
    move files it is a fast operation
    '''

    set_up_dirs()

    name_patt = r"^\d{4}-\d{2}-\d{2}\.csv$"

    for i, folder in enumerate(folder_list, start=1):

        for file in get_files(folder):
            file_path, file_name = os.path.split(file)
            if re.match(name_patt, file_name):
                shutil.move(file, os.path.join(raw_data + "\\" + file_name[:4] + "\\", file_name))

        # print(folder)
        shutil.rmtree(folder)  # there is no need to keep it


'''
uncomment when necessary
functions return info for log system
'''

# n_files, exec_t_download = fetch_files()

file_list = sorted([os.path.join(raw_data, zip_file) for zip_file in os.listdir(raw_data)
                    if os.path.isfile(os.path.join(raw_data, zip_file)) and
                    ("data" in os.path.split(os.path.join(raw_data, zip_file))[1])])

exec_t_unzip = unzip_files(file_list)

# folders with csv data
folders = sorted([os.path.join(raw_data, folder) for folder in os.listdir(raw_data)
                  if os.path.isdir(os.path.join(raw_data, folder)) and
                  ("data" in os.path.split(os.path.join(raw_data, folder))[1])])

# set_up_dirs()  # TODO improved it
sort_files(folders)
