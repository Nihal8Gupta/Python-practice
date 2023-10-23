class Sr:
    def __init__(self,f,l):
        self.n1=f
        self.n2=l
    def __iter__(self):
        self.i=self.n1
        return self
    def __next__(self):
        if self.i<=self.n2:
            if self.n1>1:
                for i in range(2,self.n1//2+1):
                    if self.n1%i==0:
                        return f'{self.n1} is not prime'
                else:
                    return f'{self.n1} is prime'

            else:
                return f'{self.n1} is not prime'
        raise StopIteration
            
s=Sr(0,10)
print('Prime:-')
for i in s:
    print(i,end=' ')