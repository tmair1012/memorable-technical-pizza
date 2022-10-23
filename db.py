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
#mycursor.execute('CREATE TABLE Pizzas (id int PRIMARY KEY AUTO_INCREMENT, pizza_name VARCHAR(50), timestamp TIMESTAMP)')

#toppings table creation
#mycursor.execute('CREATE TABLE Toppings (id int PRIMARY KEY AUTO_INCREMENT, topping_name VARCHAR(50), timestamp TIMESTAMP)')

#mycursor.execute('''CREATE TABLE Masterpieces (
    #id int PRIMARY KEY AUTO_INCREMENT,
    #pizzaID int,
    #toppingID int,
    #FOREIGN KEY (pizzaID) REFERENCES pizzas(id),
    #FOREIGN KEY (toppingID) REFERENCES toppings(id),
    #created_by VARCHAR(50),
    #timestamp TIMESTAMP)''')

#mycursor.execute('''INSERT INTO pizzas (pizza_name)
#VALUES ('Buffalo Chicken')''')

#mycursor.execute('''INSERT INTO Toppings (topping_name)
#VALUES
#('Sausage'),
#('Anchovies'),
#('Mushrooms'),
#('Bacon'),
#('White Onion'),
#('Red Onion'),
#('Garlic'),
#('Ham'),
#('Canadian Bacon'),
#('Pineapple'),
#('Sprinkles')
#''')
#db.commit()

#mycursor.execute('UPDATE Toppings SET timestamp = NOW()')
#db.commit()