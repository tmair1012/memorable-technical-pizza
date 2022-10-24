from flask import Flask, render_template, request
app = Flask(__name__)
import mysql.connector
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os



#Secret Key
SECRET_KEY = os.urandom(32)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Moxie2020!@localhost/pizza_creator'
app.config["SECRET_KEY"] = "alalalala"
db = SQLAlchemy(app)


#initialize Database


#homepage route
@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')


#@app.route("/updateToppings/<int:id>", methods=['GET', 'POST'])
#def updateToppings(id):

#Toppings Class
class Toppings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable = False, unique=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Name %r>' % self.name

#topping form
class ToppingForm(FlaskForm):
    name = StringField("Add a Topping Name", validators=[DataRequired()])
    submit = SubmitField("Add Topping")
#Topping Page
@app.route('/topping', methods=['GET', 'POST'])
def toppings():
    name = None
    form = ToppingForm()
    #validators
    return render_template('topping.html',
        name = name,
        form = form)

@app.route('/topping/add', methods=['GET', 'POST'])
def add_toppings():
    topping_name = None
    form = ToppingForm()
    if form.validate_on_submit():
        topping_name = Toppings.query.filter_by(topping_name=form.name.data).first()
        if topping_name is None:
            topping_name = Toppings(topping_name=form.name.data)
            db.session.add(topping_name)
            db.session.commit()
        topping_name = form.name.data
        form.name.data = ''
    available_toppings = Toppings.query
    return render_template('topping.html',
    form=form,
    topping_name=topping_name,
    available_toppings = available_toppings
    )





#Bad URL page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

#Internal error page
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500


    
with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(port=5000, debug = True)