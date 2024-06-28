from flask import Blueprint, jsonify, request
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from pathlib import Path
from utils.utils import checkAdminToken
import os

dotenv_path = Path('./database.env')
load_dotenv(dotenv_path=dotenv_path)


connection_string = "mysql+mysqlconnector://{0}:{1}@{2}:3306/{3}".format(os.getenv("MYSQL_USER"), os.getenv("MYSQL_PASSWORD"), os.getenv("MYSQL_HOST"), os.getenv("MYSQL_DB")) 
engine = create_engine(connection_string, echo=True)

associates = Blueprint("associates", __name__)


#Route to retrieve all associates
@associates.route("/", methods=['GET', 'PATCH', 'DELETE'])
def handle_associates():
        if request.method == 'GET':
                try:
                        admin_token = request.args.get("auth_token")
                        auth = checkAdminToken(admin_token)

                        if(auth == 200):
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
                                        response.append({"quantity": len(response)})
                                        return jsonify(response), 200
                        if(auth == 403):
                                return "Not Authorized.", 403
                except:
                        error = [{"error": "Something went wrong, please try again..."}]
                        return jsonify(error), 500


                
                
        
# Route to retrieve, or update associate by callsign
@associates.route("/<string:callsign>", methods=['GET', 'PATCH'])
def handle_associate_by_callsign(callsign):
        if request.method == 'GET':
                try:
                        admin_token = request.args.get("auth_token")
                        auth = checkAdminToken(admin_token)

                        if(auth == 200):
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
                                        response.append({"quantity": len(response)})
                                        return jsonify(response), 200
                        if(auth == 403):
                                return "Not Authorized.", 403
                except:
                        error = [{"error": "Something went wrong, please try again..."}]
                        return jsonify(error), 500