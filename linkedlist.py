#WAP to create singly linked list
class Linklist:
    def __init__(self,d):
        self.data=d
        self.next=None
head=None
while True:
    data=eval(input("Enter the data/Press stop for break"))
    if data=='stop':
        break
    else:
        obj=Linklist(data)
        if head==None:
            head=obj
        else:
            t.next=obj
        t=obj
        
while head!=None:
    print(head.data)
    head=head.next