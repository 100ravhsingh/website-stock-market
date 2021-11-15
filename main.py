from flask import Flask, render_template, request, redirect, session
# import os
import mysql.connector

app = Flask(__name__, template_folder='template')
# app.secret_key=os.urandom(24) # session set 24 character key

# connect to sql
conn = mysql.connector.connect(host="remotemysql.com", user="YaEpvwldhp", password="An8ukY1faE", database="YaEpvwldhp")
# communicate with database using cursor
cursor = conn.cursor()
@app.route('/')
def home():
    return render_template("index.html")
@app.route('/aboutus')
def about():
    return render_template("aboutus.html")

@app.route('/course')
def course():
    return render_template("knowcourse.html")

@app.route('/financial_service')
def service():
    return render_template("financial.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@app.route('/registration')
def registration():
    return render_template("registration.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/login_validation', methods=['POST'])
def login_validation():
    # data receive from login page
    email = request.form.get('fullemail')
    password = request.form.get('fullpassword')

    cursor.execute("""SELECT * FROM `stockdb` WHERE
     `Email` = '{}' AND `Password` = '{}'""".format(email, password))
    stockdb = cursor.fetchall()
    if len(stockdb)>0:
        return redirect('/dashboard')
    else:
        return redirect('/login')

@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form.get('fullname')
    email = request.form.get('fullemail')
    mob_number = request.form.get('fullnumber')
    password = request.form.get('fullpassword')
    city_name = request.form.get('fullcity')

    cursor.execute("""INSERT INTO `stockdb` (`Id`, `Name`, `Email`, `Number`, `Password`, `City`) 
    VALUES (NULL, '{}', '{}', '{}', '{}', '{}')""".format(name,email,mob_number,password,city_name))
    conn.commit()
    return "User registered successfully"

if __name__ == '__main__':
    app.run(debug=True)