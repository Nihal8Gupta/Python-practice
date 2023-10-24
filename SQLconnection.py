import sqlite3
con=sqlite3.connect("demo_db")
Sid=input("Enter the stud id:")
Sname=input("Enter the student name:")
Sroll=input("Enter the roll no:")

query="insert into Student(Sid,Sname,Sroll) values("+Sid+",'"+Sname+"',"+Sroll+")"

con.execute(query)
con.commit()
con.close()
print("Saved")