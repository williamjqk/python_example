import os
import sqlite3
data_path = "/home/tom/data/my_coin_data"

sql_path = os.path.join(data_path, "evt_sql.db")
conn = sqlite3.connect(sql_path)
c = conn.cursor()
evt_keys = ['id', 'is_best_match', 'is_buy', 'price', 'time', 'trade_id_first', 'trade_id_last', 'vol']

c.execute('''CREATE TABLE COMPANY
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);''')
c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Paul', 32, 'California', 20000.00 )");


t0 = time.time()
for i in range(20000,40000):
    # sql_line = f"INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES ({i}, 'Paul', 32, 'California', 2000{i}.00 )"
    # c.execute(sql_line)
    sql_line = f"INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (?, ?, ?, ?, ?)"
    c.execute(sql_line, [i, 'Paul', 32, 'California', 2000.00 * 10000 + i])

t1 = time.time()
print(f"{t1 - t0}")

conn.commit() # NOTE: 只用执行了commit，sql才会固化到硬盘

# cursor = c.execute("SELECT id, name, address, salary  from COMPANY")
# c.execute("DELETE from COMPANY where ID<30000;")
cursor = c.execute("SELECT id, name, address, salary  from COMPANY where id>30000")
rows = []
for row in cursor:
    rows.append(row)
   # print( "ID = ", row[0])
   # print( "NAME = ", row[1])
   # print( "ADDRESS = ", row[2])
   # print( "SALARY = ", row[3], "\n")
len(rows)
