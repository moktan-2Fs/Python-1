import psycopg2 as pg 
conn = pg.connect(
  host = 'localhost',
  dbname = 'postgres',
  user = 'postgres',
  password = '1234',
  port = '5555'
)
cur = conn.cursor()

# cur.execute("""CREATE TABLE IF NOT EXISTS person (
#             id INT PRIMARY KEY,
#             name VARCHAR(255),
#             age INT,
#             gender CHAR
# );
# """)
# name = 'Moktan'
# cur.execute(f"""INSERT INTO person (id,name,age,gender) VALUES 
#             (1, 'Sagar {name}', 22, 'M'),
#             (2, 'Raj {name}', 21, 'M'),
#             (3, 'Kumar {name}', 41, 'M'),
#             (4, 'Laxmi Tamang', 35, 'F')  
# """)
id = int(input('Enter user id: '))
cur.execute(f""" SELECT * FROM person WHERE id = {id};""")
a = cur.fetchone()
print(a, type(a))

cur.execute(""" SELECT * FROM person WHERE age < 30;""")
for row in cur:
  print(row)
conn.commit()

cur.close()
conn.close()
