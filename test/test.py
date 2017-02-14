import sqlite3

sql = open("bd.sql").read()
con = sqlite3.connect("catalog.db")
cur = con.cursor() 

cur.executescript(sql)