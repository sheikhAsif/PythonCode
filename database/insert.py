import sqlite3 as sql

db = sql.connect('user.db')
c = db.cursor()

while True:
    Id = int(input("Enter id of student : "))
    Name =input("Enter name of the student : ")
    Course = input("Enter course detail : ")
    Fees = float(input("fees : "))
   
    cmd = "insert into student values({},'{}','{}',{})".format(Id,Name,Course,Fees)

    c.execute(cmd)
    db.commit()
    
    print("\nStudent Added successfully")

    ch = input("\nPress y to add more : ").strip().lower()
    if ( ch !='y' or 'yes'):
        break

c.close()
db.close()

