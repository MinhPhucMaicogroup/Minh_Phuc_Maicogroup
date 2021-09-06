from employee import Employee
class TechEmployee(Employee):
    employees = []
    
    def __init__(self, name, birth, position, skill, started, prog_lang, projects):
        super().__init__(name, birth, position, skill, started)
        self.prog_lang = prog_lang
        self.projects = projects
        TechEmployee.recruit_employee(self)

    @classmethod
    def python_team(cls):
        is_python_dev = lambda prog_lang: "Python" in prog_lang
        python_team = []
        for tech_employee in cls.employees:
            if is_python_dev(tech_employee.prog_lang):
                python_team.append(tech_employee)
        return python_team
    
    def __repr__(self):
        return f"Name: {self.name} - Birth: {self.birth} - \
Position: {self.position} - Skills: {self.skill} - Started: {self.started} - \
Languages: {self.prog_lang} - Projects: {self.projects}"

    @classmethod
    def experienced_team(cls):
        proj_demand = lambda proj: proj > 5
        experienced_team = []
        for ele in cls.employees:
            if proj_demand(ele.projects) and ele.get_age() >= 30:
                experienced_team.append(ele)
        return experienced_team


employee21 = TechEmployee("Nguyen Minh Phuc", 2002, "AI Team", 10, 2021,"C++", 6)
employee22 = TechEmployee("Nguyen Ngoc An", 2002, "IT Team", 10, 2021, "C", 10)
employee23 = TechEmployee("Do Ngoc Cuong", 1985, "BI Team", 15, 2020, "C#", 7)
employee24 = TechEmployee("Ho Gia Bao", 1989, "IT Team", 10, 2020, "Java", 8)
employee25 = TechEmployee("Ngo Dinh", 1970, "AI Team", 15, 2021, "Javascript", 9)
employee26 = TechEmployee("Nguyen Phuong Thao", 1975, "BI Team", 20, 2021, "Javascript", 10)
employee27 = TechEmployee("Vo Hoang Ngan", 2002, "AI Team", 25, 2021, "Python", 12)
employee28 = TechEmployee("Tieu Vy", 2001, "BI Team", 15, 2021, "C++", 20)
employee29 = TechEmployee("Nguyen Ngoc Nguyen", 1970, "IT Team", 20, 2021, "Javascript", 7)
employee30 = TechEmployee("Do Quoc Trung", 1995, "AI Team", 30, 2021, "Java", 3)
employee31 = TechEmployee("Nguyen Bao Han", 1970, "AI Team", 15, 2021, "C#", 1)
employee32 = TechEmployee("Nguyen Minh Hieu", 1970, "AI Team", 15, 2021, "R, Python", 2)
employee33 = TechEmployee("Nguyen Tam Nhu", 2003, "IT Team", 20, 2020, "Ruby", 4)
employee34 = TechEmployee("Nguye Ngoc Duy", 2000, "IT Team", 15, 2021, "Swift, C", 2)
employee35 = TechEmployee("Do Quoc Viet", 1998, "IT Team", 10, 2019, "Scala, Swift", 7)

py_team =  TechEmployee.python_team()
str = "Python team"
str = str.center(130, "-")
print(str)
[print(member) for member in py_team]
experience_team = TechEmployee.experienced_team()
print("")
str = "Experience team"
str = str.center(130, "-")
print(str)
[print(member) for member in experience_team]
