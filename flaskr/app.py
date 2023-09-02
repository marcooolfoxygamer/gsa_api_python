from flaskr import create_app
from flask_restful import Api
from .modelos import db, Tipos_usuarios, Anteced_salud, Anteced_saludSchema, Usuarios, UsuariosSchema, Anuncios, AnunciosSchema, Asistencia, AsistenciaSchema, Musculos, MusculosSchema, Planificador, PlanificadorSchema, Ejercicios, EjerciciosSchema
from .vistas import VistaAntecedentes, VistaUsuarios, VistaUsuario, VistaAnuncios, VistaAnuncio, VistaAsistencias, VistaAsistencia, VistaMusculos, VistaMusculo,VistaPlanificador, VistaEjercicios, VistaEjercicio, VistaMusculosEjercicios
from flask_migrate import Migrate

app = create_app("default")
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

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

# Codigo prueba de inserción de datos directamente en la base de datos
"""
with app.app_context():

    # Antecedentes
    anteced_salud_Schema = Anteced_saludSchema()
    anteced_1 = Anteced_salud(antecedente='Asma')
    db.session.add(anteced_1)
    anteced_2 = Anteced_salud(antecedente='Artritis')
    db.session.add(anteced_2)
    anteced_3 = Anteced_salud(antecedente='Diabetes')
    db.session.add(anteced_3)
    anteced_4 = Anteced_salud(antecedente='Enfermedad cardiovascular')
    db.session.add(anteced_4)
    anteced_5 = Anteced_salud(antecedente='Enfermedad pulmonar')
    db.session.add(anteced_5)
    anteced_6 = Anteced_salud(antecedente='Enfermedad cronica')
    db.session.add(anteced_6)
    anteced_7 = Anteced_salud(antecedente='Ninguna')
    db.session.add(anteced_7)

    # Usuarios
    usuarios_Schema = UsuariosSchema()
    u1 = Usuarios(id_user=1, fk_tipo_user=Tipos_usuarios.Administrador, nom1_user='Juan', nom2_user=None, ape1_user='Carrillo', ape2_user=None, correo_sena_user='j@soy.sena.edu.co', contrasena='123', fk_anteced_salud_sel=anteced_7.antecedente, anteced_salud_inp=None, estado_user=1)
    db.session.add(u1)
    u2 = Usuarios(id_user=2, fk_tipo_user=Tipos_usuarios.Aprendiz, nom1_user='Lucas', nom2_user='Roberto', ape1_user='Lopez', ape2_user=None, correo_sena_user='l@soy.sena.edu.co', contrasena='123',fk_anteced_salud_sel=anteced_6.antecedente, anteced_salud_inp='No', estado_user=1)
    db.session.add(u2)
    u3 = Usuarios(id_user=3, fk_tipo_user=Tipos_usuarios.Instructor, nom1_user='Pedro', nom2_user=None, ape1_user='Isis', ape2_user=None, correo_sena_user='p@soy.sena.edu.co', contrasena='123',fk_anteced_salud_sel=anteced_7.antecedente, anteced_salud_inp='Ninguna', estado_user=1)
    db.session.add(u3)
    
    
    # Anuncios
    anuncios_Schema = AnunciosSchema()
    anunc1 = Anuncios(fk_id_admin_anunc=u1.id_user, titulo_anunc='Ten en cuenta', desc_anunc='Por situaciones adversas, el gimnasio no estará disponible en las mañanas hasta nuevo aviso. Pedimos excusas por esta situación. Gracias.', img_anunc='cinco.jpg', estado_anunc=1)
    db.session.add(anunc1)
    anunc2 = Anuncios(fk_id_admin_anunc=u1.id_user, titulo_anunc='Recuerda...', desc_anunc='Estamos disponibles de 6am a 8pm (sugeto a cambios).', img_anunc='principal.jpg', estado_anunc=1)
    db.session.add(anunc2)
    anunc3 = Anuncios(fk_id_admin_anunc=u1.id_user, titulo_anunc='Si', desc_anunc='Estamos disponibles de 6am a 8pm (sugeto a cambios).', img_anunc='cuatro.jpg', estado_anunc=1)
    db.session.add(anunc3)

    # Asistencia
    asistencia_Schema = AsistenciaSchema()
    asist = Asistencia(id_instruc_asis=3,fk_id_aprend_asis=u2.id_user,fecha_asis='2023-09-10',estado_asis=1)
    db.session.add(asist)

    # Musculos
    musculos_Schema = MusculosSchema()
    musc1 = Musculos(musculo='Cuadriceps')
    #db.session.add(musc1)
    musc2 = Musculos(musculo='Triceps')
    #db.session.add(musc2)
    musc3 = Musculos(musculo='Biceps')
    #db.session.add(musc3)
    musc4 = Musculos(musculo='Isquiotibiales')
    #db.session.add(musc4)
    musc5 = Musculos(musculo='Espalda')
    #db.session.add(musc5)

    # Planificador
    planificador_Schema = PlanificadorSchema()
    planif = Planificador(fk_id_aprend=u2.id_user,fk_musculo=musc4.musculo)
    db.session.add(planif)

    # Ejercicios
    ejercicios_Schema = EjerciciosSchema()
    ejerc1 = Ejercicios(ejercicio='Leg-press',imagen_ejerc='ej01.png')
    #db.session.add(ejerc1)
    ejerc2 = Ejercicios(ejercicio='Extension de pierna', imagen_ejerc='ej02.png')
    #db.session.add(ejerc2)
    ejerc3 = Ejercicios(ejercicio='Copa triceps', imagen_ejerc='ej03.png')
    #db.session.add(ejerc3)
    ejerc4 = Ejercicios(ejercicio='Rompecraneos', imagen_ejerc='ej04.png')
    #db.session.add(ejerc4)
    ejerc5 = Ejercicios(ejercicio='Curl con mancuernas', imagen_ejerc='ej05.png')
    #db.session.add(ejerc5)
    ejerc6 = Ejercicios(ejercicio='Dominadas', imagen_ejerc='ej06.png')
    #db.session.add(ejerc6)
    ejerc7 = Ejercicios(ejercicio='Puente isometrico', imagen_ejerc='ej07.png')
    #db.session.add(ejerc7)
    ejerc8 = Ejercicios(ejercicio='Curl nordico', imagen_ejerc='ej08.png')
    #db.session.add(ejerc8)
    ejerc9 = Ejercicios(ejercicio='Jalon al pecho', imagen_ejerc='ej09.png')
    #db.session.add(ejerc9)
    ejerc10 = Ejercicios(ejercicio='Remo brazo', imagen_ejerc='ej10.png')
    #db.session.add(ejerc10)

    # Musculos_Ejercicios
    musc1.ejercicios.append(ejerc1)
    musc1.ejercicios.append(ejerc2)
    db.session.add(musc1)

    musc2.ejercicios.append(ejerc3)
    musc2.ejercicios.append(ejerc4)
    db.session.add(musc2)

    musc3.ejercicios.append(ejerc5)
    musc3.ejercicios.append(ejerc6)
    db.session.add(musc3)

    musc4.ejercicios.append(ejerc7)
    musc4.ejercicios.append(ejerc8)
    db.session.add(musc4)

    musc5.ejercicios.append(ejerc9)
    musc5.ejercicios.append(ejerc10)
    db.session.add(musc5)

    db.session.commit()
"""