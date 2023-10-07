# MULTIPLE Inheritance
class Men:     #First Parent 
    
    def Mdress(self):
        print('Mens Cloths')
        print("Shirts")
        print("Jeans")
        print("Kurta")
        print("T-shirt")
        print('Party wear')
        print('Footwear')
    
    
class Women:    #Second Parent
    
    def Wdress(self):
        print('womens Cloths')
        print("Sarees")
        print("Jeans")
        print("Kurti")
        print("Tops")
        print('Party wear')
        print('Footwear')
          
class Seller(Men,Women):   # Child
    def __init__(self,n,m,a):
        self.name=n
        self.mobile=m
        self.age=a
    
obj=Seller('Nihal',8081773606,22)
obj.Mdress()
obj.Wdress()