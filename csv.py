import csv
def create():
    with open("demo.csv","w") as demo:
        fobj=csv.writer(demo)
        fobj.writerow(eval(input('Enter column name in list')))
        i=1
        while True:
            Id=i
            roll=int(input('Enter roll:'))
            name=input('Enter name:')
            subj=input('Enter subject:')
            r=[Id,roll,name,subj]
            fobj.writerow(r)
            i+=1
            if int(input('Press 1 for stop/Any number'))==1:
                break
        print(i)

create()