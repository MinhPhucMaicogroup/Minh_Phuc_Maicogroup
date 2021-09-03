def read_symbol_file():
    read_file = open("Nhap_mon_Python/kyhieu.txt","r")
    dic_symbol = dict()
    symbol_list = read_file.readlines()
    read_file.close()
    symbol_list = [ele.strip() for ele in symbol_list]
    for ele in symbol_list:
        ele = ele.strip()
        date, syntax = ele.split(":")
        dic_symbol[date] = syntax
    return dic_symbol


def weather_forecast(day,date, next_n_days):
    read_file = open("Nhap_mon_Python/dubaothoitiet.txt","r") 
    day_in_week = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")
    weather = read_symbol_file()
    flag = False
    index = day_in_week.index(day)
    list_forecast = read_file.readlines();
    read_file.close()
    list_forecast = [ele.strip() for ele in list_forecast]

    for i in range(len(list_forecast)):
        if(date in list_forecast[i]):
            flag = True
            j = i+1
            for j in range(j,j+next_n_days):
                if(j == len(list_forecast)):
                    print("No information")
                    break
                index += 1
                if(index == 7):
                    index = 0
                following_date, syntax = list_forecast[j].split(':')
                syntax = weather[syntax]
                list_forecast[j] = ':'.join([following_date,syntax])
                print(f"{day_in_week[index]} - {list_forecast[j]}")
        if(flag == True):
            break

    if(flag == False):
        print("No information")


print("Bai tap 4: Cho cac du bao thoi tiet cho 30 ngay,nhap thong tin thu-ngay/thang/nam cua hom nay de yeu cau chuong trinh dua ra du bao cua n ngay tiep theo")
print("Cac ky hieu thoi tiet duoc chu thich trong file kyhieu.txt")
print("Vi du: Today: wednesday - 11/9/2022")
print("n = 2 ")
print("weather forecast for 2 day: ")
print("thursday - 12/9/2022: fog")
print("friday - 13/9/2022: sunny")
day, date = input("Today: ").split("-")
day = day.strip()
date = date.strip()
next_n_days = int(input("n = "))
weather_forecast(day, date, next_n_days)


