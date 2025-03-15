import os
import subprocess
import pickle
import hashlib
import sqlite3
from flask import Flask, request

app = Flask(__name__)

# **1. Command Injection**
@app.route('/ping', methods=['GET'])
def ping():
    ip = request.args.get('ip', '')
    response = subprocess.Popen(f"ping -c 3 {ip}", shell=True, stdout=subprocess.PIPE)
    return response.stdout.read()

# **2. Insecure Deserialization**
@app.route('/load', methods=['POST'])
def load():
    data = request.form.get('data')
    obj = pickle.loads(data.encode())  # Unsafe deserialization
    return str(obj)

# **3. Hardcoded Password**
HARDCODED_PASSWORD = "admin123"  # Vulnerability: Hardcoded credentials

# **4. SQL Injection**
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"  # SQL Injection
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()
    
    return "Login successful" if user else "Login failed"

# **5. Weak Hashing Algorithm**
def weak_hash(password):
    return hashlib.md5(password.encode()).hexdigest()  # Weak MD5 Hashing

# **6. Arbitrary File Read**
@app.route('/read', methods=['GET'])
def read_file():
    filename = request.args.get('file', '')
    with open(filename, 'r') as file:
        return file.read()

if __name__ == '__main__':
    app.run(debug=True)
