import psycopg2

def createTable(cursor):
    command = '''
        CREATE TABLE users (
            id serial,
            firstname VARCHAR(25) NOT NULL,
            lastname VARCHAR(25) NOT NULL,
            PRIMARY KEY (id)
        )
        ''' 
    cursor.execute(command)
    print('Table created successfully')

def createTableRelation(cursor):
    command = '''
        CREATE TABLE address (
            user_id int NOT NULL,
            city VARCHAR(30) NOT NULL,
            state VARCHAR(30) NOT NULL,
            PRIMARY KEY (user_id),
            CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES users (id)
        )
        ''' 
    cursor.execute(command)
    print('Table created successfully')

def insertData(cursor,user_id,city,state):
    insert_query = "insert into address (user_id,city,state) values(%s,%s,%s)"
    record_to_insert = (user_id,city,state)
    cursor.execute(insert_query,record_to_insert) 
    print('Insertion successfull')

def updateTableData(cursor):
    cursor.execute("UPDATE users SET age = 23 where id = 3")
    print('Data Updated Successfully')

#  Note -> while deleting data from table make sure you first delete the fk one data then the pk one later
#  fk ( Foreign Key ) , pk ( Primary Key ) 
def deleteFromTable(cursor):
    cursor.execute("DELETE FROM users WHERE id = 3")
    print('Data Deleted Successfully')

# Note -> while altering column if column is not null then define it as default some_value 
def alterColumn(cursor):
    #cursor.execute("ALTER TABLE address ADD CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE")
    #cursor.execute("ALTER TABLE address DROP CONSTRAINT fk_user_id")
    cursor.execute("ALTER TABLE users ADD COLUMN age int ")
    print('Altered Successfully')

def getRecords(cursor):
    cursor.execute('select * from address')
    record = cursor.fetchall()
    print('Records',record)


connection = None 
try:
    connection = psycopg2.connect(user='postgres',password='postgres',host='127.0.0.1',port='5432',database='postgres')
    cursor  =  connection.cursor()
    print('Connected to BD ->\n')
    #createTable(cursor)
    #createTableRelation(cursor)
    #insertData(cursor,3,'Satna','M.P')
    #updateTableData(cursor)
    deleteFromTable(cursor)
    #alterColumn(cursor)
    getRecords(cursor)
    connection.commit()
except (Exception,psycopg2.Error) as error:
    print(error)
finally:
    if connection is not None:
        cursor.close()
        connection.close()
        print("\nDB connection closed ->")
print("Done :)")
