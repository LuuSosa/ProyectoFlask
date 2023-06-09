from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config.from_object('configuration.DevelopmentConfig')
db = SQLAlchemy(app)

from tiendita.modulos.home.views import bp_home
from tiendita.modulos.empleados.views import bp_empleados
from tiendita.modulos.puestos.views import bp_puestos

app.register_blueprint(bp_home)
app.register_blueprint(bp_empleados)
app.register_blueprint(bp_puestos)

with app.app_context():
    db.create_all()