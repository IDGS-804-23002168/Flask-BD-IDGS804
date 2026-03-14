from wtforms import Form, StringField, DateField, IntegerField, EmailField, validators, TextAreaField, SelectField, SelectMultipleField
from flask_wtf import FlaskForm
 
class UserForm(FlaskForm):
    id = IntegerField('id')
   
    nombre = StringField('nombre',[
        validators.DataRequired(message='El nombre es requerido'),
        validators.length(min=4, max=20, message='requiere minimo 4, maximo 20')
    ])
   
    apellidos = StringField('apellidos',[
        validators.DataRequired(message='El apellido es requerido')
    ])
   
    email = EmailField('correo',[
        validators.DataRequired(message='El correo es requerido'),
        validators.Email(message='Ingrese un correo valido')
    ])
    
    telefono = StringField('telefono',[
        validators.DataRequired(message='El telefono es requerido')
    ])
    
class UserForm2(FlaskForm):

    id = IntegerField('id')

    nombre = StringField('nombre')
    apellidos = StringField('apellidos')
    email = EmailField('correo')
    telefono = EmailField('telefono')
    
    
class MaestroForm(FlaskForm):
    matricula = IntegerField('Matrícula', [validators.DataRequired(message='La Matricula es requerida')])
    nombre = StringField('Nombre', [validators.DataRequired(message='El Nombre es requerido')])
    apellidos = StringField('Apellidos', [validators.DataRequired(message='Los Apellidos es requerido')])
    especialidad = StringField('Especialidad', [validators.DataRequired(message='La Especialidad es requerido')])
    email = StringField('Email', [validators.DataRequired(message='El correo electrónico es obligatorio'), validators.Email(message='El correo es requerido')])
    

class CursoForm(FlaskForm):

    nombre = StringField(
        "Nombre",
        [validators.DataRequired(message='El nombre es obligatorio')]
    )

    descripcion = TextAreaField(
        "Descripción"
    )

    maestro_id = SelectField(
        "Maestro",
        coerce=int
    )


class InscripcionForm(FlaskForm):

    alumnos = SelectMultipleField(
        "Alumnos",
        coerce=int
    )