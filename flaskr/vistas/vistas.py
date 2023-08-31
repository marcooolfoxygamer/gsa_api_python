from flask_restful import Resource
#from ..modelos import db, Cancion, CancionSchema, Album, AlbumSchema, Usuario, UsuarioSchema
from flask import request

# Instancia schema
anteced_salud_schema = Anteced_saludSchema()
usuarios_schema = UsuariosSchema()
anuncios_schema = AnunciosSchema()
asistencia_schema = AsistenciaSchema()
musculos_schema = MusculosSchema()
planificador_schema = PlanificadorSchema()
ejercicios_schema = EjerciciosSchema()


# Creacion vista antecedentes
class VistaAntecedentes(Resource):
    def get(self):
        return [anteced_salud_schema.dump()]


# Creacion vista canciones
class VistaCanciones(Resource):
    def get(self): #trae todas las canciones
        return [cancion_schema.dump(Cancion) for Cancion in Cancion.query.all()]

    def post(self):
        nueva_cancion = Cancion(titulo=request.json['titulo'],\
                                minutos=request.json['minutos'],\
                                segundos=request.json['segundos'],\
                                interprete=request.json['interprete'])
        db.session.add(nueva_cancion) #Agrega en la bd
        db.session.commit() #Guarda los cambios
        return cancion_schema.dump(nueva_cancion) #retorna la nueva cancion en formato json


class VistaCancion(Resource):
    def get(self, id_cancion):  # trae una sola cancion
        return cancion_schema.dump(Cancion.query.get_or_404(id_cancion))

    #actualizar

    def put(self, id_cancion):
        cancion = Cancion.query.get_or_404(id_cancion)
        cancion.titulo = request.json.get('titulo', cancion.titulo)
        cancion.minutos = request.json.get('minutos', cancion.minutos)
        cancion.segundos = request.json.get('segundos', cancion.segundos)
        cancion.interprete = request.json.get('interprete', cancion.interprete)
        db.session.commit()
        return cancion_schema.dump(cancion)

    # eliminar
    def delete(self, id_cancion):
        cancion = Cancion.query.get_or_404(id_cancion)
        db.session.delete(cancion)
        db.session.commit()
        return 'Operacion existosa', 204

## Album

class VistaAlbumes(Resource):
    def get(self): #trae todos los albums
        return [album_schema.dump(Album) for Album in Album.query.all()]

    def post(self):
        nuevo_album = Album(titulo=request.json['titulo'],\
                            anio=request.json['anio'],\
                            descripcion=request.json['descripcion'], \
                            medio=request.json['medio'], \
                            usuario=request.json['usuario'])
        db.session.add(nuevo_album) #Agrega en la bd
        db.session.commit() #Guarda los cambios
        return album_schema.dump(nuevo_album) #retorna el nuevo album en formato json

class VistaAlbum(Resource):
    def get(self, id_album):  # trae un solo album
        return album_schema.dump(Album.query.get_or_404(id_album))

    #actualizar

    def put(self, id_album):
        album = Album.query.get_or_404(id_album)
        album.titulo = request.json.get('titulo', album.titulo)
        album.anio = request.json.get('anio', album.anio)
        album.descripcion = request.json.get('descripcion', album.descripcion)
        album.medio = request.json.get('medio', album.medio)
        album.usuario = request.json.get('usuario', album.usuario)
        db.session.commit()
        return album_schema.dump(album)

    # eliminar
    def delete(self, id_album):
        album = Album.query.get_or_404(id_album)
        db.session.delete(album)
        db.session.commit()
        return 'Operacion existosa', 204

## Usuario

class VistaUsuarios(Resource):
    def get(self): #trae todos los usuarios
        return [usuario_schema.dump(Usuario) for Usuario in Usuario.query.all()]

    def post(self):
        nuevo_usuario = Usuario(nombre_usuario=request.json['nombre_usuario'],\
                                contrasena=request.json['contrasena'])
        db.session.add(nuevo_usuario) #Agrega en la bd
        db.session.commit() #Guarda los cambios
        return usuario_schema.dump(nuevo_usuario) #retorna el nuevo usuario en formato json

class VistaUsuario(Resource):
    def get(self, id_usuario):  # trae un solo usuario
        return usuario_schema.dump(Usuario.query.get_or_404(id_usuario))

    #actualizar

    def put(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        usuario.nombre_usuario = request.json.get('nombre_usuario', usuario.nombre_usuario)
        usuario.contrasena = request.json.get('contrasena', usuario.contrasena)
        db.session.commit()
        return usuario_schema.dump(usuario)

    # eliminar
    def delete(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        db.session.delete(usuario)
        db.session.commit()
        return 'Operacion existosa', 204


## Clase con ruta adicional, creada con el propósito de listar las canciones que le correspondan al album pasado por parámetro
class VistaAlbumesCanciones(Resource):
    def get(self,albumes):
        alb = Album.query.get(albumes)
        canciones = alb.canciones

        lista = [ c.titulo for c in canciones ]
        return {'canciones del album':lista}