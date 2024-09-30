import sqlite3
connection=sqlite3.connect("students.db")
cursor=connection.cursor()
# table_info="""create table students(Name varchar(50),dept varchar(43),roll_no int(40))"""
# cursor.execute(table_info)
# cursor.execute("""insert into students values('akhil','DS',050)""")
# cursor.execute("""insert into students values('medha','DS',053)""")
# cursor.execute("""insert into students values('komal','DS',047)""")
cursor.execute("""insert into students values('aditya','DS',063)""")
print("all rows are inserted")
data=cursor.execute('select * from students')
for i in data:
    print(i)
print("All files are accessed")

connection.commit()