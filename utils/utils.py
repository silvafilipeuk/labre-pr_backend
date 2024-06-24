from flask import jsonify
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from pathlib import Path

import os

dotenv_path = Path('./database.env')
load_dotenv(dotenv_path=dotenv_path)


connection_string = "mysql+mysqlconnector://{0}:{1}@{2}:3306/{3}".format(os.getenv("MYSQL_USER"), os.getenv("MYSQL_PASSWORD"), os.getenv("MYSQL_HOST"), os.getenv("MYSQL_DB")) 
engine = create_engine(connection_string, echo=True)

# Get Quantity of associates
def getQtyOfAssociates():
    try:
        with engine.connect() as connection:
            qtyOfAssociates = connection.execute(text("SELECT COUNT(*) as qty FROM associados"))

            for row in qtyOfAssociates:
                return int(row.qty)
    except:
        error = [{"error": "Could not get the quantity of associates, please try again..."}]

        return jsonify(error)  
    
    
# Get the total of QSL cards in the bureau
def getQtyOfQsl():
    try:
        with engine.connect() as connection:
            qtyOfQsl = connection.execute(text("SELECT SUM(qtde) as qty FROM bureau"))

            for row in qtyOfQsl:
                return int(row.qty)
    except:
        error = [{"error": "Could not get the quantity of Qsl's, please try again..."}]
        return jsonify(error)  
    

# Get the total of contributions
def getQtyOfContribs():
    try:
        with engine.connect() as connection:
            qtyOfContribs = connection.execute(text("SELECT COUNT(*) as qty FROM contribuicoes where pago <> 1"))

            for row in qtyOfContribs:
                return int(row.qty)
    except:
        error = [{"error": "Could not get the quantity of contributions, please try again..."}]
        return jsonify(error) 
    

# Get the total of pending badges requests
def getQtyOfBagdes():
    try:
        with engine.connect() as connection:
            qtyOfBadges = connection.execute(text("SELECT COUNT(*) as qty FROM cracha"))

            for row in qtyOfBadges:
                return int(row.qty)
    except:
        error = [{"error": "Could not get the quantity of pending badges, please try again..."}]
        return jsonify(error) 
