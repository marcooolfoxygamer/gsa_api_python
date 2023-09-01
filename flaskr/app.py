from flaskr import create_app
from flask_restful import Api
from .modelos import db
from .vistas import VistaAntecedentes, VistaUsuarios, VistaUsuario, VistaAnuncios, VistaAnuncio, VistaAsistencias, VistaAsistencia, VistaMusculos, VistaMusculo,VistaPlanificador, VistaEjercicios, VistaEjercicio, VistaMusculosEjercicios
from flask_migrate import Migrate

app = create_app("default")
db.init_app(app)

migrate = Migrate()
migrate.init_app(app, db, compare_type=True)


api = Api(app)
api.add_resource(VistaAntecedentes,'/antecedentes')
api.add_resource(VistaUsuarios,'/usuarios')
api.add_resource(VistaUsuario,'/usuarios/<int:id_user>')
api.add_resource(VistaAnuncios,'/anuncios')
api.add_resource(VistaAnuncio,'/anuncios/<int:id_anunc>')
api.add_resource(VistaAsistencias,'/asistencias')
api.add_resource(VistaAsistencia,'/asistencias/<int:id_registro_asis>')
api.add_resource(VistaMusculos,'/musculos')
api.add_resource(VistaMusculo,'/musculo/<string:musculo>')
api.add_resource(VistaPlanificador,'/planificador')
api.add_resource(VistaEjercicios,'/ejercicios')
api.add_resource(VistaEjercicio,'/ejercicios/<string:ejercicio>')
api.add_resource(VistaMusculosEjercicios,'/musculos/ejercicios/<string:musculos>')


