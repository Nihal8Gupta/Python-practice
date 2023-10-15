class Sr:
    def __init__(self,f,s,n):
        self.up=n
        self.n1=f
        self.n2=s
    def __iter__(self):
        self.i=1
        return self
    def __next__(self):
        if self.i<=self.up:
            d=self.n1
            self.n1+=self.n2
            self.n1,self.n2=self.n2,self.n1
            self.i+=1
            return d
        raise StopIteration
            
s=Sr(0,1,10)
print('Fibon:-')
for i in s:
    print(i,end=' ')