class Book:
    def __init__(self,n,p,a):
        self.name=n
        self.price=p
        self.author=a
    def __truediv__(self,other):
        return self.price/other-100
    def __mul__(self,other):
        return self.price*other
p=Book('Python',3000,'dfg')
d=Book('Django',4000,'dfg')
n=int(input())
print(p*n)
print(p/2)