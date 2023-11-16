
import mysql.connector

# connect to the data base connector
try:
    conn=mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='indigo'
    )
    mycursor=conn.cursor()
    print('connection established')
except:
    print('connection error')

#create database on the db servor

#mycursor.execute('create database indigo') #we have create database indigo  on mysql

#conn.commit() #for changing in database server
#create table
#airport->airport_id,code,name,city

# #mycursor.execute("""
# #create TABLE airport(
#     airport_id INTEGER PRIMARY KEY,
#     code VARCHAR(10) NOT NULL,
#     city VARCHAR(50) NOT NULL,
#     name VARCHAR(255) NOT NULL
# )
# """)
#conn.commit() # for changing


#INSERT DATA TO THE TABLE

# mycursor.execute("""
# insert into airport values
# (1,'del','new_delhi','IGIA'),
# (2,'CCU','kilkata','NSCA'),
# (3,'BOM','Mumbai','CSMA')
# """)
# conn.commit()

#search/retrieve

mycursor.execute(" select * from airport where airport_id>1")
data=mycursor.fetchall()
print(data)
for i in data:
    print(i[3])

mycursor.execute("""
update airport
set city='Bombay'
where airport_id=3
""")
conn.commit()
print(data)

mycursor.execute("""delete from airport where airport_id=3

""")
conn.commit()

mycursor.execute('select * from airport')
data=mycursor.fetchall()
print(data)