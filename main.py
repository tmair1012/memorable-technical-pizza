from flask import Flask, render_template, request
app = Flask(__name__)
import mysql.connector
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os


#initialize Database
#establish connection to mysql
db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Moxie2020!',
    database='pizzadb'
)

#cursor creation
mycursor = db.cursor()

#homepage route
@app.route("/", methods=['GET'])
def home():
    mycursor.execute("SELECT topping_name FROM Toppings")
    data = mycursor.fetchall()
    return render_template('index.html', data=data)


#@app.route("/updateToppings/<int:id>", methods=['GET', 'POST'])
#def updateToppings(id):

#Toppings Class
#class Toppings(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
   # name = db.Column(db.String(200), nullable = False, unique=True)
    #date_added = db.Column(db.DateTime, default=datetime.utcnow)

    #def __repr__(self):
        #return '<Name %r>' % self.name

#topping form
#class ToppingForm(FlaskForm):
   # name = StringField("Add a Topping Name", validators=[DataRequired()])
    #submit = SubmitField("Add Topping")
#Topping Page
#@app.route('/topping', methods=['GET', 'POST'])
#def toppings():
    #name = None
   #form = ToppingForm()
    #validators
    #return render_template('topping.html',
       # name = name,
        #form = form)
#Add a Topping
@app.route('/topping/add', methods=['GET', 'POST'])
def add_toppings():
    mycursor.execute("SELECT topping_name FROM Toppings")
    data = mycursor.fetchall()
    if request.method == 'POST':
        topping_name = request.form.get('topping_name')
        query = "INSERT INTO Toppings(id, topping_name, timestamp) VALUES (NULL, %s, NOW())"
        mycursor.execute(query, (topping_name,))
        db.commit()
    return render_template('topping.html', data=data)

#Add a Pizza
@app.route('/pizza/add', methods=['GET', 'POST'])
def add_pizza():
    mycursor.execute("SELECT topping_name id FROM Toppings")
    data = mycursor.fetchall()
    if request.method == 'POST':
        checked = request.form.get('checked_toppings')
        pizza_name = request.form.get('pizza_name')
        query = "INSERT INTO Pizzas(id, pizza_name, topping_name, timestamp) VALUES (NULL, %s, %s, NOW())"
        mycursor.execute(query, (pizza_name, checked))
        db.commit()
    return render_template('pizza.html', data=data)

#@app.route('/pizza/update/<int:id>', methods=['POST', 'GET'])
#def update(id):
  




#Bad URL page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

#Internal error page
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500





if __name__ == "__main__":
    app.run(port=5000)