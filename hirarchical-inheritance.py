#Hirarchical Inheritance
class Jsp:               #Parent
    Name='Jspider'
    Add='Marathahalli'
    def __init__(self,n,a,m,y):
        self.name=n
        self.age=a
        self.mobile=m
        self.yop=y
    @classmethod
    def Std_details(cls):
        print('Name:',cls.Name)
        print("Address:",cls.Add)

class Pythonfull_d(Jsp):           # First Child
    mentor='Harshad Sir'
    fee=35000
    def __init__(self,n,a,m,y,s):
        super().__init__(n,a,m,y)
        self.stream=s

    def course_details(self):
        print('# Database')
        print('# Web Tech')
        print('# Python')
        print('# Django and Flask')
    @classmethod
    def Std_details(cls):
        super().Std_details()
        print(cls)

class Javafull_d(Jsp):             # Second Child
    mentor="Raveesh Sir"
    fee=36000
    def __init__(self,n,a,m,y,s):
        super().__init__(n,a,m,y)
        self.stream=s

    def course_details(self):
        print('# Database')
        print('# Core Java')
        print('# J2EE')
        print('# Frameworks')
        print('# Web Tech')
        print('# Web services')

p=Pythonfull_d()
j=Javafull_d()