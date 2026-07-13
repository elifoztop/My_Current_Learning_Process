import sqlite3
import os

def crate_datebase():
    if os.path.exists("Persons.db"):  # böyle bir datebase varsa sil
        os.remove("Persons.db")
    conn=sqlite3.connect("Persons.db") #bağlantı
    cursor=conn.cursor() #imleç
    return conn,cursor

def crate_table(cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Peoples(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL, 
    surname VARCHAR(50) NOT NULL,
    age INTEGER,
    email VARCHAR(50) NOT NULL UNIQUE)
    ''')

    cursor.execute('''
           CREATE TABLE IF NOT EXISTS Appearance(
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           hair_color VARCHAR(50) NOT NULL, 
           eye_color VARCHAR(50) NOT NULL,
           weight INTEGER NOT NULL,
           height FLOAT NOT NULL)
    ''')

"""
not null: olmak zorunda demek
unique: eşsiz, aynı emaile sahip ikikişi olamaz
"""

def add_data(cursor):
    peoples = [
        (1, 'Ayşe', 'Yılmaz', 21, 'ayse.yilmaz@gmail.com'),
        (2, 'Mehmet', 'Kaya', 23, 'mehmet.kaya@gmail.com'),
        (3, 'Zeynep', 'Demir', 20, 'zeynep.demir@gmail.com'),
        (4, 'Can', 'Şahin', 22, 'can.sahin@gmail.com'),
        (5, 'Elif', 'Arslan', 19, 'elif.arslan@gmail.com'),
    ]

    appearance = [
        (1, 'Kahverengi', 'Ela', 62, 1.68),
        (2, 'Siyah', 'Kahverengi', 78, 1.80),
        (3, 'Sarışın', 'Mavi', 55, 1.65),
        (4, 'Kumral', 'Yeşil', 70, 1.75),
        (5, 'Siyah', 'Kahverengi', 58, 1.63),
    ]

    cursor.executemany('''INSERT INTO Peoples VALUES (?,?,?,?,?)''', peoples)
    cursor.executemany('''INSERT INTO Appearance VALUES (?,?,?,?,?)''', appearance)

def sql_select_data(cursor):
    # SELECT ALL
    cursor.execute('''SELECT * FROM Peoples''')
    p_records = cursor.fetchall()
    print("PEOPLE DATA")
    print(*p_records, sep="\n")
    cursor.execute('''SELECT * FROM Appearance''')
    a_records = cursor.fetchall()
    print("APPEARANCE DATA")
    print(*a_records, sep="\n")

def sql_operation(cursor):

    #SELECT COLUMNS

    cursor.execute('''SELECT email FROM Peoples''')
    e_records=cursor.fetchall()
    print("\nEMAIL DATA")
    for row in e_records:
        print(row[0])

    #WHERE CLAUSE
    cursor.execute('''SELECT * FROM Appearance WHERE weight>=60''')
    w_records=cursor.fetchall()
    print("\nWEIGHT>=60 kg DATA")
    for row in w_records:
        print(row[0],row[1],row[2],row[3],row[4])

    #ORDER BY
    cursor.execute('''SELECT name,surname,age FROM Peoples ORDER BY age DESC''')
    age_records=cursor.fetchall()
    print("\nAGE DATA")
    for row in age_records:
        print(row[0],row[1],row[2])

def update_insert_delete_data(cursor,conn):
    cursor.execute('''INSERT INTO Peoples (name,surname,age,email) VALUES (?,?,?,?)''',('Elif','Öztop',19,'elif_o.@gmail.com'))
    conn.commit()
    cursor.execute('''UPDATE Appearance SET hair_color='Siyah' WHERE id=1''')
    conn.commit()
    cursor.execute('''DELETE FROM Peoples WHERE id=5''')
    conn.commit()
    sql_select_data(cursor)

def aggregate_func(cursor):

    #COUNT
    cursor.execute('''SELECT COUNT(*) FROM Appearance''')
    a_results=cursor.fetchone() #one data
    print("\nAPPEARANCE DATA COUNT:",a_results[0])

    #AVERAGE
    cursor.execute('''SELECT AVG(height) FROM Appearance ''')
    h_results=cursor.fetchone()
    print("AVERAGE HEIGTH DATA:",h_results[0])

    #MAX_MİN
    cursor.execute('''SELECT MAX(weight), MIN(weight) FROM Appearance''')
    w_results=cursor.fetchone()
    print("MAX WEIGHT DATA:",w_results[0])
    print("MIN WEIGHT DATA:", w_results[1])

    #GROUP BY
    cursor.execute('''SELECT eye_color,COUNT(*) FROM Appearance GROUP BY eye_color ''')
    e_results=cursor.fetchall()
    print("\nEYE COLOR DATA COUNTS:")
    for row in e_results:
        print(row[0],"=>",row[1])

def main():
    conn,cursor=crate_datebase()
    try:
        crate_table(cursor)
        add_data(cursor)
        print("\nDATABASE CONTENTS\n")
        sql_select_data(cursor)
        sql_operation(cursor)
        print("\nCHANGED DATABASE CONTENTS\n")
        update_insert_delete_data(cursor,conn)
        aggregate_func(cursor)
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

if __name__ == '__main__':
    main()
