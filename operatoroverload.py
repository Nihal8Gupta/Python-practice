class Rectangle:
    def __init__(self,l,w):
        self.area=l*w
    def __gt__(self,other):
       return True if self.area>other.area else False
            
r1=Rectangle(10,20)
r2=Rectangle(20,40)
print(r1>r2)