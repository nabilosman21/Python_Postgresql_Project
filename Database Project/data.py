import psycopg2

def create():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="54321", host="localhost", port="5432")
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE student(ID SERIAL, NAME TEXT, AGE TEXT, ADDRESS TEXT);
    ''')
    print("Table created")
    conn.commit()
    conn.close()
    print("Connection is a success.")

def insert_data():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="54321", host="localhost", port="5432")
    cur = conn.cursor()

    name = input("Enter name: ")
    age = input("Enter age: ")
    address = input("Enter address: ")

    query = '''
    INSERT INTO student(NAME, AGE, ADDRESS) VALUES (%s, %s, %s);
    '''

    cur.execute(query, (name, age, address))

    print("Data inserted")
    conn.commit()
    conn.close()

# Uncomment the line below if you want to create the table initially
# create()

# Call the insert_data() function to insert data into the table
insert_data()
