import sqlite3
from flask import Flask, request, redirect, render_template, url_for, flash

app = Flask(__name__, template_folder='main', static_folder='main/assets')
app.secret_key = 'your_secret_key'

# Function to initialize database and create table
def init_db():
    try:
        conn = sqlite3.connect('user_data.db')
        cur = conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()
        print("Database and table created successfully.")
    except Exception as e:
        print(f"Error initializing database: {str(e)}")

init_db()

@app.route('/')
def register():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register_user():
    try:
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        print(f"Received form data: Name={name}, Email={email}, Password={password}")
        
        conn = sqlite3.connect('user_data.db')
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO users (name, email, password)
            VALUES (?, ?, ?)
        ''', (name, email, password))
        conn.commit()
        conn.close()
        
        print(f"User {name} registered successfully.")
        return redirect('/')
    except Exception as e:
        print(f"Error registering user: {str(e)}")
        return "An error occurred while registering user."

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        print(f"Received login data: Email={email}, Password={password}")

        conn = sqlite3.connect('user_data.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM users WHERE email = ? AND password = ?', (email, password))
        user = cur.fetchone()
        conn.close()

        if user:
            print(f"Login successful for user: {user[1]}")
            # Redirect to a dashboard or home page after successful login
            return redirect(url_for('dashboard'))
        else:
            print("Login failed. Incorrect email or password.")
            flash('Incorrect email or password. Please try again.')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return "Welcome to your dashboard!"

if __name__ == '__main__':
    app.run(debug=True)