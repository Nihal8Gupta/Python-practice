class Link:
    def __init__(self,data):
        self.data=data
        self.next=None
l=[22,34,67,90,-1]
head=None
for i in l:
    if i==-1:
        break
    l=Link(i)
    if head is None:
        head=l
        tail=l
    tail.next=l
    tail=l

k=head
i=0
ip=2
while head!=None:
    if i==ip-1:
        n=head.next
        l=Link(11)
        head.next=l
        l.next=n
        break
    head=head.next
    i+=1
head=k
while head!=None:
    print(head.data)
    head=head.next