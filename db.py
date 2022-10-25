import mysql.connector

#establish connection to mysql
db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Moxie2020!',
    database='pizzadb'
)

mycursor = db.cursor()

#mycursor.execute(''' ALTER TABLE Pizza
#ADD FOREIGN KEY (topping_id) REFERENCES Toppings(id)
#''')

#mycursor.execute('USE pizzadb')
#database creation
#mycursor.execute('CREATE DATABASE pizza_creator')

#pizza table creation
#mycursor.execute('CREATE TABLE Pizzas (id int PRIMARY KEY AUTO_INCREMENT, pizza_name VARCHAR(50), timestamp TIMESTAMP)')

#toppings table creation
#mycursor.execute('CREATE TABLE Toppings (id int PRIMARY KEY AUTO_INCREMENT, topping_name VARCHAR(50), timestamp TIMESTAMP)')

#mycursor.execute('''CREATE TABLE Masterpieces (
    #id int PRIMARY KEY AUTO_INCREMENT,
    #pizzaID int,
    #toppingID int,
    #FOREIGN KEY (pizzaID) REFERENCES Pizzas(id),
    #FOREIGN KEY (toppingID) REFERENCES Toppings(id),
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

#mycursor.execute('UPDATE Pizzas SET timestamp = NOW()')
#db.commit()

#mycursor.execute('''INSERT INTO Masterpieces (pizzaID, toppingID, created_by)
#VALUES
#(2,52,'Tyler Mair'),
#(2,53,'Tyler Mair'),
#(3,54,'Tyler Mair'),
#(3,56,'Tyler Mair'),
#(3,57,'Tyler Mair'),
#(3,59,'Tyler Mair'),
#(5,57,'Tyler Mair'),
#(5,58,'Tyler Mair'),
#(5,59,'Tyler Mair')
#''')
#db.commit()