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


readobj = open('C:/Code/Minh_Phuc_Internship/Nhap_mon_Python/dubaothoitiet.txt','r')
str = '5/10/2022'
for line in readobj:
    if(str in line):
       str = readobj.readline()
       for i in range(0,4):
            if(str != ''):
               str = str.strip()
               print(str)
               str = readobj.readline()
            else:
                print('No information')
    print(line[len(line)-2])
        

        