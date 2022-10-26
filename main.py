from flask import Flask, render_template, request, url_for, redirect, flash
import mysql.connector
from flask_wtf import FlaskForm
from wtforms import Form, StringField, SubmitField, validators
from wtforms.validators import DataRequired
from datetime import datetime
import os

#create Flask instance
app = Flask(__name__)


#establish connection to mysql
db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Moxie2020!',
    database='pizzadb'
)

#cursor creation
mycursor = db.cursor()

class ToppingForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])

class PizzaForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)]) 


#homepage route
@app.route("/")
def home():
    #Get all Toppings
    mycursor.execute("SELECT * FROM Toppings")
    data = mycursor.fetchall()

    mycursor.execute("SELECT * FROM Pizzas")
    pizza_data = mycursor.fetchall()

    return render_template('index.html', data=data, pizza_data=pizza_data)

    

@app.route("/creation/<string:id>/")
def article(id):

    data = mycursor.execute("SELECT * FROM Pizzas WHERE id =%s", [id])

    data = mycursor.fetchone()

    return render_template('masterpiece.html', data=data)


#Get all Toppings
@app.route('/toppings')
def toppings():
    
    #get Toppings
    mycursor.execute("SELECT * FROM Toppings")

    toppings = mycursor.fetchall()

    return render_template('toppings.html', toppings=toppings)

    
#Add a Topping
@app.route('/topping/add', methods=['GET', 'POST'])
def add_toppings():
    form = ToppingForm(request.form)
    if request.method == 'POST' and form.validate():
        topping_name = form.name.data

        # Execute cursor
        mycursor.execute("INSERT INTO Toppings(id, topping_name, timestamp) VALUES (NULL, %s, NOW())",(topping_name,))

        # Commit to DB
        db.commit()

        #Success Message
        flash('Topping Created', 'success')

        return redirect(url_for("home"))
    return render_template('add_topping.html', form=form)

@app.route('/edit_topping/<string:id>', methods=['GET','POST'])
def edit_topping(id):
    #get topping by ID
    mycursor.execute("SELECT topping_name FROM Toppings WHERE id = %s", [id,])

    fetchit = mycursor.fetchone()
    
    # Implement Form
    form = ToppingForm(request.form)

    #form Fields
    form.name.data = fetchit

    if request.method == 'POST':
        name = request.form['name']
        

        mycursor.execute("UPDATE Toppings SET topping_name=%s WHERE id = %s",(name, id))

        db.commit()

        flash('Topping Updated', 'success')

        return redirect(url_for('home'))

    return render_template('updateTopping.html', form=form)

@app.route('/delete_topping/<string:id>', methods=['POST'])
def delete_topping(id):
    
    #execute query
    mycursor.execute("DELETE FROM Toppings Where id = %s", [id])

    #commit
    db.commit()

    flash('Article Deleted', 'success')

    return redirect(url_for('dashboard'))


    

#PIZZA CREATION METHODS

#Add a Pizza
@app.route('/pizza/add', methods=['GET', 'POST'])
def add_pizza():
    mycursor.execute("SELECT * FROM Toppings")
    data = mycursor.fetchall()
    if request.method == 'POST':
        checked = request.form.getlist('checked_toppings')
        pizza_name = request.form.get('pizza_name')
        for checks in checked:
            query = "INSERT INTO Pizzas(id, pizza_name, topping_id, timestamp) VALUES (NULL, %s, %s, NOW())"
            mycursor.execute(query, (pizza_name, checks))
            db.commit()
    return render_template('pizza.html', data=data)

# Update a Pizza
@app.route('/edit_pizza/<string:id>', methods=['GET','POST'])
def edit_topping(id):
    #get topping by ID
    mycursor.execute("SELECT * FROM Pizzas WHERE id = %s", [id,])

    fetchit = mycursor.fetchone()
    
    # Implement Form
    form = ToppingForm(request.form)

    #form Fields
    form.name.data = fetchit

    if request.method == 'POST':
        name = request.form['name']
        

        mycursor.execute("UPDATE Toppings SET topping_name=%s WHERE id = %s",(name, id))

        db.commit()

        flash('Topping Updated', 'success')

        return redirect(url_for('home'))

    return render_template('updateTopping.html', form=form)

#@app.route('/pizza/update/<int:id>', methods=['POST', 'GET'])
#def update(id):

#Delete Topping
#@app.route('/delete_topping/<string:id>', methods = ['GET','POST'])
#def delete(id):
       # query = ("DELETE FROM Toppings WHERE id=%s", (id,))
        #mycursor.execute(query, (id))
        #db.commit()
       # return redirect(url_for('index'))




#Bad URL page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

#Internal error page
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500





if __name__ == "__main__":
    app.secret_key='shhhhh smiley face'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(port=5200)