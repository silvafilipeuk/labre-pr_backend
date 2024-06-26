from flask import Flask
import pytest
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
        