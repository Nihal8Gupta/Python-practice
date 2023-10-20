class NestedIterator:
    def __init__(self, nestedList):
        self.nums=[]
        def go(u=nestedList):
            for el in u: self.nums.append(el.getInteger()) if el.isInteger() else go(el.getList());
        go()
    
    def next(self) -> int:
        return self.nums.pop(0)
    
    def hasNext(self) -> bool:
         return len(self.nums)>0
N=NestedIterator([1,2,[3,4],5])
#Output [1,2,3,4,5]