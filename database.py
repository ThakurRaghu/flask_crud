import sqlite3 as sql

#connect to SQLite
con = sql.connect('db_web.db')

#Create a Connection
cur = con.cursor()

#Drop users table if already exsist.
cur.execute("DROP TABLE IF EXISTS student_t3")

#Create users table  in db_web database
sql ='''CREATE TABLE "student_t3" (
	"UID"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"UNAME"	TEXT NOT NULL,
	"EMAIL" TEXT NOT NULL,
	"CONTACT"	TEXT NOT NULL,
	"AGE" INT NOT NULL
)'''
cur.execute(sql)

#commit changes
con.commit()
print('database and table create')
#close the connection
con.close()