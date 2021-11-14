from flask import Flask, render_template, request
app = Flask(__name__, template_folder='template')

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
    return render_template("index.html")

@app.route('/registration')
def registration():
    return render_template("registration.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/login_validation', methods=['POST'])
def login_validation():
    # data receive from here
    email = request.form.get('hemail')
    password = request.form.get('hpassword')
    return "the email is {} and the password is {}".format(email, password)


if __name__ == '__main__':
    app.run(debug=True)