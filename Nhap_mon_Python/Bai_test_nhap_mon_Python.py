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
    prod = a*b
    result = prod//uoc_chung_lon_nhat(a,b) #BCNN(a,b) = (a*b)/UCLN(a,b)
    return result


def pyramid(n):
    number_of_star = 1+ 2*(n-1) #so luong toi da cua "*" trong 1 hang VD: n =3 => so luong toi da la 5
    for i in range(0,n):
        str = "" 
        for j in range(0,i):
            str += " " 
        for k in range(i,number_of_star-i):
            str+= "*"
        print(str)


def weather_forecast(day,date,next_n_days):
    read_file = open("Nhap_mon_Python/dubaothoitiet.txt","r") 
    flag = False 
    day_of_week = {"monday": 0, "tuesday": 1,"wednesday": 2,"thursday": 3,"friday": 4,"saturday":5, "sunday": 6}
    value_list = list(day_of_week.values())
    key_list = list(day_of_week.keys())
    weather = {'S': 'sunny','C': 'cloudy','D': 'drizzle','F':'fog','R':'rain'}
    idx = day_of_week[day]

    for line in read_file:
        if(date in line):
            flag = True 
            line = read_file.readline()
            for i in range(0,next_n_days):
                idx+=1
                if(idx == 7): #neu idx = 7 thi chuyen sang monday bang cach cho idx = 0 
                    idx = 0
                if(line == ''): #neu doc toi cuoi file thi dung
                    print('No information')
                    break
                line = line.strip()
                arr =  line.split(':')
                #VD: line = 11/9/2022:S => arr= ['11/9/2022','S']
                arr[1] = weather[arr[1]]
                line = ':'.join(arr) #noi list thanh 1 chuoi phan tach nhau bang dau ':'
                convert_day = value_list.index(idx)
                print(f'{key_list[convert_day]} - {line}')
                line = read_file.readline()
        if(flag == True): #sau khi da doc xong, chuong trinh se doc toi cuoi file
            #de tiet kien thoi gian, thi bien flag se cho biet minh da thuc hien xong yeu cau 
            #va thoat khoi vong lap
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
    pyramid(level)

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

