from typing import TYPE_CHECKING


class Employee:
    list_of_employee = []
    @classmethod
    def add_employee(cls, ele):
        cls.list_of_employee.append(ele)

    def __init__(self, name="anonymous", birth: int=0, position="Internship", skill: int=0, started: int=2021):
        self.name = name.strip()
        self.birth = birth
        self.position = position.strip()
        self.skill = skill
        self.started = started
        self._index = 0
        Employee.add_employee(self)

    def __gt__(self, other):
        if self.skill > other.skill:
            return True
        elif self.skill == other.skill:# 100 > 95
            if self.name < other.name:
                return True
            else:
                return False
        else:
            return False
    
    def __lt__(self, other):
        return not self > other

    @classmethod
    def sort_by_skills(cls):
        for i in range(1,len(cls.list_of_employee)):
            j = i - 1 
            target = cls.list_of_employee[i]
            while j >= 0 and target < cls.list_of_employee[j]:
                cls.list_of_employee[j+1] = cls.list_of_employee[j]
                j -= 1
            cls.list_of_employee[j+1] = target

    @classmethod
    def three_best_employee(cls):
        first = cls.list_of_employee[0]
        second = Employee()
        third = Employee()
        for i in range(1,len(cls.list_of_employee)):
            if cls.list_of_employee[i] > first:
                third = second
                second = first
                first = cls.list_of_employee[i]
            elif cls.list_of_employee[i] > second:
                third = second
                second = cls.list_of_employee[i]
            elif third < cls.list_of_employee[i]:
                third = cls.list_of_employee[i]
        return [first, second, third]
                

    @classmethod
    def all_employee(cls):
       [print(employ) for employ in cls.list_of_employee]

    def __str__(self):
        return f"Name: {self.name} - Birth: {self.birth} - \
Position: {self.position} - Skills: {self.skill} - Started: {self.started}"


class TechEmployee(Employee):
    def __init__(self, name, birth: int, position, skill: int, started: int, program_language, projects: int):
        super().__init__(name, birth, position, skill, started)
        self.language = program_language
        self.projects = projects


Phuc = Employee("Dung", 2002, "AI Team", 120, 2020)
Hieu = Employee("Cong", 2001, "IT Team", 100, 2019)
Dang = Employee("Ban", 2002, "AI Team", 100, 2018)
An = Employee("An", 2002, "IT Team", 100, 2030)

result = Employee.three_best_employee()
[print(ele) for ele in result]