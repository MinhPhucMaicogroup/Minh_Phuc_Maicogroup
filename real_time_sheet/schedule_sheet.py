from numpy import single
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import numpy as np
import pandas as pd
import time
import psycopg2

class SggwSheet:
    def __init__(self, database, username, password, table_name):
        self._database = database
        self._user = username
        self._password = password
        self._table_name = table_name
        self._connector = psycopg2.connect(database=database, user=username, password=password)
        self._cursor = self._connector.cursor()

    def _create_table(self):
        checker = "DROP TABLE IF EXISTS %s" %(self._table_name)
        self._cursor.execute(checker)
        command = ("""CREATE TABLE %s (name VARCHAR(50) NULL,
        date DATE NULL, shift VARCHAR(50) NULL)""") %(self._table_name)
        self._cursor.execute(command)
        self._connector.commit()

    @staticmethod
    def handle_exception(date, dataframe):
        if(date[0] == "T2"):
            date = dataframe.iloc[1].to_numpy()
            date = np.delete(date, 0)
        return date

    def insert(self, dataframe):
        date = dataframe.iloc[0].to_numpy()
        date = np.delete(date, 0)
        date = SggwSheet.handle_exception(date, dataframe)
        row_idx = 0
        date_style = "SET datestyle = DMY;"
        self._cursor.execute(date_style)
        for day in date:
            row_idx += 1
            for index in dataframe.index:
                if index == 0:
                    continue
                name = dataframe.at[index, 0]
                shift = dataframe.at[index, row_idx]
                query = "INSERT INTO %s (name, shift, date) VALUES ('%s', '%s', '%s')" %(self._table_name,\
                name, shift, day)
                missing_command = """DELETE FROM %s
                WHERE shift = 'nan' OR name IN ('LỊCH TRỰC TỐI', 'LỊCH TRỰC TRƯA', 'LỊCH TÌM NHẠC')
                OR LENGTH(name) = 0 OR LENGTH(shift) = 0;""" %(self._table_name)
                self._cursor.execute(query)
                self._cursor.execute(missing_command)
        self._connector.commit()

    def real_time_read(self, sheets):
        pages = sheets.worksheets()
        for count in range(1,6):
            pages.pop()
        reset_command = "TRUNCATE %s" %(self._table_name)
        while True:
            for sheet_id in pages:
                data = sheet_id.get_values("B4:I20")
                data = pd.DataFrame(data)
                if data.empty:
                    time.sleep(6)
                    continue
                print(data)
                self.insert(data)
                time.sleep(6)
            time.sleep(120)
            self._cursor.execute(reset_command)
            self._connector.commit()


class SgavSheet(SggwSheet):
    def __init__(self, database, username, password, table_name):
        super().__init__(database, username, password, table_name)
    
    def _create_table(self):
        return super()._create_table()

    @staticmethod
    def handle_exception(date, dataframe):
        check = dataframe.iloc[1].to_numpy()
        check = np.delete(check, 0)
        if check[0] == "T2":
            date = dataframe.iloc[2].to_numpy()
            date = np.delete(date, 0)
        return date
    
    def insert(self, dataframe):
        date = dataframe.iloc[0].to_numpy()
        date = np.delete(date, 0)
        date = SgavSheet.handle_exception(date, dataframe)
        row_idx = 0
        command = "SET datestyle = DMY;"
        self._cursor.execute(command)
        for day in date:
            row_idx += 1
            for index in dataframe.index:
                if index == 0:
                    continue
                name = dataframe.at[index, 0]
                shift = dataframe.at[index, row_idx]
                query = "INSERT INTO %s (name, shift, date) VALUES ('%s', '%s', '%s')" %(self._table_name, name,\
                shift, day)
                missing_command = """DELETE FROM %s
                WHERE shift = 'nan' OR name IN ('LỊCH TRỰC TỐI', 'LỊCH TRỰC TRƯA', 'LỊCH TÌM NHẠC');""" %(self._table_name)
                self._cursor.execute(query)
                self._cursor.execute(missing_command)
        self._connector.commit()
    
    def real_time_read(self, sheets):
        pages = sheets.worksheets()
        reset_command = "TRUNCATE %s" %(self._table_name)
        while True:
            for sheet_id in pages:
                checker = sheet_id.cell(6, 1).value
                if checker == None:
                    data = sheet_id.get_values("B3:I11")
                else:
                    data = sheet_id.get_values("A3:H11")
                data = pd.DataFrame(data)
                if data.empty:
                    time.sleep(6)
                    continue
                print(data)
                self.insert(data)
                time.sleep(6)
            time.sleep(120)
            self._cursor.execute(reset_command)
            self._connector.commit()


scope = ("https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets",\
"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive")
creds = ServiceAccountCredentials.from_json_keyfile_name("real_time_sheet/creds.json", scope)
client = gspread.authorize(creds)
sheets = client.open("ĐĂNG KÝ LỊCH LÀM VIỆC TEAM THỦ ĐỨC ")
test = SgavSheet("sales", "postgres", "gangster123", "thu_duc_schedule")
test._create_table()
test.real_time_read(sheets)
