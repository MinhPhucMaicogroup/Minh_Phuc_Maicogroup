def draw_nth_pyramid(level):
    number_of_stars = 1 + 2*(level-1)
    for i in range(0,level):
        stage = "" 
        for j in range(0,i):
            stage += " " 
        for k in range(i,number_of_stars-i):
            stage += "*"
        print(stage)


print("Bai tap 3: Xuat ra man hinh mot kim tu thap, co tham so truyen vao bang so tang, tang duoi it hon tang tren")
level = int(input("Input level of a pyramid: "))
draw_nth_pyramid(level)
