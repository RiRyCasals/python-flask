import os
import sqlite3

code = '1510065'

conn = sqlite3.connect(os.path.dirname(__file__) + '/zip.sqlite')

c = conn.cursor()
res = c.execute('SELECT * FROM zip WHERE code=?', [code])

for row in res:
    print(row)
