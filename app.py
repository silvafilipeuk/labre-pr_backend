from flask import Flask, jsonify, request
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
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)



@app.route("/", methods=['GET'])
def index():
        return "Labre-PR API - Live!"


# Route to retrieve, add or update associates
@app.route("/associates", methods=['GET', 'POST', 'PATCH'])
def get_associates():
        if request.method == 'GET':
                cur = mysql.connection.cursor()
                cur.execute("SELECT * FROM associados")
                associates = [
                        dict(id=row["id"], nome=row["nome"], cpf=row["cpf"],
                                rg=row["rg"], expedidor=row["expedidor"], local_nasc=row["local_nasc"],
                                data_nasc=row["data_nasc"], indicativo=row["indicativo"],
                                classe=row["classe"], profissao=row["profissao"], endereco=row["endereco"],
                                bairro=row["bairro"], cep=row["cep"], cidade=row["cidade"],
                                estado=row["estado"], telefone=row["telefone"], celular=row["celular"],
                                email=row["email"], data_assoc=row["data_assoc"], fistel=row["fistel"], remido=row["remido"] )
                        for row in cur.fetchall()
                ]
                return jsonify(associates), 200
        

# Route to retrieve, or update associate by callsign
@app.route("/associate/<string:callsign>", methods=['GET', 'PATCH'])
def get_associate_by_callsign(callsign):
        if request.method == 'GET':
                cur = mysql.connection.cursor()
                cur.execute("SELECT * FROM associados WHERE indicativo = %s", (callsign,))
                associate = [
                        dict(id=row["id"], nome=row["nome"], cpf=row["cpf"],
                                rg=row["rg"], expedidor=row["expedidor"], local_nasc=row["local_nasc"],
                                data_nasc=row["data_nasc"], indicativo=row["indicativo"],
                                classe=row["classe"], profissao=row["profissao"], endereco=row["endereco"],
                                bairro=row["bairro"], cep=row["cep"], cidade=row["cidade"],
                                estado=row["estado"], telefone=row["telefone"], celular=row["celular"],
                                email=row["email"], data_assoc=row["data_assoc"], fistel=row["fistel"], remido=row["remido"] )
                        for row in cur.fetchall()
                ]
                return jsonify(associate), 200
        

if __name__ == '__main__':
    app.run(debug=True)