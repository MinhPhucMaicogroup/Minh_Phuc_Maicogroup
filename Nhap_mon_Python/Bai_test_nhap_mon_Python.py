import math
from os import read
def check_prime_number(n):
    if n == 2:
        return True
    elif n<2:
        return False
    else:
        for i in range(2,math.floor(math.sqrt(n))+1):
            if(n%i == 0):
                return False
    return True

def UCLN(a,b):
    while(a*b != 0):
        if(a>b):
            a%=b
        else:
            b%=a
    return a+b

def BCNN(a,b):
    prod = a*b
    result = prod//UCLN(a,b)
    return result

def pyramid(n):
    number_of_star = 1+ 2*(n-1)
    for i in range(0,number_of_star):
        str = ""
        for j in range(0,i):
            str += " "
        for k in range(i,number_of_star-i):
            str+= "*"
        print(str)

def weather_forecast(day,date,n):
    readobj = open('C:/Code/Nhap_mon_Python/dubaothoitiet.txt','r')
    flag = False
    day_of_week = {'monday': 0, 'tuesday': 1,'wednesday': 2,'thursday': 3,'friday': 4,'saturday':5, 'sunday': 6}
    val_list = list(day_of_week.values()) #0 1 2 3 4 5 6
    weather = {'S': 'sunny','C': 'cloudy','D': 'drizzle','F':'fog','R':'rain'}
    key_list = list(day_of_week.keys())
    idx = day_of_week[day]
    for line in readobj:
        if(date in line):
            flag = True
            line = readobj.readline()
            for i in range(0,n):
                idx+=1
                if(idx == 7):
                    idx = 0
                if(line == ''):
                    print('No information')
                    break
                line = line.strip()
                arr =  line.split(':')
                arr[1] = weather[arr[1]]
                line = ':'.join(arr)
                convert_day = val_list.index(idx)
                print(f'{key_list[convert_day]} - {line}')
                line = readobj.readline()
        if(flag == True):
            break
    if(flag == False):
        print('No information')

