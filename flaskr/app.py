from flaskr import create_app
from flask_restful import Api
from .modelos import db
from flask_migrate import Migrate


app = create_app("default")
db.init_app(app)

#db = SQLAlchemy(app)
migrate = Migrate()
migrate.init_app(app, db, compare_type=True)


#app_context = app.app_context()
#app_context.push()

#db.init_app(app)
#db.create_all()

"""
api = Api(app)
api.add_resource(VistaCanciones,'/canciones')
api.add_resource(VistaCancion,'/canciones/<int:id_cancion>')
api.add_resource(VistaAlbumes,'/albums')
api.add_resource(VistaAlbum,'/albums/<int:id_album>')
api.add_resource(VistaUsuarios,'/usuarios')
api.add_resource(VistaUsuario,'/usuarios/<int:id_usuario>')
api.add_resource(VistaAlbumesCanciones,'/canciones/albums/<int:albumes>')
#api.add_resource(VistaAnuncio,'/anuncios/<int:id_anunc>')
#api.add_resource(VistaAlbumesCanciones,'/canciones/albums/<int:albumes>')
"""

# Codigo prueba de que inserta y consulta datos correctamente (así como se pueden hacer más operaciones y funciona bien)
"""
with app.app_context():
    # Usuario
    Usuario_Schema = UsuarioSchema()
    U = Usuario(nombre_usuario='Juan', contrasena='12345')

    # Album
    Album_Schema = AlbumSchema()
    A = Album(titulo='prueba', anio=1999, descripcion='texto', medio=Medio.CD, usuario=1)

    # Cancion
    Cancion_Schema = CancionSchema()
    C = Cancion(titulo='mi cancion', minutos=1, segundos=15, interprete="Juanito")
    C2 = Cancion(titulo='mi cancion 2', minutos=2, segundos=15, interprete="Carlos")

    U.albumes.append(A)
    A.canciones.append(C)

    A.canciones.append(C2)

    db.session.add(U)
    db.session.add(C)
    db.session.add(C2)

    #A_C = albumes_canciones(album_id=1,cancion_id=1)
    #db.session.add(A_C)

    db.session.commit()

    print([Album_Schema.dumps(album) for album in Album.query.all()])
    print([Cancion_Schema.dumps(cancion) for cancion in Cancion.query.all()])
    print([Usuario_Schema.dumps(usuario) for usuario in Usuario.query.all()])
"""