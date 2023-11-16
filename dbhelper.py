import mysql.connector
import pandas as pd
class DB:
    def __init__(self):
        # connect to the data base connector
        try:
            self.conn = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='',
                database='indigo'
            )
            self.mycursor = self.conn.cursor()
            print('connection established')
        except:
            print('connection error')

    def fetch_city(self):
        city=[]
        self.mycursor.execute("""
        select  distinct(Destination) from indigo.`flights_cleaned - flights_cleaned`
        union
        select distinct(source) from indigo.`flights_cleaned - flights_cleaned`
        """)
        data=self.mycursor.fetchall()

        for i in data:
            city.append(i[0])
        return city

    def fetch_all_flights(self,source,destination):
        self.mycursor.execute("""
        select Airline,Route,Dep_Time,Duration,Price,Date_of_Journey from indigo.`flights_cleaned - flights_cleaned`
        where Source='{}' and Destination='{}'
        """.format(source,destination))
        data=self.mycursor.fetchall()
        return data

    def fetch_airline_frequency(self):
        airline=[]
        frequency=[]
        self.mycursor.execute("""
        select Airline,count(*) from indigo.`flights_cleaned - flights_cleaned`
        group by Airline
        """)
        data=self.mycursor.fetchall()
        for item in data:
            airline.append(item[0])
            frequency.append(item[1])
        return airline,frequency

    def busy_airport(self):
        city=[]
        frequency=[]
        self.mycursor.execute("""
        select source as 'busy_airport',count(*)  from (select Source from indigo.`flights_cleaned - flights_cleaned`

        union all 
        select Destination from indigo.`flights_cleaned - flights_cleaned`) t

        group by t.source
        order by count(*) desc""")
        data=self.mycursor.fetchall()
        for i in data:
            city.append(i[0])
            frequency.append(i[1])
        return city,frequency

    def Date_of_journey(self):
        self.mycursor.execute("""
        select Date_of_journey,count(*) from indigo.`flights_cleaned - flights_cleaned`
            group by Date_of_journey""")
        data=self.mycursor.fetchall()
        date=[]
        frequency=[]
        for i in data:
            date.append(i[0])
            frequency.append(i[1])

        D_o_j=pd.DataFrame({'Date':date,'frequency':frequency})
        return D_o_j

db=DB()


busy_airport = db.busy_airport()
print(db.Date_of_journey())