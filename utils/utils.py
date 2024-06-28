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
            qtyOfAssociates = connection.execute(text("SELECT COUNT(*) AS qty FROM associados"))

            for row in qtyOfAssociates:
                return int(row.qty)
    except:
        error = [{"error": "Could not get the quantity of associates, please try again..."}]

        return jsonify(error)  
    
    
# Get the total of QSL cards in the bureau
def getQtyOfQsl():
    try:
        with engine.connect() as connection:
            qtyOfQsl = connection.execute(text("SELECT SUM(qtde) AS qty FROM bureau"))

            for row in qtyOfQsl:
                return int(row.qty)
    except:
        error = [{"error": "Could not get the quantity of Qsl's, please try again..."}]
        return jsonify(error)  
    

# Get the total of contributions
def getQtyOfContribs():
    try:
        with engine.connect() as connection:
            qtyOfContribs = connection.execute(text("SELECT COUNT(*) AS qty FROM contribuicoes where pago <> 1"))

            for row in qtyOfContribs:
                return int(row.qty)
    except:
        error = [{"error": "Could not get the quantity of contributions, please try again..."}]
        return jsonify(error) 
    

# Get the total of pending badges requests
def getQtyOfBagdes():
    try:
        with engine.connect() as connection:
            qtyOfBadges = connection.execute(text("SELECT COUNT(*) AS qty FROM cracha"))

            for row in qtyOfBadges:
                return int(row.qty)
    except:
        error = [{"error": "Could not get the quantity of pending badges, please try again..."}]
        return jsonify(error) 


# Get the Birthdays of the Month
def getBirthdaysOfMonth():
    try:
        with engine.connect() as connection:
            monthBirthdays = connection.execute(text("SELECT indicativo FROM associados WHERE MONTH(data_nasc) = MONTH(CURRENT_DATE())"))

            response = [
                dict(indicativo=row["indicativo"])
                    for row in monthBirthdays.mappings()
                ]
            response.append({"quantity": len(response)})
            return response
    except:
        error = [{"error": "Could not get the birthdays of the month, please try again..."}]
        return jsonify(error)
    

# Get associate ID number
def getAssociateId(callsign):
    try:
        with engine.connect() as connection:
            associateId = connection.execute(text("SELECT id from associados where indicativo = :indicativo"), dict(indicativo=callsign))

            for row in associateId:
                return int(row.id)
    except:
        error = [{"error": "Could net get the associate ID, please try again..."}]
        return jsonify(error)
    

# Get next date the annuity is due
def getAnnuityDue(id):
    try:
        with engine.connect() as connection:
            nextAnnuityDate = connection.execute(text("SELECT DATE_ADD(max(data), INTERVAL 365 DAY) AS next_annuity FROM pagamentos WHERE id_socio = :idnum"), dict(idnum=id))

            for row in nextAnnuityDate:
                return str(row.next_annuity)
    except:
        error = [{"error": "Could net get the next date of the annuity, please try again..."}]
        return jsonify(error)
    
    
def getPaymentHistory(id):
    try:
        with engine.connect() as connection:
            paymentHistory = connection.execute(text("SELECT a.nome, a.indicativo, b.data, b.descricao, b.valor FROM associados a INNER JOIN pagamentos b ON a.id = b.id_socio WHERE a.id = :idnum ORDER BY b.data DESC"), dict(idnum=id))

            response = [
                        dict(nome=row["nome"], indicativo=row["indicativo"], data=row["data"], descricao=row["descricao"], valor=row["valor"])
                        for row in paymentHistory.mappings()
                    ]
            
            return jsonify(response)
    except:
        error = [{"error": "Could not get the payment history for this user, please try again..."}]
        return jsonify(error)
    

def checkAdminToken(token):
    try:
        with engine.connect() as connection:
            adminUser = connection.execute(text("SELECT admin_token FROM admin_token WHERE admin_token = :admin_token"), dict(admin_token=token))

            if adminUser.rowcount > 0:
                return 200
            else:
                return 403
    except:
        error = [{"error": "Could net verify authorization for the given token, please try again..."}]
        return jsonify(error)