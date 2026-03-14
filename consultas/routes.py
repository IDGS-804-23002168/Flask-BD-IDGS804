from flask import render_template, request
from . import consultas
from models import Alumnos, Curso


@consultas.route("/consultas", methods=["GET","POST"])
def index():

    alumnos = Alumnos.query.all()
    cursos = Curso.query.all()

    alumno = None
    cursos_alumno = None

    curso = None
    alumnos_curso = None

    if request.method == "POST":

        alumno_id = request.form.get("alumno_id")
        curso_id = request.form.get("curso_id")

        if alumno_id:

            alumno = Alumnos.query.get(alumno_id)
            cursos_alumno = alumno.cursos

        elif curso_id:

            curso = Curso.query.get(curso_id)
            alumnos_curso = curso.alumnos

    return render_template(
        "consultas/index.html",
        alumnos=alumnos,
        cursos=cursos,
        alumno=alumno,
        cursos_alumno=cursos_alumno,
        curso=curso,
        alumnos_curso=alumnos_curso
    )
    
    
@consultas.route("/consultas/alumnos", methods=["GET","POST"])
def alumnos():

    alumnos = Alumnos.query.all()
    cursos = Curso.query.all()

    alumno = None
    cursos_alumno = None

    curso = None
    alumnos_curso = None

    if request.method == "POST":

        alumno_id = request.form.get("alumno_id")
        curso_id = request.form.get("curso_id")

        if alumno_id:

            alumno = Alumnos.query.get(alumno_id)
            cursos_alumno = alumno.cursos

        elif curso_id:

            curso = Curso.query.get(curso_id)
            alumnos_curso = curso.alumnos

    return render_template(
        "consultas/alumnos.html",
        alumnos=alumnos,
        cursos=cursos,
        alumno=alumno,
        cursos_alumno=cursos_alumno,
        curso=curso,
        alumnos_curso=alumnos_curso
    )