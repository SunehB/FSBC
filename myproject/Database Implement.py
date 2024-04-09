import sqlite3

db = sqlite3.connect('DataBase.db')
cursor = db.cursor()

table ="""CREATE TABLE IF NOT EXISTS fsbcDB (id INTEGER PRIMARY KEY, date STRING, song STRING, client INTEGER, satid INTEGER);"""
cursor.execute(table)

id = 0
date = '4-7-24'
song = 'Never Gonna Give You Up'
client = 83902
satid = 9797

def insertRow (cursor, id, date, song, client, satid):
    try:
        cursor.execute("INSERT INTO fsbcDB (id, date, song, client, satid) VALUES (?, ?, ?, ?, ?)", (id, date, song, client, satid))
        db.commit()
        print("Insert operation successful")
    except sqlite3.Error as e:
        print("Insert operation failed:", e)

def deleteRow(cursor, id_toDelete):
    try:
        cursor.execute("DELETE FROM fsbcDB WHERE id=?", (id_toDelete,))
        db.commit()
        print("Delete operation successful")
    except sqlite3.Error as e:
        print("Delete operation failed:", e)

def printTable(cursor):
    cursor.execute("SELECT * FROM fsbcDB")
    rows = cursor.fetchall()
    for row in rows:
        print(row)



"""
for i in range(10):
    id += 1
    satid += 10
    insertRow(cursor, id, date, song, client, satid)

printTable(cursor)
id_toDelete = 5
deleteRow(cursor, id_toDelete)
printTable(cursor)


db.close()
"""