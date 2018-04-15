class Employee():
    e_count = 0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.e_count += 1

    def get_emp_data(self):
        return 'Name: {}\nSalary: {}'.format(self.name,self.salary)

class Qualification():
    q_count = 0
    def __init__(self,degree,experience):
        self.degree = degree
        self.exp = experience
        Qualification.q_count += 1

    def get_qualification(self):
        return 'Degree: {}\nExperience: {}'.format(self.degree,self.exp)

class Scientist(Employee,Qualification):
    s_count = 0
    def __init__(self,name,salary,degree,experience,domain):
        Scientist.s_count += 1
        Employee.__init__(self,name,salary)
        Qualification.__init__(self,degree,experience)
        self.domain=domain

    def get_scientist_details(self):
        return '{}\n{}\nDomain: {}\nEmployee count:{}\nQualification count:{}\nScientist count:{}'.format(self.get_emp_data(),self.get_qualification(),self.domain,Employee.e_count,Qualification.q_count,self.s_count)

class Manager(Employee,Qualification):
    m_count = 0
    def __init__(self,name,salary,degree,experience):
        Manager.m_count += 1
        Employee.__init__(self,name,salary)
        Qualification.__init__(self,degree,experience)

    def get_scientist_details(self):
        return '{}\n{}\nEmployee count:{}\nQualification count:{}\nManager count:{}'.format(self.get_emp_data(),self.get_qualification(),Employee.e_count,Qualification.q_count,self.m_count)


scientist = Scientist("Jacob","150000","PhD",15,"Astro Physics")
print('\nScientist Details:\n')
print(scientist.get_scientist_details())
print('\n\nManager Details:\n')
manager = Manager("Alex","35000","MBA",5)
print(manager.get_scientist_details())