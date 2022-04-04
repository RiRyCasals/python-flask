import os
import sqlite3, csv

FILE_SQLITE = os.path.dirname(__file__) + '/zip.sqlite'

conn = sqlite3.connect(FILE_SQLITE)

conn.execute("""
    CREATE TABLE IF NOT EXISTS zip (
        zip_id INTEGER PRIMARY KEY,
        code TEXT,
        ken TEXT,
        shi TEXT,
        cho TEXT
    )
""")

conn.execute('DELETE FROM zip')

def read_csv(fname):
    c = conn.cursor()
    f = open(fname, encoding='cp932')
    reader = csv.reader(f)
    for row in reader:
        code = row[2]
        ken = row[6]
        shi = row[7]
        cho = row[8]
        if cho == '以下に掲載がない場合':
            cho = ''
        print(code, ken, shi, cho)
        c.execute('INSERT INTO zip (code,ken,shi,cho) VALUES (?,?,?,?)',
                  [code, ken, shi, cho])
    f.close()
    conn.commit()

def read_jigyosyo_csv(fname):
    c = conn.cursor()
    f = open(fname, encoding='cp932')
    reader = csv.reader(f)
    for row in reader:
        code = row[7]
        ken = row[3]
        shi = row[4]
        cho = row[5] + row[6] + ' ' + row[2]
        print(code, ken, shi, cho)
        c.execute('INSERT INTO zip (code,ken,shi,cho) VALUES (?,?,?,?)',
                  [code, ken, shi, cho])
    f.close()
    conn.commit()

read_csv(os.path.dirname(__file__) + '/KEN_ALL.CSV')
read_jigyosyo_csv(os.path.dirname(__file__) + '/JIGYOSYO.CSV')

conn.close()
print('ok')
