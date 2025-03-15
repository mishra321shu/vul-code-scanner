import os
import sys
import subprocess
import pickle
import sqlite3
import requests

# 🚨 **Vulnerability #1: Hardcoded Credentials**
USERNAME = "admin"
PASSWORD = "password123"  # CWE-798: Use of Hardcoded Credentials

# 🚨 **Vulnerability #2: Insecure Command Execution**
def run_command(cmd):
    subprocess.call(cmd, shell=True)  # CWE-78: OS Command Injection

# 🚨 **Vulnerability #3: Insecure Deserialization**
def load_user_data(filename):
    with open(filename, "rb") as f:
        data = pickle.load(f)  # CWE-502: Insecure Deserialization
    return data

# 🚨 **Vulnerability #4: SQL Injection**
def get_user_info(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"  # CWE-89: SQL Injection
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

# 🚨 **Vulnerability #5: Insecure HTTP Request**
def fetch_data():
    response = requests.get("http://example.com/data")  # CWE-829: Use of Untrusted URL
    return response.text

if __name__ == "__main__":
    print("Executing vulnerable functions...")

    # Exploitable Functions
    run_command("ls -la")
    print(load_user_data("user_data.pkl"))
    print(get_user_info("admin"))
    print(fetch_data())
