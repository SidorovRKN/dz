import sqlite3
from random import randint as r
conn = sqlite3.connect('new_data.db')

cursor = conn.cursor()
cursor.execute('DROP TABLE new_tab')
cursor.execute('''CREATE TABLE IF NOT EXISTS new_tab(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER, col_2 INTEGER)''')
for i in range(4):
    num = r(0,9)
    num_1 = r(0, 9)
    cursor.execute('''INSERT INTO new_tab(col_1,col_2) VALUES (?,?)''', (num, num_1))
conn.commit()
cursor.execute('''SELECT*FROM new_tab''')
print(cursor.fetchall())
cursor.execute('''SELECT AVG(col_1), AVG(col_2) FROM new_tab''')
nums = cursor.fetchall()[0]
print(nums)
if sum(nums)/2 > 4:
    cursor.execute('''DELETE FROM new_tab where id == '4' ''')
cursor.execute('''SELECT*FROM new_tab''')
print(cursor.fetchall())
