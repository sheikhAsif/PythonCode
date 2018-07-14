import sqlite3 as sql
db = sql.connect('user.db')
c = db.cursor()
cmd = "create table student(id int(6) primary key,name text not null,course text not null,fees float not null)"
c.execute(cmd)
db.commit()
c.close()
db.close()


