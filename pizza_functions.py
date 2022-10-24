import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Moxie2020!',
    database='pizzadb'
)

mycursor = db.cursor()

#Add a new topping
def addTopping(db, Toppings):
    mycursor = db.cursor()
    query = ("""INSERT INTO Toppings (topping_name, timestamp)
    VALUES
        (%s, 'NOW()')
    """)

    mycursor.execute(query, Toppings)
    db.commit()    

    mycursor.close()
    

#create a new pizza
#def makePizza():

