import math
from os import read
def check_prime_number(n):
    if n == 2:
        return True
    elif n<2:
        return False
    else:
        for i in range(2,math.floor(math.sqrt(n))+1): #kiem tra neu n chia het cho 1 so trong khoang tu
            if(n%i == 0):                             #2 -> sqrt(n)
                return False
    return True


def uoc_chung_lon_nhat(a,b):
    while(a*b != 0):
        if(a>b):
            a%=b
        else:
            b%=a
    return a+b 


def Boi_chung_nho_nhat(a,b):
    product = a*b
    result = product//uoc_chung_lon_nhat(a,b)
    return result


def Pyramid(n):
    number_of_star = 1+ 2*(n-1)
    for i in range(0,n):
        str = "" 
        for j in range(0,i):
            str += " " 
        for k in range(i,number_of_star-i):
            str+= "*"
        print(str)

def read_symbol():
    read_file = open("Nhap_mon_Python/kyhieu.txt","r")
    dic_sym = dict()
    for line in read_file:
        if(line == ""):
            return dic_sym
        List = line.split(":")
        List[0] = List[0].strip()
        List[1] = List[1].strip()
        dic_sym[List[0]] = List[1]
    return dic_sym


def weather_forecast(day,date,next_n_days):
    read_file = open("Nhap_mon_Python/dubaothoitiet.txt","r") 
    flag = False 
    day_of_week = ("monday", "tuesday","wednesday","thursday","friday","saturday", "sunday")
    weather = read_symbol()
    idx = day_of_week.index(day)

    for line in read_file:
        if(date in line):
            flag = True 
            line = read_file.readline()
            for i in range(0,next_n_days):
                idx+=1
                if(idx == 7):
                    idx = 0
                if(line == ""):
                    print('No information')
                    break
                line = line.strip()
                arr =  line.split(':')
                #VD: line = 11/9/2022:S => arr= ['11/9/2022','S']
                arr[1] = weather[arr[1]]
                line = ':'.join(arr)
                convert_day = day_of_week[idx]
                print(f'{convert_day} - {line}')
                line = read_file.readline()
        if(flag == True):
            break

    if(flag == False): #neu du lieu yeu cau khong xuat hien trong file
        print('No information')
    read_file.close()


if __name__ == "__main__":
    #Bai 1
    print("Exercise 1: kiem tra so nguye to, tra ve True neu do la so nguyen, nguoc lai tra ve False")
    num = int(input("input a number: "))
    if(check_prime_number(num)== True):
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")

    #Bai 2
    print("Exercise 2: nhap 2 so nguyen va tim boi chung nho nhat cua 2 so do")
    print("Input 2 numbers a and b: ")
    a = int(input("input a: "))
    b = int(input("input b: "))
    print(f"least common multiple of a and b: {Boi_chung_nho_nhat(a,b)}")

    #Bai 3
    print("Exercise 3: Xuat ra man hinh mot kim tu thap, co tham so truyen vao bang so tang, tang duoi it hon tang tren")
    level = int(input("Input level of a pyramid: "))
    Pyramid(level)

    #Bai 4
    print("Exercise 4: Cho cac du bao thoi tiet cho 30 ngay,nhap thong tin thu - ngay - thang - nam cua hom nay de yeu cau chuong trinh dua ra du bao cua n ngay tiep theo")
    print("Cac ky hieu thoi tiet duoc chu thich trong file ky hieu.txt")
    print("Vi du: Today: wednesday - 11/9/2022")
    print("n = 2 ")
    print("weather forecast for 2 day: ")
    print("thursday - 12/9/2022: fog")
    print("friday - 13/9/2022: sunny")
    day,date = input("Today: ").split("-")
    day = day.strip()
    date = date.strip()
    next_n_days = int(input("n = "))
    weather_forecast(day,date,next_n_days)

