import numpy as np
from oauth2client import service_account 
import pandas as pd
import time
import threading
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import psycopg2
from pyasn1.type.constraint import ValueSizeConstraint

def connect_table(dat, user, passw):
    connect = psycopg2.connect(database=dat, user=user, password=passw)
    cursor = connect.cursor()
    return connect, cursor


def disconnect_table(connect, cursor):
    connect.close()
    cursor.close()


def create_table(table_name):
    connect, cursor = connect_table("sales", "postgres", "gangster123")
    check = "DROP TABLE IF EXISTS %s" %(table_name)
    cursor.execute(check)
    commands = ("""CREATE TABLE %s (name VARCHAR(50),
    target_month VARCHAR(20), reached_month VARCHAR(20), ratio_month VARCHAR(20),salary VARCHAR(20),
    target_week1 VARCHAR(20), reached_week1 VARCHAR(20), ratio_week1 VARCHAR(20),
    target_week2 VARCHAR(20), reached_week2 VARCHAR(20), ratio_week2 VARCHAR(20),
    target_week3 VARCHAR(20), reached_week3 VARCHAR(20), ratio_week3 VARCHAR(20),
    target_week4 VARCHAR(20), reached_week4 VARCHAR(20), ratio_week4 VARCHAR(20),
    headquarters VARCHAR(15), policy_salary_22 VARCHAR(20),
    date_start DATE, date_end DATE)""") %(table_name)
    cursor.execute(commands)
    connect.commit()
    disconnect_table(connect, cursor)


def insert_data(df, table_name, date_start, date_end):
    connect, cursor = connect_table("sales", "postgres", "gangster123")
    command = "SET datestyle = DMY;"
    cursor.execute(command)
    for index in df.index:
        values = np.array([df.at[index, col] for col in list(df.columns)])
        if len(values) < 20:
            if len(values) == 19:
                values = np.append(values, "chưa áp dụng")
            else:
                values = np.append(values, "trụ sở chính")
                values = np.append(values, "chưa áp dụng")

        query = """INSERT INTO %s VALUES('%s', '%s', '%s', '%s', '%s', '%s'
        ,'%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')""" %(table_name, values[0],\
        values[1], values[2], values[3], values[4], values[6], values[7], values[8], values[9], values[10],\
        values[11], values[12], values[13], values[14], values[15], values[16], values[17], values[18], values[19],\
        date_start, date_end)
        cursor.execute(query)
    connect.commit()
    disconnect_table(connect, cursor)


def real_time(sheets, table_name):
    sheet = sheets.worksheets()
    for count in range(0, 10):
        sheet.pop()
    connect, cursor = connect_table("sales", "postgres", "gangster123")
    update = "TRUNCATE %s" %(table_name)
    while True:
        for sheet_id in sheet:
            time_table = pd.DataFrame()
            for index in range(10, 36):
                data = sheet_id.get_values("B%s:U%s"%(index, index))
                data = pd.DataFrame(data)
                time_table = time_table.append(data, ignore_index=True)
            start_date = sheet_id.cell(1, 3).value
            end_date = sheet_id.cell(2, 3).value
            print(time_table)
            insert_data(time_table, table_name, start_date, end_date)
            time.sleep(8)
        time.sleep(120)
        cursor.execute(update)
        connect.commit()


scope = ("https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets",\
"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive")
creds = ServiceAccountCredentials.from_json_keyfile_name("real_time_sheet/creds.json", scope)
client = gspread.authorize(creds)
sheets = client.open("MỤC TIÊU DOANH SỐ 2020 - MCG")
create_table("target_sales_2020")
real_time(sheets, "target_sales_2020")



