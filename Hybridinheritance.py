#Hybrid inheritance
class Company:
    Cname='Apple'
    headquarter='California'
    products='iPhone,Apple TV,macOS..'
class Iphone(Company):
    def iphone15(self):
        print('iphone15')
        print('iphone15 plus 128gb')
        print('iphone15 plus 256gb')
        print('iphone15 plus 512gb')
    def iphone14(self):
        print('iphone14')
        print('iphone14 5g 128gb')
        print('iphone14 5g plus 256gb')
        print('iphone14 5g plus 512gb')
class Macbook(Company):
    def macbook_Air(self):
        print('Apple 2022 Macbook Air M1')
        print('Apple 2022 Macbook Air M2')
        print('Apple 2023 Macbook Air Pro M2')
    def macbook_Pro(self):
        print('Apple Macbook Pro M2')
        print('Apple Macbook Pro M2 Max')
        print('Apple Macbook Pro M1 Max')
class User(Iphone,Macbook):
    def __init__(self,n,m):
        self.name=n
        self.mobile=m
    def purchase(self):
        print(Company.Cname)
        print('User name:',self.name)
        print('Mobile :',self.mobile)
obj=User('Nihal',8081773606)