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