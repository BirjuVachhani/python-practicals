class Employee():
    count = 0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    def to_string(self):
        return 'Name: {}\nSalary: {}'.format(self.name,self.salary)

#Driver code
emp1 = Employee('Birju',21100)
emp2 = Employee('Harsh',25200)
emp3 = Employee('Karan',18000)
print(emp1.to_string())
print(emp2.to_string())
print(emp3.to_string())
print('\nTotal count: {}'.format(Employee.count))