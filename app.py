from flask import Flask
from blueprints.associates import associates


app = Flask(__name__)
app.register_blueprint(associates, url_prefix="/associates")


@app.route("/")
def index():
    return "Labre-PR API - Live..."

     
if __name__ == '__main__':
    app.run(debug=True)