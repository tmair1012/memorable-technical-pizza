import mysql.connector

#establish connection to mysql
db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Moxie2020!',
    database='pizzadb'
)

mycursor = db.cursor()

#mycursor.execute(''' DROP TABLE Masterpieces
#''')

#mycursor.execute('USE pizzadb')

#mycursor.execute("""ALTER TABLE Pizzas
#DROP CONSTRAINT pizzas_ibfk_1
#""")

#mycursor.execute("""ALTER TABLE Pizzas
#ADD CONSTRAINT pizzas_ibfk_1
#FOREIGN KEY(topping_id) REFERENCES Toppings(id)
#ON DELETE CASCADE
#ON UPDATE CASCADE
#""")

#pizza table creation
#mycursor.execute('CREATE TABLE Pizzas (id int PRIMARY KEY AUTO_INCREMENT, pizza_name VARCHAR(50), timestamp TIMESTAMP)')

#toppings table creation
#mycursor.execute('CREATE TABLE Toppings (id int PRIMARY KEY AUTO_INCREMENT, topping_name VARCHAR(50), timestamp TIMESTAMP)')


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

#mycursor.execute('''INSERT INTO Pizzas (pizza_name)
#VALUES
#('Meat Lovers'),
#('Alfredo'),
#('Buffalo Chicken'),
#('Veggie'),
#('Hawaiian'),
#('Breakfast'),
#('Cheese')
#''')
#db.commit()




