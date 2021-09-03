from math import floor
from math import sqrt

def check_prime_number(number):    
    if number == 2:
        return True
    elif number < 2:
        return False
    else:
        for i in range(2,floor(sqrt(number))+1): 
            if(number%i == 0):                            
                return False
    return True


print("Bai tap 1: kiem tra so nguyen to, tra ve True neu do la so nguyen to, nguoc lai tra ve False")
number = int(input("input a number: "))
if(check_prime_number(number) == True):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")