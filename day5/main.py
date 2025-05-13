class Person:
  
  moods = ("happy", "tired", "lazy")
  def __init__(self,name,money,mood,healthRate):
    self.name=name
    self.money=money
    self.mood=mood
    self.healthRate=healthRate
  def sleep(self,hours):
    if hours == 7:
      self.mood='happy'
    elif hours < 7:
      self.mood='tired'
    else:
      self.mood='lazy'
    return self.mood
  def eat(self,meals):
    if meals == 3:
      self.healthRate='100% hth'
    elif meals == 2:
      self.healthRate='75% hth'
    elif meals == 1:
      self.healthRate='50% hth'
    return self.healthRate
  def buy(self,items):
    if item==1:
      self.money-=10
    return self.money
  
    @property
    def healthRate(self):
        return self._healthRate

    @healthRate.setter
    def healthRate(self, value):
        if 0 <= value <= 100:
            self._healthRate = value
        else:
            print("HealthRate between 0 and 100")
  
class Employee(Person):
    def __init__(self, id, car, email, salary, distanceToWork, name, money, mood, healthRate):
        super().__init__(name, money, mood, healthRate)
        self.id = id
        self.car = car
        self._email = None
        self.email = email  
        self._salary = None
        self.salary = salary  
        self.distanceToWork = distanceToWork

    def work(self, hours):
        if hours == 8:
            self.mood = 'happy'
        elif hours > 8:
            self.mood = 'tired'
        else:
            self.mood = 'lazy'
        return self.mood

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value >= 1000:
            self._salary = value
        else:
            print("wrong salary must equal or greater than 1000")

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" in value and "." in value:
            self._email = value
        else:
            print("wrong email it should be end with @")

  
emp = Employee(1, "Fiat 128", "samy@iti.org", 1500, 20, "Samy", 500, "neutral", 90)

print(emp.salary)     
print(emp.email)    
print(emp.healthRate) 
print(Person.moods)    

emp.salary = 800       
emp.email = "wrongmail" 
emp.healthRate = 1   
    
 
class Office:
  def __init__(self,name,employees):
    self.name=name
    self.employees=employees

class Car:
  def __init__(self,name,fuelRate,velocity):
    self.name=name
    self.fuelRate=fuelRate
    self.velocity=velocity

      