from numpy import single
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import numpy as np
import pandas as pd
import threading
import time
import psycopg2

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
    commands = ("""CREATE TABLE %s (name VARCHAR(50) NULL,
    date DATE NULL, shift VARCHAR(50) NULL)""") %(table_name)
    cursor.execute(commands)
    connect.commit()
    disconnect_table(connect, cursor)


def insert(df, table):
    connect, cursor = connect_table("sales", "postgres", "gangster123")
    date = df.iloc[0].to_numpy()
    date = np.delete(date, 0)
    if(date[0] == "T2"):
        date = df.iloc[1].to_numpy()
        date = np.delete(date, 0)
    count = 0
    command = "SET datestyle = DMY;"
    cursor.execute(command)
    for day in date:
        count += 1
        for index in df.index:
            if index == 0:
                continue
            name = df.at[index, 0]
            shift = df.at[index, count]
            query = "INSERT INTO %s (name, shift, date) VALUES ('%s', '%s', '%s')" %(table, name,\
            shift, day)
            missing_command = """DELETE FROM %s
            WHERE shift = 'nan' OR name IN ('LỊCH TRỰC TỐI', 'LỊCH TRỰC TRƯA', 'LỊCH TÌM NHẠC')
            OR LENGTH(name) = 0;""" %(table)
            cursor.execute(query)
            cursor.execute(missing_command)
    connect.commit()
    disconnect_table(connect, cursor)


def real_time(sheets, table_name):
    sheet = sheets.worksheets()
    for count in range(1,6):
        sheet.pop()
    connect, cursor = connect_table("sales", "postgres", "gangster123")
    update = "TRUNCATE %s" %(table_name)
    while True:
        for sheet_id in sheet:
            time_table = pd.DataFrame()
            for index in range(4, 21):
                data = sheet_id.get_values("B%s:I%s" %(index, index))
                data = pd.DataFrame(data)
                time_table = time_table.append(data, ignore_index=True)
            if time_table.empty:
                time.sleep(8)
                continue
            print(time_table)
            insert(time_table, table_name)
            time.sleep(8)
        cursor.execute(update)
        connect.commit()



scope = ("https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets",\
"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive")
creds = ServiceAccountCredentials.from_json_keyfile_name("real_time_sheet/creds.json", scope)
client = gspread.authorize(creds)
sheets = client.open("Đăng ký lịch làm SGGW")
create_table("sggw_schedule")
real_time(sheets, "sggw_schedule")