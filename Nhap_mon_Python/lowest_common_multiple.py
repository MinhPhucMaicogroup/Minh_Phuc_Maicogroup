def greatest_common_divisor(a,b):
    while(a*b != 0):
        if(a > b):
            a = a % b
        else:
            b = b % a
    return a + b


def lowest_common_multiple(a,b):
    product = a * b    
    result = product // greatest_common_divisor(a,b)
    return result


print("Bai tap 2: nhap 2 so nguyen duong va tim boi chung nho nhat cua 2 so do")
print("Input 2 numbers a and b: ")
a = int(input("input a: "))
b = int(input("input b: "))
print(f"lowest common multiple of a and b: {lowest_common_multiple(a,b)}")

