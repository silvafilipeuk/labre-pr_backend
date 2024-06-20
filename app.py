from flask import Flask, jsonify
from flask_mysqldb import MySQL
from dotenv import load_dotenv
from pathlib import Path
import os

dotenv_path = Path('./database.env')
load_dotenv(dotenv_path=dotenv_path)

app = Flask(__name__)
app.config['MYSQL_HOST'] = os.getenv("MYSQL_HOST")
app.config['MYSQL_USER'] = os.getenv("MYSQL_USER")
app.config['MYSQL_PASSWORD'] = os.getenv("MYSQL_PASSWORD")
app.config['MYSQL_DB'] = os.getenv("MYSQL_DB")
mysql = MySQL(app)

if __name__ == '__main__':
    app.run(debug=True)

@app.route("/")
def index():
        return "Labre-PR API - Live!"

@app.route("/associates")
def get_associates():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * from associados")
        associates = cur.fetchall()
        return jsonify(associates)