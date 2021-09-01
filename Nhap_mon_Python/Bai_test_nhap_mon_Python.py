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
                return False #neu n chia het cho i thi n khong phai la so nguyen to tra ve False
    return True


def UCLN(a,b):
    while(a*b != 0):
        if(a>b):
            a%=b
        else:
            b%=a
    return a+b #mot trong 2 a va b se bang 0 nen dung phep cong de tinh ket qua


def BCNN(a,b):
    prod = a*b
    result = prod//UCLN(a,b) #BCNN(a,b) = (a*b)/UCLN(a,b)
    return result


def pyramid(n):
    number_of_star = 1+ 2*(n-1) #so luong toi da cua "*" trong 1 hang VD: n =3 => so luong toi da la 5
    for i in range(0,n):
        str = "" #khoi tao string rong 
        for j in range(0,i):
            str += " " #cach i dong
        for k in range(i,number_of_star-i):
            str+= "*"
        print(str)#xuat string


def weather_forecast(day,date,next_n_days):
    read_file = open("Nhap_mon_Python/dubaothoitiet.txt","r") #mo file va chon mode doc file
    flag = False #khoi toan bien bool flag
    day_of_week = {"monday": 0, "tuesday": 1,"wednesday": 2,"thursday": 3,"friday": 4,"saturday":5, "sunday": 6}
    value_list = list(day_of_week.values()) #khoi tao 1 list chua cac value trong dictionary day_of_week
    key_list = list(day_of_week.keys())#khoi tao 1 list chua cac key trong dictionary day_of_week
    weather = {'S': 'sunny','C': 'cloudy','D': 'drizzle','F':'fog','R':'rain'}#khoi tao 1 dictionary dua theo file kyhieu.txt
    idx = day_of_week[day]  #khoi tao bien idx de chuyen so ngay sang kieu int VD: monday => idx =0

    for line in read_file:
        if(date in line): #neu dd/mm/year xuat hien khi doc tren 1 dong
            flag = True  # dat gia tri bien flag = True
            line = read_file.readline() #doc dong tiep theo
            for i in range(0,next_n_days): #vong lap de doc n dong cua ngay tiep theo
                idx+=1
                if(idx == 7): #neu idx = 7 thi chuyen sang monday bang cach cho idx = 0 
                    idx = 0
                if(line == ''): #neu da doc toi cuoi file thi dung
                    print('No information')
                    break
                line = line.strip() #xoa cac ky tu khoang trang,/t, /n o dau va cuoi file
                arr =  line.split(':') # tach du lieu thanh 2 de xu ly
                #VD: line = 11/9/2022:S => arr= ['11/9/2022','S']
                arr[1] = weather[arr[1]] #thay doi 'S' thanh 'sunny' dua vao dictionary weather
                line = ':'.join(arr) #noi list thanh 1 chuoi phan tach nhau bang dau ':'
                convert_day = value_list.index(idx) #chuyen integer idx sang thu 
                #VD: 0 => monday, 1=> tuesday,...
                print(f'{key_list[convert_day]} - {line}') #xuat ra man hinh bang cach dinh dang chuoi
                line = read_file.readline() #doc dong tiep theo
        if(flag == True): #sau khi da doc xong, chuong trinh co the doc het toi cuoi file
            #nen de tiet kien thoi gian, thi bien flag se cho biet minh thuc hien xong yeu cau 
            # va thoat khoi vong lap thay vi doc het toi cuoi file
            break

    if(flag == False): #neu du lieu yeu cau khong xuat hien trong file thi se xuat ra 'khong co thong tin"
        print('No information')
    read_file.close() #dong file


if __name__ == "__main__":
    #Bai 1
    print("Exercise 1")
    num = int(input("input a number: "))
    if(check_prime_number(num)== True):
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")

    #Bai 2
    print("Exercise 2")
    a,b = input("input two numbers: ").split()
    a = int(a)
    b = int(b)
    print(f"least common multiple of a and b: {BCNN(a,b)}")

    #Bai 3
    print("Exercise 3")
    level = int(input("Input number of level of a pyramid: "))
    pyramid(level)

    #Bai 4
    print("Exercise 4")
    day,date = input("Today: ").split("-")
    day = day.strip()
    date = date.strip()
    next_n_days = int(input("n = "))
    weather_forecast(day,date,next_n_days)

