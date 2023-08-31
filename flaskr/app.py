from flaskr import create_app
#from .modelos import db, Cancion, Album, Usuario, Medio, albumes_canciones
#from .modelos import AlbumSchema, CancionSchema, UsuarioSchema
from flask_restful import Api
#from .vistas import VistaCanciones, VistaCancion, VistaAlbumes, VistaAlbum, VistaUsuarios, VistaUsuario, VistaAlbumesCanciones
from flask import Flask, render_template, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
import enum

app = create_app("default")

db = SQLAlchemy(app)
migrate = Migrate()
migrate.init_app(app, db, compare_type=True)

class Tipos_usuarios(enum.Enum):
    Administrador = 1
    Aprendiz = 2
    Instructor = 3

class Anteced_salud(db.Model):
    # __tablename__ = 'anteced_salud'
    antecedente = db.Column(db.String(80), primary_key=True)
    usuarios = db.relationship('Usuarios', cascade='all, delete, delete-orphan')

    def __init__(self, antecedente):
        self.antecedente = antecedente

    def json(self):
        return {'antecedente': self.antecedente}

    def __str__(self):
        return str(self.__class__) + ":" + str(self.__dict__)


class Usuarios(db.Model):
    #__tablename__ = 'usuarios'
    id_user = db.Column(db.BigInteger, primary_key=True)
    fk_tipo_user = db.Column(db.Enum(Tipos_usuarios))
    nom1_user = db.Column(db.String(30), nullable=False)
    nom2_user = db.Column(db.String(30), nullable=True)
    ape1_user = db.Column(db.String(30), nullable=False)
    ape2_user = db.Column(db.String(30), nullable=True)
    correo_sena_user = db.Column(db.String(80), nullable=False)
    contrasena = db.Column(db.String(80), nullable=False)
    fk_anteced_salud_sel = db.Column(db.String(80), db.ForeignKey("anteced_salud.antecedente"))
    anteced_salud_inp = db.Column(db.String(255), nullable=True)
    estado_user = db.Column(db.Boolean, nullable=True)
    anuncios = db.relationship('Anuncios', cascade='all, delete, delete-orphan')
    asistencia = db.relationship('Asistencia', cascade='all, delete, delete-orphan')
    planificador = db.relationship('Planificador', cascade='all, delete, delete-orphan')

    def __init__(self,id_user,fk_tipo_user,nom1_user,nom2_user,ape1_user,ape2_user,correo_sena_user,contrasena,fk_anteced_salud_sel,anteced_salud_inp,estado_user):
        self.id_user = id_user
        self.fk_tipo_user = fk_tipo_user
        self.nom1_user = nom1_user
        self.nom2_user = nom2_user
        self.ape1_user = ape1_user
        self.ape2_user = ape2_user
        self.correo_sena_user = correo_sena_user
        self.contrasena = contrasena
        self.fk_anteced_salud_sel = fk_anteced_salud_sel
        self.anteced_salud_inp = anteced_salud_inp
        self.estado_user = estado_user

    def json(self):
        return{'id_user':self.id_user,'fk_tipo_user':self.fk_tipo_user,'nom1_user':self.nom1_user,'nom2_user':self.nom2_user,'ape1_user':self.ape1_user,'ape2_user':self.ape2_user,'correo_sena_user':self.correo_sena_user,'contrasena':self.contrasena,'fk_anteced_salud_sel':self.fk_anteced_salud_sel,'anteced_salud_inp':self.anteced_salud_inp,'estado_user':self.estado_user}

    def __str__(self):
        return str(self.__class__)+":"+str(self.__dict__)

class Anuncios(db.Model):
    #__tablename__ = 'anuncios'
    id_anunc = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fk_id_admin_anunc = db.Column(db.BigInteger, db.ForeignKey("usuarios.id_user"))
    titulo_anunc = db.Column(db.String(60), nullable=False)
    desc_anunc = db.Column(db.String(255), nullable=False)
    img_anunc = db.Column(db.String(255), nullable=False)
    estado_anunc = db.Column(db.Boolean, nullable=True)

    def __init__(self,fk_id_admin_anunc,titulo_anunc,desc_anunc,img_anunc,estado_anunc):
        self.fk_id_admin_anunc = fk_id_admin_anunc
        self.titulo_anunc = titulo_anunc
        self.desc_anunc = desc_anunc
        self.img_anunc = img_anunc
        self.estado_anunc = estado_anunc

    def json(self):
        return {'id_anunc':self.id_anunc,'fk_id_admin_anunc':self.fk_id_admin_anunc,'titulo_anunc':self.titulo_anunc,'desc_anunc':self.desc_anunc,'img_anunc':self.img_anunc,'estado_anunc':self.estado_anunc}

    def __str__(self):
        return str(self.__class__) + ":" + str(self.__dict__)

class Asistencia(db.Model):
    # __tablename__ = 'asistencia'
    id_registro_asis = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_instruc_asis = db.Column(db.BigInteger, nullable=False)
    fk_id_aprend_asis = db.Column(db.BigInteger, db.ForeignKey("usuarios.id_user"))
    fecha_asis = db.Column(db.Date, nullable=False)
    estado_asis = db.Column(db.Boolean, nullable=True)

    def __init__(self,id_instruc_asis,fk_id_aprend_asis,fecha_asis,estado_asis):
        self.id_instruc_asis = id_instruc_asis
        self.fk_id_aprend_asis = fk_id_aprend_asis
        self.fecha_asis = fecha_asis
        self.estado_asis = estado_asis

    def json(self):
        return {'id_registro_asis':self.id_registro_asis,'id_instruc_asis':self.id_instruc_asis,'fk_id_aprend_asis':self.fk_id_aprend_asis,'fecha_asis':self.fecha_asis,'estado_asis': self.estado_asis}

    def __str__(self):
        return str(self.__class__) + ":" + str(self.__dict__)

class Musculos(db.Model):
    #__tablename__ = 'musculos'
    musculo = db.Column(db.String(30), primary_key=True)
    ejercicios = db.relationship('Ejercicios', secondary='musculo_ejercicio', back_populates='musculos')
    planificador = db.relationship('Planificador', cascade='all, delete, delete-orphan')

    def __init__(self,musculo):
        self.musculo = musculo

    def json(self):
        return {'musculo':self.musculo}

    def __str__(self):
        return str(self.__class__) + ":" + str(self.__dict__)

class Planificador(db.Model):
    #__tablename__ = 'planificador'
    id_reg_planif = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fk_id_aprend = db.Column(db.BigInteger, db.ForeignKey("usuarios.id_user"))
    fk_musculo = db.Column(db.String(30), db.ForeignKey("musculos.musculo"))

    def __init__(self,fk_id_aprend,fk_musculo):
        self.fk_id_aprend = fk_id_aprend
        self.fk_musculo = fk_musculo

    def json(self):
        return {'id_reg_planif':self.id_reg_planif,'fk_id_aprend':self.fk_id_aprend,'fk_musculo':self.fk_musculo}

    def __str__(self):
        return str(self.__class__) + ":" + str(self.__dict__)

class Ejercicios(db.Model):
    #__tablename__ = 'ejercicios'
    ejercicio = db.Column(db.String(30), primary_key=True)
    imagen_ejerc = db.Column(db.String(255), nullable=False)
    musculos = db.relationship('Musculos', secondary='musculo_ejercicio', back_populates='ejercicios')

    def __init__(self,ejercicio,imagen_ejerc):
        self.ejercicio = ejercicio
        self.imagen_ejerc = imagen_ejerc

    def json(self):
        return {'ejercicio':self.ejercicio,'imagen_ejerc':self.imagen_ejerc}

    def __str__(self):
        return str(self.__class__) + ":" + str(self.__dict__)


musculos_ejercicios = db.Table('musculo_ejercicio', \
    db.Column('pkfk_musculo', db.String(30), db.ForeignKey('musculos.musculo'), primary_key=True),\
    db.Column('pkfk_ejercicio', db.String(30), db.ForeignKey('ejercicios.ejercicio'), primary_key=True))

class EnumADiccionario(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return None
        return {'llave':value.name, 'valor':value.value}


## SCHEMA

class Anteced_saludSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Anteced_salud
        include_relationships = True
        load_instance = True

class UsuariosSchema(SQLAlchemyAutoSchema):
    fk_tipo_user = EnumADiccionario(attribute=('fk_tipo_user'))
    class Meta:
        model = Usuarios
        include_relationships = True
        load_instance = True

class AnunciosSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Anuncios
        include_relationships = True
        load_instance = True

class AsistenciaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Asistencia
        include_relationships = True
        load_instance = True

class MusculosSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Musculos
        include_relationships = True
        load_instance = True

class PlanificadorSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Planificador
        include_relationships = True
        load_instance = True

class EjerciciosSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Ejercicios
        include_relationships = True
        load_instance = True






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