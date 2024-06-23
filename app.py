from flask import Flask
from blueprints.associates import associates
from blueprints.news import news


app = Flask(__name__)
app.register_blueprint(associates, url_prefix="/associates")
app.register_blueprint(news, url_prefix="/news")


@app.route("/")
def index():
    return "Labre-PR API - Live..."

     
if __name__ == '__main__':
    app.run(debug=True)