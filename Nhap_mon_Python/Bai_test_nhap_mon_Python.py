from os import read
from math import sqrt
from math import floor
def checkPrimeNumber(number):
    if number == 2:
        return True
    elif number<2:
        return False
    else:
        for i in range(2,floor(sqrt(number))+1): 
            if(number%i == 0):                            
                return False
    return True


def greatestCommonDivisor(first_number,second_number):
    while(first_number*second_number != 0):
        if(first_number>second_number):
            first_number%=second_number
        else:
            second_number%=first_number
    return first_number+second_number


def lowestCommonMultiple(first_number,second_number):
    product = first_number*second_number
    result = product//greatestCommonDivisor(first_number,second_number)
    return result


def drawPyramid(n):
    number_of_stars = 1+ 2*(n-1)
    for i in range(0,n):
        str = "" 
        for j in range(0,i):
            str += " " 
        for k in range(i,number_of_stars-i):
            str+= "*"
        print(str)


def readSymbol():
    read_file = open("Nhap_mon_Python/kyhieu.txt","r")
    dic_symbol = dict()
    for line in read_file:
        if(line == ""):
            read_file.close()
            return dic_symbol
        List = line.split(":")
        List[0] = List[0].strip()
        List[1] = List[1].strip()
        dic_symbol[List[0]] = List[1]
    return dic_symbol


def weatherForecast(day,date,next_n_days):
    read_file = open("Nhap_mon_Python/dubaothoitiet.txt","r") 
    flag = False 
    DAY_OF_WEEK = ("monday", "tuesday","wednesday","thursday","friday","saturday", "sunday")
    weather = readSymbol()
    idx = DAY_OF_WEEK.index(day)

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
                convert_day = DAY_OF_WEEK[idx]
                print(f'{convert_day} - {line}')
                line = read_file.readline()
        if(flag == True):
            break

    if(flag == False): #neu du lieu yeu cau khong xuat hien trong file
        print('No information')
    read_file.close()


if __name__ == "__main__":
    #Bai 1
    print("Bai tap 1: kiem tra so nguyen to, tra ve True neu do la so nguyen, nguoc lai tra ve False")
    number = int(input("input a number: "))
    if(checkPrimeNumber(number)== True):
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")

    #Bai 2
    print("Bai tap 2: nhap 2 so nguyen va tim boi chung nho nhat cua 2 so do")
    print("Input 2 numbers a and b: ")
    a = int(input("input a: "))
    b = int(input("input b: "))
    a = abs(a) if a<0 else a
    b = abs(b) if b<0 else b
    print(f"lowest common multiple of a and b: {lowestCommonMultiple(a,b)}")

    #Bai 3
    print("Bai tap 3: Xuat ra man hinh mot kim tu thap, co tham so truyen vao bang so tang, tang duoi it hon tang tren")
    level = int(input("Input level of a pyramid: "))
    drawPyramid(level)

    #Bai 4
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
    next_n_days = int(input("n = "))
    weatherForecast(day,date,next_n_days)

