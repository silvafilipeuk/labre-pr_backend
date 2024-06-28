from flask import Flask, json
import pytest
from sqlalchemy import JSON
import utils.utils as utils

## Utils functions testing:

def test_getQtyOfAssociates():
    app = Flask(__name__)
    with app.app_context():
        result = utils.getQtyOfAssociates()
        assert result == 219
        assert type(result) is int


def test_getQtyOfQsl():
    app = Flask(__name__)
    with app.app_context():
        result = utils.getQtyOfQsl()
        assert result == 62
        assert type(result) is int


def test_getQtyOfContribs():
    app = Flask(__name__)
    with app.app_context():
        result = utils.getQtyOfContribs()
        assert result == 134
        assert type(result) is int


def test_getQtyOfBadges():
    app = Flask(__name__)
    with app.app_context():
        result = utils.getQtyOfBagdes()
        assert result == 35
        assert type(result) is int


def test_getBirthdaysOfMonth():
    app = Flask(__name__)
    with app.app_context():
        result = utils.getBirthdaysOfMonth()
        assert type(result) is list
        assert type(result[0]) is dict
        assert type(result[0]["indicativo"]) is str
        assert type(result[len(result)-1]["quantity"]) is int


def test_getAssociateId():
    app = Flask(__name__)
    with app.app_context():
        result = utils.getAssociateId("PY5MW")
        assert type(result) is int
        assert result == 8


def test_getAnnuityDue():
    app = Flask(__name__)
    with app.app_context():
        result = utils.getAnnuityDue(8)
        assert type(result) is str
        assert result == "2018-12-15"

def test_getPaymentHistory():
    app = Flask(__name__)
    with app.app_context():
        result = utils.getPaymentHistory(8)
        assert result.content_type == 'application/json'
        data = json.loads(result.get_data(as_text=True))
        assert len(data) == 5

        for row in data:
            assert row["indicativo"] == 'PY5MW'
            assert row["nome"] == "FILIPE LEANDRO PEREIRA DA SILVA"
            assert type(row["data"]) == str
            assert type(row["descricao"]) == str
            assert type(row["valor"]) == str

def test_checkAdminToken():
    app = Flask(__name__)
    with app.app_context():
       result = utils.checkAdminToken("Rh9wJx7mlgbF6jex6RB3ewmoBI1gPmDudyFJdLZMWSihqOYq4y6qzWf9obBBdvxC")
       assert result == 200
       result = utils.checkAdminToken("Rh9wJx7mlgbF6jex6RB3ewmoBI1gPmDDDDDDDLZMWSihqOYq4y6qzWf9obBBdvxC")
       assert result == 403