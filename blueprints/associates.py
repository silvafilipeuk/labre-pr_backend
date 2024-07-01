from shutil import ExecError
from flask import Blueprint, jsonify, request
from sqlalchemy import create_engine, text, update, Table, Column, Integer, String, Date, MetaData
from dotenv import load_dotenv
from pathlib import Path
from utils.utils import checkAdminToken
import os

dotenv_path = Path('./database.env')
load_dotenv(dotenv_path=dotenv_path)

metadata_obj = MetaData();

Associados = Table(
        "associados",
        metadata_obj,
        Column("id", Integer, primary_key=True),
        Column("nome", String(500)),
        Column("cpf", String(20)),
        Column("rg", String(20)),
        Column("expedidor", String(10)),
        Column("local_nasc", String(100)),
        Column("data_nasc", Date), 
        Column("indicativo", String(6)),
        Column("classe", String(1)),
        Column("profissao", String(200)),
        Column("endereco", String(500)),
        Column("bairro", String(200)),
        Column("cep", String(10)),
        Column("cidade", String(100)),
        Column("estado", String(100)),
        Column("telefone", String(20)),
        Column("celular", String(20)),
        Column("email", String(100)),
        Column("password", String(50)),
        Column("admin", Integer),
        Column("data_assoc", Date),
        Column("fistel", String(50)),
        Column("liberado", Integer),
        Column("anuncio", Integer),
        Column("remido", Integer),
)


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
                
        elif request.method == 'PATCH':
                try:
                        admin_token = request.args.get("auth_token")
                        auth = checkAdminToken(admin_token)

                        if(auth == 200):
                                with engine.connect() as connection:
                                        updateAssociate = request.json
                                        stmt = (
                                                update(Associados)
                                                .where(Associados.c.id == updateAssociate["id"])
                                                .values(updateAssociate)
                                        )
                                        connection.execute(stmt)
                                        connection.commit()

                                        associates = connection.execute(text("SELECT * FROM associados WHERE id=:idnum"), dict(idnum=updateAssociate["id"]))
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
                except Exception:
                        error = [{"error": Exception}]
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