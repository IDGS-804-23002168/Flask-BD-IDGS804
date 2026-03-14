from models import Alumnos
from . import alumnos
from flask import Flask, render_template, request,redirect,url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask import g
import forms
from flask_migrate import Migrate
from alumnos.routes import alumnos, alumnos
from models import db
from models import Alumnos


# LISTADO
@alumnos.route("/alumnos", methods=['GET','POST'])
@alumnos.route("/alumnos/index")
def index():
     create_form=forms.UserForm(request.form)
      #tem= Alumnos.query('select *from alumnos)
     alumno=Alumnos.query.all()
     return render_template("alumnos/index.html", form=create_form, alumno=alumno)
    
    
# @app.route("/", methods=['GET', 'POST'])
# @app.route("/index")
# def index():
#     create_form=forms.UserForm(request.form)
#      #tem= Alumnos.query('select *from alumnos)
#     alumno=Alumnos.query.all()
#     return render_template("index.html", form=create_form, alumno=alumno)

# CREAR
# @alumnos.route("/alumnos/crear", methods=['GET','POST'])
# def crear():
#     form = forms.UserForm()

#     if request.method == 'POST' and form.validate():

#         alumno = Alumnos(
#             id=form.id.data,
#             nombre=form.nombre.data,
#             apellidos=form.apellidos.data,
#             email=form.email.data,
#             telefono=form.telefono.data
#         )

#         db.session.add(alumno)
#         db.session.commit()

#         return redirect(url_for('alumnos.index'))

#     return render_template("alumnos/Alumno.html", form=form)


@alumnos.route("/alumnos/crear", methods=['GET','POST'])
def crear():
    create_form=forms.UserForm(request.form)
    if request.method == 'POST' and create_form.validate():
    # if request.method=='POST':
        alum=Alumnos(nombre=create_form.nombre.data,
                     apellidos=create_form.apellidos.data,
                     email=create_form.email.data,
                     telefono=create_form.telefono.data)
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('alumnos.index'))
    
    return render_template("alumnos/Alumno.html", form=create_form)


# DETALLES
# @alumnos.route("/alumnos/detalles/<int:id>")
# def detalles(id):

#     alumno = Alumnos.query.get_or_404(id)

#     return render_template(
#         "alumnos/detalles.html",
#         alumno=alumno
#     )
    
@alumnos.route("/alumnos/detalles", methods=['GET', 'POST'])
def detalles():
    create_form=forms.UserForm(request.form)
    if request.method=='GET':
        id=request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id==id).first()
        id=request.args.get('id')
        nombre=alum1.nombre
        apellidos=alum1.apellidos
        email=alum1.email
        telefono=alum1.telefono
    
    return render_template('alumnos/detalles.html', id=id, nombre=nombre, apellidos=apellidos, email=email, telefono=telefono, form=create_form)


# EDITAR
@alumnos.route("/alumnos/editar/<int:id>", methods=['GET','POST'])
def editar(id):

    alumno = Alumnos.query.get_or_404(id)

    form = forms.UserForm(obj=alumno)

    if request.method == 'POST' and form.validate():

        alumno.id = form.id.data
        alumno.nombre = form.nombre.data
        alumno.apellidos = form.apellidos.data
        alumno.email = form.email.data
        alumno.telefono = form.telefono.data

        db.session.commit()

        return redirect(url_for('alumnos.index'))

    return render_template("alumnos/modificar.html", form=form)


# ELIMINAR
@alumnos.route("/alumnos/eliminar/<int:id>", methods=['GET','POST'])
def eliminar(id):

    alumno = Alumnos.query.get_or_404(id)

    form = forms.UserForm(obj=alumno)

    if request.method == 'POST':

        db.session.delete(alumno)
        db.session.commit()

        return redirect(url_for('alumnos.index'))

    return render_template("alumnos/eliminar.html", form=form)