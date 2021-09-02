def read_file_symbol():
    read_file = open("Nhap_mon_Python/kyhieu.txt","r")
    dic_symbol = dict()
    symbol_file = read_file.readlines()
    symbol_file = [element.strip() for element in symbol_file]
    for weather_symbol in symbol_file:
        weather_symbol = weather_symbol.strip()
        arr = weather_symbol.split(":")
        dic_symbol[arr[0]] = arr[1]
    return dic_symbol


def weather_forecast(day,date,next_n_days):
    read_file = open("Nhap_mon_Python/dubaothoitiet.txt","r") 
    day_of_week = ("monday", "tuesday","wednesday","thursday","friday","saturday", "sunday")
    weather = read_file_symbol()
    flag = False
    index = day_of_week.index(day)
    list_forecast = read_file.readlines();
    list_forecast = [element.strip() for element in list_forecast]

    for index in range(len(list_forecast)):
        if(date in list_forecast[index]):
            flag = True
            forecast = index+1
            for forecast in range(forecast,forecast+next_n_days):
                if(forecast == len(list_forecast)):
                    print("No information")
                    break
                index += 1
                if(index == 7):
                    index = 0
                arr = list_forecast[forecast].split(':')
                arr[1] = weather[arr[1]]
                list_forecast[forecast] = ':'.join(arr)
                print(f"{day_of_week[index]} - {list_forecast[forecast]}")
        if(flag == True):
            break
    if(flag == False):
        print("No information")
    read_file.close()


print("Bai tap 4: Cho cac du bao thoi tiet cho 30 ngay,nhap thong tin thu-ngay/thang/nam cua hom nay de yeu cau chuong trinh dua ra du bao cua n ngay tiep theo")
print("Cac ky hieu thoi tiet duoc chu thich trong file kyhieu.txt")
print("Vi du: Today: wednesday - 11/9/2022")
print("n = 2 ")
print("weather forecast for 2 day: ")
print("thursday - 12/9/2022: fog")
print("friday - 13/9/2022: sunny")
day,date = input("Today: ").split("-")
day = day.strip()
date = date.strip()
next_nth_days = int(input("n = "))
weather_forecast(day,date,next_nth_days)


