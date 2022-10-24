from flask import Flask, render_template, request
import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Moxie2020!',
    database='pizzadb'
)
mycursor = db.cursor()
app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    mycursor.execute("SELECT topping_name FROM Toppings")
    data = mycursor.fetchall()
    return render_template('index.html', data=data)

#@app.route("/updateToppings/<int:id>", methods=['GET', 'POST'])
#def updateToppings(id):
    
#Bad URL page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

#Internal error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500


    


if __name__ == "__main__":
    app.run()