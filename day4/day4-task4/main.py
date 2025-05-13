class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"My name  {self.name},{self.age} years old, {self.gender}.")
        
class Employee:
    def __init__(self, employee_id, position, salary):
        self.employee_id = employee_id
        self.position = position
        self.salary = salary

    def work(self):
        print(f"Employee {self.employee_id}  working as a {self.position}.")

    def get_salary(self):
        print(f"Employee {self.employee_id}'s salary  {self.salary}.")
        
person = Human("Alaa", 24, "Male")
person.introduce()

person2 = Human("mohammed", 24, "Male")
person2.introduce()

worker = Employee("1", "Developer", 5000)
worker.work()
worker.get_salary()

worker2 = Employee("2", "software engineer", 6000)
worker2.work()
worker2.get_salary()