from typing import TYPE_CHECKING, List

class Employee:
    _employees = []
    
    def __init__(self, name="anonymous", birth=0, position="Internship", skill=0, started=0):
        self._name = name.strip()
        self._birth = int(birth)
        self._position = position.strip()
        self._skill = int(skill)
        self._started = int(started)
        if self._name != "anonymous":
            Employee.recruit_employee(self)

    def __repr__(self):
        return f"Name: {self._name} - Birth: {self._birth} - \
Position: {self._position} - Skills: {self._skill} - Started: {self._started}"

    def __gt__(self, other):
        if self._skill > other._skill:
            return True
        elif self._skill == other._skill:
            name_split = self._name.split()
            last_name = name_split[len(name_split)-1]
            other_split = other._name.split()
            other_last_name = other_split[len(other_split)-1]
            name_split.clear()
            other_split.clear()
            if(last_name < other_last_name):
                return True
            else:
                return False
        else:
            return False

    def __lt__(self, other):
        return not self > other

    def get_age(self):
        try:
            age = 2021 - self._birth
            if age >= 100 or age < 0:
                raise Exception
            return age
        except:
            print("Invalid age !!")

    @classmethod
    def recruit_employee(cls, ele):
        cls._employees.append(ele)

    @classmethod
    def three_best_employee(cls):
        first = cls._employees[0]
        second = Employee()
        third = Employee()
        for i in range(1,len(cls._employees)):
            if cls._employees[i] > first:
                third = second
                second = first
                first = cls._employees[i]
            elif cls._employees[i] > second:
                third = second
                second = cls._employees[i]
            elif third < cls._employees[i]:
                third = cls._employees[i]
        return (first, second, third)

    @classmethod
    def print_team(cls):
        [print(member) for member in cls._employees]


# Test case Employee
employee1 = Employee(name="Do Ngoc An", birth=1995, position="Sales Team", skill=30, started=2020)
employee2 = Employee("Do Thi Khanh Van", 2002, "IT Team", 30, 2021)
employee3 = Employee("Vo Quang Thang", 1985, "Telesales Team", 10, 2019)
employee4 = Employee("Ho Gia Loc",2002, "MKT Team", 20, 2018)
employee5 = Employee("Le Hoang Phuc", 1992, "AI Team", 5, 2017)
employee6 = Employee("Nguyen Thanh Tung", 1996, "Sales Team", 13, 2017)
employee7 = Employee("Tran Tuan Thai", 1997, "Telesales Team", 22, 2016)
employee8 = Employee("Trinh Hoang Long", 2000, "IT Team", 14, 2015)
employee9 = Employee("Nguyen Minh Khoi", 1997, "MKT Team", 20, 2019)
employee10 = Employee("Bui Trinh Trung", 1999, "Sales Team", 20, 2020)
employee11 = Employee("Vo Hoai Linh", 1960, "Telesales Team", 19, 2017)
employee12 = Employee("Nguyen Tien Dat", 2004, "Telesales Team", 30, 2014)
employee13 = Employee("Nguyen Thuy Chi", 2002, "Sales Team", 17, 2018)
employee14 = Employee("Hoang Thuy Linh", 2000, "IT Team", 16, 2017)
employee15 = Employee("Nguyen Thanh Tung", 1995, "MKT Team", 17, 2018)
employee16 = Employee("Nguyen Bao Khanh", 2001, "BI Team", 19, 2019)
employee17 = Employee("Tran Phuong Tuan", 1997, "AI Team", 13, 2021)
employee18 = Employee("Nguyen Duc Cuong", 1993, "BI Team", 7, 2017)
employee19 = Employee("Nguyen Minh Hang", 1996, "IT Team", 17, 2013)
employee20 = Employee("Khac Hung", 1992, "Telesales Team", 14, 2016)
str = "Three Best Employee"
str = str.center(130,"-")
print(str)
three_best_player = Employee.three_best_employee()
[print(chosen_mem) for chosen_mem in three_best_player]