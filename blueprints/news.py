from flask import Blueprint, jsonify, request
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from pathlib import Path
import os

dotenv_path = Path('./database.env')
load_dotenv(dotenv_path=dotenv_path)


connection_string = "mysql+mysqlconnector://{0}:{1}@{2}:3306/{3}".format(os.getenv("MYSQL_USER"), os.getenv("MYSQL_PASSWORD"), os.getenv("MYSQL_HOST"), os.getenv("MYSQL_DB")) 
engine = create_engine(connection_string, echo=True)

news = Blueprint("news", __name__)


#Route to retrieve all news
# Available queries:
# id, titulo
@news.route("/", methods=['GET', 'PATCH', 'DELETE'])
def handle_news():
        if request.method == 'GET':
                try:
                        with engine.connect() as connection:
                                id = request.args.get("id")
                                titulo = request.args.get("titulo")

                                if(id):
                                    news = connection.execute(text("SELECT * FROM noticias where id = :idnum"), dict(idnum=id))
                                elif(titulo):
                                    news = connection.execute(text("SELECT * FROM noticias where titulo = :title"), dict(title=titulo))
                                else:
                                    news = connection.execute(text("SELECT * FROM noticias order by data desc"))

                                response = [
                                        dict(id=row["id"], data=row["data"], titulo=row["titulo"],
                                                noticia=row["noticia"])
                                        for row in news.mappings()
                                ]
                                response.append({"quantity": len(response)})
                                return jsonify(response), 200
                except:
                        error = [{"error": "Something went wrong, please try again..."}]
                        return jsonify(error), 500            
                
        
