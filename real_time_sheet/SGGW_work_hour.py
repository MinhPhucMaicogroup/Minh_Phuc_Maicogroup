from numpy import single
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import numpy as np
import pandas as pd
import threading
import time
import psycopg2

class SggwSheet:
    def __init__(self, database, username, password, table_name):
        self.__database = database
        self.__user = username
        self.__password = password
        self.__table_name = table_name
        self.__connector = psycopg2.connect(database=database, user=username, password=password)
        self.__cursor = self.__connector.cursor()

    def create_table(self):
        checker = "TRUNCATE TABLE IF EXISTS %s" %(self.__table_name)
        self.__cursor.execute(checker)
        command = ("""CREATE TABLE %s (name VARCHAR(50) NULL,
        date DATE NULL, shift VARCHAR(50) NULL)""") %(self.__table_name)
        self.__cursor.execute(command)
        self.__connector.commit()

    @staticmethod
    def __handle__exception(date, dataframe):
        if(date[0] == "T2"):
            date = dataframe.iloc[1].to_numpy()
            date = np.delete(date, 0)
        return date

    def insert(self, dataframe):
        date = dataframe.iloc[0].to_numpy()
        date = np.delete(date, 0)
        date = SggwSheet.__handle__exception(date, dataframe)
        row_idx = 0
        date_style = "SET datestyle = DMY;"
        self.__cursor.execute(date_style)
        for day in date:
            row_idx += 1
            for index in dataframe.index:
                if index == 0:
                    continue
            name = dataframe.at[index, 0]
            shift = dataframe.at[index, row_idx]
            query = "INSERT INTO %s (name, shift, date) VALUES ('%s', '%s', '%s')" %(self.__table_name,\
            name, shift, day)
            missing_command = """DELETE FROM %s
            WHERE shift = 'nan' OR name IN ('LỊCH TRỰC TỐI', 'LỊCH TRỰC TRƯA', 'LỊCH TÌM NHẠC')
            OR LENGTH(name) = 0;""" %(self.__table_name)
            self.__cursor.execute(query)
            self.__cursor.execute(missing_command)
        self.__connector.commit()

    def real_time_read(self, sheets):
        pages = sheets.worksheets()
        for count in range(1,6):
            pages.pop()
        reset_command = "TRUNCATE %s" %(self.__table_name)
        while True:
            for sheet_id in pages:
                time_table = pd.DataFrame()
                for index in range(4, 21):
                    data = sheet_id.get_values("B%s:I%s" %(index, index))
                    data = pd.DataFrame(data)
                    time_table = time_table.append(data, ignore_index=True)
                if time_table.empty:
                    time.sleep(12)
                    continue
                print(time_table)
                self.insert(time_table)
                time.sleep(12)
            time.sleep(120)
            self.__cursor.execute(reset_command)
            self.__connector.commit()


scope = ("https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets",\
"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive")
creds = ServiceAccountCredentials.from_json_keyfile_name("real_time_sheet/creds.json", scope)
client = gspread.authorize(creds)
sheets = client.open("Đăng ký lịch làm SGGW")
test = SggwSheet("sales", "postgres", "gangster123", "sggw_schedule")
test.create_table()
test.real_time_read(sheets)
