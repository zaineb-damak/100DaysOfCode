class Job():
    name = None
    salary = None
    hoursWorked = None

    def __init__(self, name, salary, hoursWorked):
        self.name = name
        self.salary = salary
        self.hoursWorked = hoursWorked

    def print(self):
        print(f"name : {self.name}, salary : {self.salary}, work hours : {self.hoursWorked}")

class Doctor(Job):
    experience = None
    speciality = None

    def __init__(self, name , salary, hoursWorked, experience, speciality):
        super.__init__(name, salary, hoursWorked)
        self.experience = experience
        self.speciality = speciality
    
    def print(self):
         print(f"name : {self.name}, salary : {self.salary}, work hours : {self.hoursWorked}, experience : {self.experience}, speciality : {self.speciality}")

class Teacher(Job):
    subject = None
    position = None

    def __init__(self, name , salary, hoursWorked, subject, position):
        super().__init__(name, salary, hoursWorked)
        self.subject = subject
        self.position = position

    def print(self):
         print(f"name : {self.name}, salary : {self.salary}, work hours : {self.hoursWorked}, position : {self.position}, subject : {self.subject}")    

lawyer = Job("lawyer", 100000, 40)
lawyer.print()