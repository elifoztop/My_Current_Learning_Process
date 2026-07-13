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

# QUESSTIONS:

# 1) peoples tablosunda, ortalama yaşın üzerinde olan kişileri getirin.

# 2) peoples tablosunda, e-posta adresinin @ işaretinden önceki kısmı 10 karakterden uzun olan kişileri getirin.

#3) appearance tablosunda, kilo/boy² oranı (basit bir BMI hesaplaması) en yüksek olan kişiyi getirin.

# 4) appearance tablosunda, saç rengine göre gruplandırıp her grubun kişi sayısını ve ortalama kilosunu getirin.

# 5) peoples tablosunda, adının harf sayısına göre artan sırada  sıralayarak getirin.


def quiz(cursor,conn):
    print("\nQUESS 1\n")
    cursor.execute('''SELECT * FROM Peoples WHERE age>(SELECT AVG(age) FROM Peoples)''')
    print(*cursor.fetchall(),sep='\n')

    print("\nQUESS 2\n")
    cursor.execute('''SELECT * FROM Peoples WHERE LENGTH(email)>20''')
    print(*cursor.fetchall(),sep='\n')

    print("\nQUESS 3\n")
    cursor.execute('''SELECT id,MAX(weight/(height*height)) FROM Appearance''')
    print(f"id={cursor.fetchone()[0]}")

    print("\nQUESS 4\n")
    cursor.execute('''SELECT hair_color,COUNT(*),AVG(weight) FROM Appearance GROUP BY hair_color''')
    results=cursor.fetchall()
    for result in results:
        print(f"{result[0]}={result[1]} --{result[2]}")

    print("\nQUESS 5\n")
    cursor.execute('''SELECT * FROM Peoples ORDER BY LENGTH(name) ''')
    print(*cursor.fetchall(),sep='\n')

def main():
    conn, cursor = crate_datebase()
    try:
        crate_table(cursor)
        add_data(cursor)
        quiz(cursor,conn)
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

if __name__ == '__main__':
    main()