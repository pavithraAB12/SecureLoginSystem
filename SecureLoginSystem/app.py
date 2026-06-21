from flask import Flask, render_template, request, redirect, session
import sqlite3
import bcrypt
import re

app = Flask(__name__)
app.secret_key = "mysecretkey"

# Create database and table
def init_db():
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password BLOB
    )
    """)

    conn.commit()
    conn.close()

init_db()

# Home Page
@app.route('/')
def home():
    return redirect('/login')

# Register
@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        # Validation
        if not username or not password:
            return "All fields are required"

        if len(password) < 8:
            return "Password must be at least 8 characters"

        if not re.match(r"^[A-Za-z0-9_]+$", username):
            return "Only letters, numbers and underscore allowed"

        # Hash password
        hashed = bcrypt.hashpw(
            password.encode(),
            bcrypt.gensalt()
        )

        try:
            conn = sqlite3.connect("users.db")
            cur = conn.cursor()

            cur.execute(
                "INSERT INTO users(username,password) VALUES(?,?)",
                (username, hashed)
            )

            conn.commit()
            conn.close()

            return redirect('/login')

        except:
            return "Username already exists"

    return render_template("register.html")

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect("users.db")
        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM users WHERE username=?",
            (username,)
        )

        user = cur.fetchone()

        conn.close()

        if user and bcrypt.checkpw(
            password.encode(),
            user[2]
        ):
            session['user'] = username
            return redirect('/dashboard')

        return "Invalid Username or Password"

    return render_template("login.html")

# Dashboard
@app.route('/dashboard')
def dashboard():

    if 'user' not in session:
        return redirect('/login')

    return render_template(
        "dashboard.html",
        user=session['user']
    )

# Logout
@app.route('/logout')
def logout():

    session.pop('user', None)

    return redirect('/login')

if __name__ == "__main__":
    app.run(debug=True)