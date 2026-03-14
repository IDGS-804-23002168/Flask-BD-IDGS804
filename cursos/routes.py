from . import cursos
from flask import render_template, request, redirect, url_for
from models import db, Curso, Maestros, Alumnos, Inscripcion
import forms


# LISTADO DE CURSOS
@cursos.route("/cursos")
def index():

    cursos_list = Curso.query.all()

    return render_template(
        "cursos/listado.html",
        cursos=cursos_list
    )


# CREAR CURSO
@cursos.route("/cursos/crear", methods=["GET","POST"])
def crear():

    form = forms.CursoForm()

    maestros = Maestros.query.all()
    form.maestro_id.choices = [
        (m.matricula, m.nombre + " " + m.apellidos)
        for m in maestros
    ]

    if request.method == "POST" and form.validate():

        curso = Curso(
            nombre=form.nombre.data,
            descripcion=form.descripcion.data,
            maestro_id=form.maestro_id.data
        )

        db.session.add(curso)
        db.session.commit()

        return redirect(url_for("cursos.index"))

    return render_template(
        "cursos/crear.html",
        form=form
    )


# DETALLES
@cursos.route("/cursos/detalles/<int:id>")
def detalles(id):

    curso = Curso.query.get_or_404(id)

    return render_template(
        "cursos/detalles.html",
        curso=curso
    )




# ELIMINAR CURSO
@cursos.route("/cursos/eliminar/<int:id>", methods=["GET", "POST"])
def eliminar(id):

    curso = Curso.query.get_or_404(id)

    if request.method == "POST":

        db.session.delete(curso)
        db.session.commit()

        return redirect(url_for("cursos.index"))

    return render_template(
        "cursos/eliminar.html",
        curso=curso
    )
    
    
    # EDITAR CURSO
@cursos.route("/cursos/editar/<int:id>", methods=["GET", "POST"])
def editar(id):

    curso = Curso.query.get_or_404(id)

    curso_form = forms.CursoForm(obj=curso)
    inscripcion_form = forms.InscripcionForm()

    maestros = Maestros.query.all()

    curso_form.maestro_id.choices = [
        (m.matricula, m.nombre + " " + m.apellidos)
        for m in maestros
    ]

    alumnos = Alumnos.query.all()

    inscripcion_form.alumnos.choices = [
        (a.id, a.nombre + " " + a.apellidos)
        for a in alumnos
    ]

    # alumnos actualmente inscritos
    alumnos_actuales = [a.id for a in curso.alumnos]

    if request.method == "GET":
        inscripcion_form.alumnos.data = alumnos_actuales

    if request.method == "POST":

        if curso_form.validate():

            # actualizar datos del curso
            curso.nombre = curso_form.nombre.data
            curso.descripcion = curso_form.descripcion.data
            curso.maestro_id = curso_form.maestro_id.data

            # alumnos seleccionados
            nuevos_alumnos = inscripcion_form.alumnos.data

            # eliminar inscripciones que ya no estén
            Inscripcion.query.filter_by(curso_id=id)\
                .filter(~Inscripcion.alumno_id.in_(nuevos_alumnos))\
                .delete(synchronize_session=False)

            # agregar nuevas
            existentes = {
                i.alumno_id
                for i in Inscripcion.query.filter_by(curso_id=id).all()
            }

            for alumno_id in nuevos_alumnos:
                if alumno_id not in existentes:
                    db.session.add(
                        Inscripcion(
                            alumno_id=alumno_id,
                            curso_id=id
                        )
                    )

            db.session.commit()

            return redirect(url_for("cursos.detalles", id=id))

    return render_template(
        "cursos/editar.html",
        curso=curso,
        curso_form=curso_form,
        inscripcion_form=inscripcion_form
    )