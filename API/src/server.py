from flask import Flask
from flask_restful import Api
from src.app.routes import blueprint_urls
from src.config.db import db
from src.config.auth import authenticate, identity
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mssql+pyodbc://sa:Password123*@sqlserver,1433/sepomex?driver=ODBC+Driver+17+for+SQL+Server"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
api = Api(app)
app.register_blueprint(blueprint_urls)

@app.route("/")
def index():
    return "<h1>Welcome to Cura Deuda API</h1>"

app.config['SECRET_KEY'] = 'super-secret'
jwt = JWTManager(app)
db.init_app(app)
