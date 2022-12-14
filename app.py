from flask import Flask, render_template, request, url_for, redirect, flash
import mysql.connector
from flask_wtf import FlaskForm
from wtforms import Form, StringField, SubmitField, validators
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy



#create Flask instance
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://owteokoewiyuig:2533695a98e84b3fe0e46387925122f306d056583cd2773d1cd1cc9255adf0f0@ec2-54-163-34-107.compute-1.amazonaws.com:5432/ddq76h0h14tc7g'

db = SQLAlchemy(app)
#establish connection to mysql
db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Moxie2020!',
    database='pizzadb'
)

#cursor creation
mycursor = db.cursor()

#Topping Form Creation
class ToppingForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])

#Pizza Form Creation
class PizzaForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)]) 


#Homepage route
@app.route("/")
def home():
    #Get all Toppings
    mycursor.execute("SELECT * FROM Toppings")
    data = mycursor.fetchall()

    #Organize Toppings into their respective pizza names for markdown
    
    #fetch pizza data
    mycursor.execute("SELECT * FROM Pizzas")
    pizza_data2 = mycursor.fetchall()

    return render_template('index.html', data=data, pizza_data2=pizza_data2)

#TOPPING ROUTES 

#Add a Topping
@app.route('/topping/add', methods=['GET', 'POST'])
def add_toppings():
    mycursor.execute("SELECT topping_name FROM Toppings")
    check_duplicate = mycursor.fetchall()
    print(check_duplicate)
    form = ToppingForm(request.form)
    if request.method == 'POST' and form.validate():
        topping_name = form.name.data
        matchingString = "(\'" + topping_name + "\',)"
        if check_duplicate == matchingString:
            return redirect(url_for('page_not_found'))
        else:
        # Execute cursor
            mycursor.execute("INSERT INTO Toppings(id, topping_name, timestamp) VALUES (NULL, %s, NOW())",(topping_name,))

        # Commit to DB
            db.commit()

        #Success Message
            flash('Topping Created', 'success')

            return redirect(url_for("home"))
    return render_template('add_topping.html', form=form)


#Get all Toppings
@app.route('/toppings')
def toppings():
    
    #get Toppings
    mycursor.execute("SELECT * FROM Toppings")

    toppings = mycursor.fetchall()

    return render_template('toppings.html', toppings=toppings)

    

#Edit / update a topping
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

#Delete a topping
@app.route('/delete/<string:id>', methods=['GET','POST'])
def delete_topping(id):
    
    mycursor.execute("DELETE FROM Toppings WHERE id = %s", (id,))

    #commit
    db.commit()

    flash('Article Deleted', 'success')

    return redirect(url_for('home'))
    


    

#PIZZA ROUTES

#Add a Pizza
@app.route('/pizza/add', methods=['GET', 'POST'])
def add_pizza():
    mycursor.execute("SELECT pizza_name FROM Pizzas")
    check_duplicate = mycursor.fetchall()
    mycursor.execute("SELECT * FROM Toppings")
    data = mycursor.fetchall()
    if request.method == 'POST':
        checked = request.form.getlist('checked_toppings')
        pizza_name = request.form.get('pizza_name')
        if check_duplicate != pizza_name:
            for checks in checked:
                query = "INSERT INTO Pizzas(id, pizza_name, topping_id, timestamp) VALUES (NULL, %s, %s, NOW())"
                mycursor.execute(query, (pizza_name, checks))
                db.commit()
                return redirect(url_for('home'))

    return render_template('pizza.html', data=data)

# Update a Pizza
@app.route('/edit_pizza/<string:id>', methods=['GET','POST'])
def edit_pizza(id):
    
    mycursor.execute("SELECT * FROM Toppings")
    topping_data = mycursor.fetchall()
    #get topping by ID
    mycursor.execute("SELECT pizza_name FROM Pizzas WHERE id = %s", [id,])

    fetchit = mycursor.fetchone()
    
    # Implement Form
    form = PizzaForm(request.form)

    #form Fields
    form.name.data = fetchit

    if request.method == 'POST':
       

        name = request.form['name']
        print(name)
        reset_value = None
        checked = request.form.getlist('checked_toppings')

        mycursor.execute("UPDATE Pizzas SET pizza_name=%s WHERE id = %s",(name, id))
        db.commit()

        mycursor.execute("UPDATE Pizzas SET topping_id=%s WHERE id = %s",(reset_value, id))
        db.commit()

        for checks in checked:
            query = "UPDATE Pizzas SET topping_id=%s WHERE id = %s",(checks, id)
            mycursor.execute(query, (checks,))



        flash('Pizza Updated', 'success')

        return redirect(url_for('home'))

    return render_template('updatePizza.html', form=form, topping_data=topping_data)

#Delete Pizza
@app.route('/delete_pizza/<string:id>', methods=['GET','POST'])
def delete_pizza(id):
    
    mycursor.execute("DELETE FROM Pizzas WHERE id = %s", (id,))

    #commit
    db.commit()

    flash('Article Deleted', 'success')

    return redirect(url_for('home'))

#ERRORS PAGES

#Bad URL page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

#Internal error page
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500



#INITIALIZE
if __name__ == "__main__":
    app.secret_key='shhhhh smiley face'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(port=5200)