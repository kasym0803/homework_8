

import sqlite3 as sq

with sq.connect('student.db3') as con:
    cur = con.cursor()
    # cur.execute('''DROP TABLE students''')
    cur.execute('''CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    surname TEXT,
    year INTEGER,
    hobby TEXT,
    evaluation INTEGER
    )''')

    cur.execute('''UPDATE students SET name = 'genius' WHERE evaluation >= 90''')

    cur.execute('''SELECT rowid, * FROM students''')

    # cur.execute('''SELECT * FROM students WHERE LENGTH(surname) > 8''')
    surname_print = cur.fetchall()
    for i in surname_print:
        print(i)
    for i in surname_print:
        surname = i[1]
        if len(surname) >= 10:
            print(surname)
        else:
            ...
    cur.execute('''SELECT rowid, name FROM student WHERE name = 10''')

    cur.execute('''DELETE FROM students WHERE rowid % 2 = 0''')


    # cur.execute('''UPDATE students SET name = 'genius' WHERE evaluation > 90''')


