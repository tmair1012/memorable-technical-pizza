import mysql.connector

#establish connection to mysql
db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Moxie2020!',
    database='pizzadb'
)

mycursor = db.cursor()

#database creation
#mycursor.execute('CREATE DATABASE pizzadb')

#pizza table creation
#mycursor.execute('CREATE TABLE pizzas (id int PRIMARY KEY, pizza_name VARCHAR(50), created_by VARCHAR(50), timestamp TIMESTAMP)')

#toppings table creation
#mycursor.execute('CREATE TABLE toppings (id int PRIMARY KEY, topping_name VARCHAR(50), timestamp TIMESTAMP)')

mycursor.execute('''CREATE TABLE pizza_masterpieces (
    id int PRIMARY KEY,
    pizzaID int,
    toppingID int,
    FOREIGN KEY (pizzaID) REFERENCES pizzas(id),
    FOREIGN KEY (toppingID) REFERENCES toppings(id),
    timestamp TIMESTAMP)''')