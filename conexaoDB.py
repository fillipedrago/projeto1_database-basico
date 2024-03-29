import psycopg2

try:
    conn = psycopg2.connect("host=127.0.0.1 port=5433 dbname=myfirstdb user=postgres password=PI314159")
except psycopg2.Error as e:
    print("Error: Could not make connection to the Postgres database")
    print(e)

try:
    cur = conn.cursor()
except psycopg2.Error as e:
    print("Error: Could not get curser to the Database")
    print(e)

conn.set_session(autocommit=True)

cur.execute("DROP TABLE IF EXISTS students")

try:
    cur.execute("CREATE TABLE IF NOT EXISTS students (student_id int, name varchar,\
                age int, gender varchar, subject varchar, marks int);")
except psycopg2.Error as e:
    print("Error: Issue creating table")
    print (e)

try:
    cur.execute("INSERT INTO students (student_id, name, age, gender, subject, marks)\
                VALUES (%s, %s, %s, %s, %s, %s)",
                (1, "Raj", 23, "Male", "Python", 85))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("INSERT INTO students (student_id, name, age, gender, subject, marks)\
                VALUES (%s, %s, %s, %s, %s, %s)",
                (2, "Priya", 22, "Female", "Python", 86))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("SELECT * from students;")
except psycopg2.Error as e:
    print("Error: select *")
    print(e)

row = cur.fetchone()
while row:
    print(row)
    row = cur.fetchone

cur.close()
conn.close()