class Employee:
    Company_name='SKV'
    Company_location='Banglore'
    emp_count=0
    def __init__(self,n,a,s,e):
        self.name=n
        self.age=a
        self.speci=s
        self.exp=e
        Employee.emp_count+=1
    def __del__(self):
        Employee.emp_count-=1
        
emp1=Employee('Nihal',22,'Developer',9)
emp2=Employee('Akash',22,'Developer',10)
emp3=Employee('Sid',22,'Developer',8)
print(Employee.emp_count)
del emp3
print(Employee.emp_count)