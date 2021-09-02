import math
from os import read
def checkPrimeNumber(number):
    if number == 2:
        return True
    elif number<2:
        return False
    else:
        for i in range(2,math.floor(math.sqrt(number))+1): #kiem tra neu n chia het trong khoang tu
            if(number%i == 0):                             #2 -> sqrt(n)
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
    numberOfStars = 1+ 2*(n-1)
    for i in range(0,n):
        str = "" 
        for j in range(0,i):
            str += " " 
        for k in range(i,numberOfStars-i):
            str+= "*"
        print(str)


def readSymbol():
    readFile = open("Nhap_mon_Python/kyhieu.txt","r")
    dicSym = dict()
    for line in readFile:
        if(line == ""):
            readFile.close()
            return dicSym
        List = line.split(":")
        List[0] = List[0].strip()
        List[1] = List[1].strip()
        dicSym[List[0]] = List[1]
    return dicSym


def weatherForecast(day,date,next_n_days):
    readFile = open("Nhap_mon_Python/dubaothoitiet.txt","r") 
    flag = False 
    DAY_OF_WEEK = ("monday", "tuesday","wednesday","thursday","friday","saturday", "sunday")
    weather = readSymbol()
    idx = DAY_OF_WEEK.index(day)

    for line in readFile:
        if(date in line):
            flag = True 
            line = readFile.readline()
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
                convertDay = DAY_OF_WEEK[idx]
                print(f'{convertDay} - {line}')
                line = readFile.readline()
        if(flag == True):
            break

    if(flag == False): #neu du lieu yeu cau khong xuat hien trong file
        print('No information')
    readFile.close()


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

