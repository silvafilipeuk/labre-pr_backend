from flask import Blueprint, jsonify, request
from sqlalchemy import create_engine, text

from dotenv import load_dotenv
from pathlib import Path
import os

dotenv_path = Path('./database.env')
load_dotenv(dotenv_path=dotenv_path)


connection_string = "mysql+mysqlconnector://{0}:{1}@{2}:3306/{3}".format(os.getenv("MYSQL_USER"), os.getenv("MYSQL_PASSWORD"), os.getenv("MYSQL_HOST"), os.getenv("MYSQL_DB")) 
engine = create_engine(connection_string, echo=True)

associates = Blueprint("associates", __name__)

@associates.route("/")
def get_associates():
        if request.method == 'GET':
                with engine.connect() as connection:
                        associates = connection.execute(text("SELECT * FROM associados"))
                        response = [
                                dict(id=row["id"], nome=row["nome"], cpf=row["cpf"],
                                        rg=row["rg"], expedidor=row["expedidor"], local_nasc=row["local_nasc"],
                                        data_nasc=row["data_nasc"], indicativo=row["indicativo"],
                                        classe=row["classe"], profissao=row["profissao"], endereco=row["endereco"],
                                        bairro=row["bairro"], cep=row["cep"], cidade=row["cidade"],
                                        estado=row["estado"], telefone=row["telefone"], celular=row["celular"],
                                        email=row["email"], data_assoc=row["data_assoc"], fistel=row["fistel"], remido=row["remido"] )
                                for row in associates.mappings()
                        ]
                        return jsonify(response), 200
        
# Route to retrieve, or update associate by callsign
@associates.route("/<string:callsign>", methods=['GET', 'PATCH'])
def get_associate_by_callsign(callsign):
        if request.method == 'GET':
                with engine.connect() as connection:
                        associate = connection.execute(text("SELECT * FROM associados WHERE indicativo = :indicativo"), dict(indicativo=callsign))
                        response = [
                                dict(id=row["id"], nome=row["nome"], cpf=row["cpf"],
                                        rg=row["rg"], expedidor=row["expedidor"], local_nasc=row["local_nasc"],
                                        data_nasc=row["data_nasc"], indicativo=row["indicativo"],
                                        classe=row["classe"], profissao=row["profissao"], endereco=row["endereco"],
                                        bairro=row["bairro"], cep=row["cep"], cidade=row["cidade"],
                                        estado=row["estado"], telefone=row["telefone"], celular=row["celular"],
                                        email=row["email"], data_assoc=row["data_assoc"], fistel=row["fistel"], remido=row["remido"] )
                                for row in associate.mappings()
                        ]
                return jsonify(response), 200