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
    mycursor.execute("SELECT * FROM Toppings")
    data = mycursor.fetchall()
    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run()