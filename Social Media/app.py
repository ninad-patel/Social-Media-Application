from flask import Flask, render_template, request, redirect, url_for, session
import requests
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
app.secret_key = "nano"

# Database Connection
def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="nanoninad",
            database="nano"
        )
        return connection
    except Error as e:
        print(f"Error: '{e}'")
        return None

# Fetch live news from NewsAPI
def fetch_live_news():
    api_key = "" # get api from "https://newsapi.org/"
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "country": "us",
        "category": "business",  # Options: business, entertainment, health, science, sports, technology
        "apiKey": api_key
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        articles = response.json().get("articles", [])
        return articles
    else:
        print("Error fetching news:", response.status_code)
        return []

print(fetch_live_news())
@app.route('/')
def home():
    if 'username' not in session:
        return redirect(url_for('login'))
    articles = fetch_live_news()
    return render_template('home.html', articles=articles)

# Routes
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
            if cursor.fetchone():
                return "Username already exists."
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            connection.commit()
            connection.close()
            return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
            user = cursor.fetchone()
            if user:
                session['username'] = user[0]
                connection.close()
                return redirect(url_for('home'))
            connection.close()
        return "Invalid credentials."
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
