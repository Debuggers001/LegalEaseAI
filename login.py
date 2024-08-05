from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database configuration
# ... (your database configuration code here)

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",          # Replace with your MySQL server hostname or IP address
    user="root",      # Replace with your MySQL username
    password="@kiman2003",  # Replace with your MySQL password
    database="login"   # Replace with the name of your MySQL database
)

# Create a cursor object to interact with the database
cursor = db.cursor()

@app.route('/')
def home():
    if 'username' in session:
        return 'Logged in as ' + session['username'] + '<br>' + \
               '<a href="/logout">Logout</a>'
    return 'You are not logged in<br><a href="/login">Login</a>'

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        cursor = db.cursor()
        insert_query = "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)"
        values = (username, password, email)

        try:
            cursor.execute(insert_query, values)
            db.commit()
            return 'Signup successful!<br><a href="/login">Login</a>'
        except mysql.connector.IntegrityError:
            db.rollback()
            return 'Username or email already exists. Please choose another.<br><a href="/signup">Signup</a>'

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])

def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor = db.cursor()
        select_query = "SELECT * FROM users WHERE username = %s AND password = %s"
        values = (username, password)

        cursor.execute(select_query, values)
        user = cursor.fetchone()

        if user:
            session['username'] = username
            return redirect('/')
        else:
            return 'Login failed. Please check your credentials.<br><a href="/login">Login</a>'

    return render_template('login.html')


    return render_template('login.html')  # Render the HTML template

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
