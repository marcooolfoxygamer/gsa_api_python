from flask_restful import Resource
from ..modelos import db, Anteced_salud, Anteced_saludSchema, Usuarios, UsuariosSchema, Anuncios, AnunciosSchema, Asistencia, AsistenciaSchema, Musculos, MusculosSchema, Planificador, PlanificadorSchema, Ejercicios, EjerciciosSchema
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
        return [anteced_salud_schema.dump(Anteced_salud) for Anteced_salud in Anteced_salud.query.all()]

# Creacion vista usuarios
class VistaUsuarios(Resource):
    def get(self):
        return [usuarios_schema.dump(Usuarios) for Usuarios in Usuarios.query.all()]

    def post(self):
        nuevo_usuario = Usuarios(id_user=request.json['id_user'], \
                                 fk_tipo_user=request.json['fk_tipo_user'], \
                                 nom1_user=request.json['nom1_user'], \
                                 nom2_user=request.json['nom2_user'], \
                                 ape1_user=request.json['ape1_user'], \
                                 ape2_user=request.json['ape2_user'], \
                                 correo_sena_user=request.json['correo_sena_user'], \
                                 contrasena=request.json['contrasena'], \
                                 fk_anteced_salud_sel=request.json['fk_anteced_salud_sel'], \
                                 anteced_salud_inp=request.json['anteced_salud_inp'], \
                                 estado_user=request.json['estado_user'])
        db.session.add(nuevo_usuario)
        db.session.commit()
        return usuarios_schema.dump(nuevo_usuario)

class VistaUsuario(Resource):
    def get(self, id_user):
        return usuarios_schema.dump(Usuarios.query.get_or_404(id_user))

    #actualizar

    def put(self, id_user):
        usuario = Usuarios.query.get_or_404(id_user)
        usuario.id_user = request.json.get('id_user', usuario.id_user)
        usuario.fk_tipo_user = request.json.get('fk_tipo_user', usuario.fk_tipo_user)
        usuario.nom1_user = request.json.get('nom1_user', usuario.nom1_user)
        usuario.nom2_user = request.json.get('nom2_user', usuario.nom2_user)
        usuario.ape1_user = request.json.get('ape1_user', usuario.ape1_user)
        usuario.ape2_user = request.json.get('ape2_user', usuario.ape2_user)
        usuario.correo_sena_user = request.json.get('correo_sena_user', usuario.correo_sena_user)
        usuario.contrasena = request.json.get('contrasena', usuario.contrasena)
        usuario.fk_anteced_salud_sel = request.json.get('fk_anteced_salud_sel', usuario.fk_anteced_salud_sel)
        usuario.anteced_salud_inp = request.json.get('anteced_salud_inp', usuario.anteced_salud_inp)
        usuario.estado_user = request.json.get('estado_user', usuario.estado_user)
        db.session.commit()
        return usuarios_schema.dump(usuario)

    # eliminar
    def delete(self, id_usuario):
        usuario = Usuarios.query.get_or_404(id_usuario)
        db.session.delete(usuario)
        db.session.commit()
        return 'Operacion existosa', 204


# Creacion vista anuncios
class VistaAnuncios(Resource):
    def get(self):
        return [anuncios_schema.dump(Anuncios) for Anuncios in Anuncios.query.all()]

    def post(self):
        nuevo_anuncio = Anuncios(fk_id_admin_anunc=request.json['fk_id_admin_anunc'],\
                                titulo_anunc=request.json['titulo_anunc'],\
                                desc_anunc=request.json['desc_anunc'], \
                                img_anunc=request.json['img_anunc'], \
                                estado_anunc=request.json['estado_anunc'])
        db.session.add(nuevo_anuncio)
        db.session.commit()
        return anuncios_schema.dump(nuevo_anuncio)

class VistaAnuncio(Resource):
    def get(self, id_anunc):  # trae una sola cancion
        return anuncios_schema.dump(Anuncios.query.get_or_404(id_anunc))

    #actualizar

    def put(self, id_anunc):
        anuncio = Anuncios.query.get_or_404(id_anunc)
        anuncio.fk_id_admin_anunc = request.json.get('fk_id_admin_anunc', anuncio.fk_id_admin_anunc)
        anuncio.titulo_anunc = request.json.get('titulo_anunc', anuncio.titulo_anunc)
        anuncio.desc_anunc = request.json.get('desc_anunc', anuncio.desc_anunc)
        anuncio.img_anunc = request.json.get('img_anunc', anuncio.img_anunc)
        anuncio.estado_anunc = request.json.get('estado_anunc', anuncio.estado_anunc)
        db.session.commit()
        return anuncios_schema.dump(anuncio)

    # eliminar
    def delete(self, id_anunc):
        anuncio = Anuncios.query.get_or_404(id_anunc)
        db.session.delete(anuncio)
        db.session.commit()
        return 'Operacion existosa', 204


# Creacion vista asistencia
class VistaAsistencias(Resource):
    def get(self):
        return [asistencia_schema.dump(Asistencia) for Asistencia in Asistencia.query.all()]

    def post(self):
        nuevo_registro_asist = Asistencia(id_instruc_asis=request.json['id_instruc_asis'],\
                            fk_id_aprend_asis=request.json['fk_id_aprend_asis'],\
                            fecha_asis=request.json['fecha_asis'], \
                            estado_asis=request.json['estado_asis'])
        db.session.add(nuevo_registro_asist)
        db.session.commit()
        return asistencia_schema.dump(nuevo_registro_asist)

class VistaAsistencia(Resource):
    def get(self, id_registro_asis):
        return asistencia_schema.dump(Asistencia.query.get_or_404(id_registro_asis))

    #actualizar

    def put(self, id_registro_asis):
        asistencia = Asistencia.query.get_or_404(id_registro_asis)
        asistencia.id_instruc_asis = request.json.get('id_instruc_asis', asistencia.id_instruc_asis)
        asistencia.fk_id_aprend_asis = request.json.get('fk_id_aprend_asis', asistencia.fk_id_aprend_asis)
        asistencia.fecha_asis = request.json.get('fecha_asis', asistencia.fecha_asis)
        asistencia.estado_asis = request.json.get('estado_asis', asistencia.estado_asis)
        db.session.commit()
        return asistencia_schema.dump(asistencia)

    # eliminar
    def delete(self, id_registro_asis):
        asistencia = Asistencia.query.get_or_404(id_registro_asis)
        db.session.delete(asistencia)
        db.session.commit()
        return 'Operacion existosa', 204


# Creacion vista musculos
class VistaMusculos(Resource):
    def get(self):
        return [musculos_schema.dump(Musculos) for Musculos in Musculos.query.all()]

class VistaMusculo(Resource):
    def get(self, musculo):
        return musculos_schema.dump(Musculos.query.get_or_404(musculo))


# Creacion vista planificador
class VistaPlanificador(Resource):
    def get(self):
        return [planificador_schema.dump(Planificador) for Planificador in Planificador.query.all()]

    def post(self):
        nuevo_planificador = Planificador(fk_id_aprend=request.json['fk_id_aprend'],\
                            fk_musculo=request.json['fk_musculo'])
        db.session.add(nuevo_planificador)
        db.session.commit()
        return planificador_schema.dump(nuevo_planificador)


# Creacion vista ejercicios
class VistaEjercicios(Resource):
    def get(self):
        return [ejercicios_schema.dump(Ejercicios) for Ejercicios in Ejercicios.query.all()]

class VistaEjercicio(Resource):
    def get(self, ejercicio):
        return ejercicios_schema.dump(Ejercicios.query.get_or_404(ejercicio))


## Clase con ruta adicional, creada con el propósito de listar los ejercicios que le correspondan al músculo pasado por parámetro
class VistaMusculosEjercicios(Resource):
    def get(self,musculos):
        musc = Musculos.query.get(musculos)
        ejercici = musc.ejercicios

        lista_ejerc_titulo = [ {e.ejercicio:e.imagen_ejerc} for e in ejercici ]

        return {'lista_ejerc_titulo':lista_ejerc_titulo}