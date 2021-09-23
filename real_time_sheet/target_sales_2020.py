import numpy as np
from oauth2client import service_account 
import pandas as pd
import time
import threading
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import psycopg2
from pyasn1.type.constraint import ValueSizeConstraint

class TargetSales:
    def __init__(self, database, username, password, table_name):
        self._database = database
        self._user = username
        self._password = password
        self._table_name = table_name
        self._connector = psycopg2.connect(database=database, user=username, password=password)
        self._cursor = self._connector.cursor()
    
    def create_table(self):
        check = "DROP TABLE IF EXISTS %s" %(self._table_name)
        self._cursor.execute(check)
        create = ("""CREATE TABLE %s (name VARCHAR(50),
        target_month VARCHAR(20), reached_month VARCHAR(20), ratio_month VARCHAR(20),salary VARCHAR(20),
        target_week1 VARCHAR(20), reached_week1 VARCHAR(20), ratio_week1 VARCHAR(20),
        target_week2 VARCHAR(20), reached_week2 VARCHAR(20), ratio_week2 VARCHAR(20),
        target_week3 VARCHAR(20), reached_week3 VARCHAR(20), ratio_week3 VARCHAR(20),
        target_week4 VARCHAR(20), reached_week4 VARCHAR(20), ratio_week4 VARCHAR(20),
        headquarters VARCHAR(15), policy_salary_22 VARCHAR(20),
        date_start DATE, date_end DATE)""") %(self._table_name)
        self._cursor.execute(create)
        self._connector.commit()
    
    def insert(self, dataframe, date_start, date_end):
        date_style = "SET datestyle = DMY;"
        self._cursor.execute(date_style)
        for index in dataframe.index:
            values = np.array([dataframe.at[index, col] for col in list(dataframe.columns)])
            if len(values) < 20:
                if len(values) == 19:
                    values = np.append(values, "chưa áp dụng")
                elif len(values) == 18:
                    values = np.append(values, "trụ sở chính")
                    values = np.append(values, "chưa áp dụng")
                else:
                    values = np.append(values, "trụ sở chính")
                    values = np.append(values, "chưa áp dụng")
                    values = np.append(values, "chưa có 22% lương")

            query = """INSERT INTO %s VALUES('%s', '%s', '%s', '%s', '%s', '%s'
            ,'%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')""" %(self._table_name, values[0],\
            values[1], values[2], values[3], values[4], values[6], values[7], values[8], values[9], values[10],\
            values[11], values[12], values[13], values[14], values[15], values[16], values[17], values[18], values[19],\
            date_start, date_end)
            self._cursor.execute(query)
        self._connector.commit()
    
    def real_time_read(self, sheets):
        pages = sheets.worksheets()
        for count in range(0, 10):
            pages.pop()
        reset_command = "TRUNCATE %s" %(self._table_name)
        while True:
            for sheet_id in pages:
                data = sheet_id.get_values("B10:U35")
                data = pd.DataFrame(data)
                start_date = sheet_id.cell(1, 3).value
                end_date = sheet_id.cell(2, 3).value
                print(data)
                self.insert(data, start_date, end_date)
                time.sleep(6)
            time.sleep(120)
            self._cursor.execute(reset_command)
            self._connector.commit()


scope = ("https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets",\
"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive")
creds = ServiceAccountCredentials.from_json_keyfile_name("real_time_sheet/creds.json", scope)
client = gspread.authorize(creds)
sheets = client.open("MỤC TIÊU DOANH SỐ 2020 - MCG")
test = TargetSales("sales", "postgres", "gangster123", "target_sales_2020")
test.real_time_read(sheets)


