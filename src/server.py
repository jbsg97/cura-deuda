from flask import Flask
from flask_restful import Api
#from flask_jwt_extended import JWTManager
from src.app.routes import blueprint_urls
from src.config.db import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mssql+pyodbc://sa:Jja1793*@localhost/sepomex?driver=ODBC+Driver+17+for+SQL+Server"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#app.config.from_json(os.path.abspath(os.path.join('settings.json')))
api = Api(app)
app.register_blueprint(blueprint_urls)

@app.route("/")
def index():
    return "<h1>Welcome to Cura Deuda API</h1>"

db.init_app(app)
#sentry.init_app(app)
#init_celery(app, celery_instance)

#jwt = JWTManager(app)