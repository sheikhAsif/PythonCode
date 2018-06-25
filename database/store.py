import sqlite3 as sql
db = sql.connect('user.db')
c = db.cursor()
cmd = "create table student(sno int(6) primary key,name text not null,course text not null,fees float not null)"
c.execute(cmd)
cmd = "insert into student values(1,'ram','python',15000)"
c.execute(cmd)
db.commit()
c.close()
db.close()

