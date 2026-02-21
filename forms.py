from wtforms import Form, StringField, DateField, IntegerField, EmailField,validators
from flask_wtf import FlaskForm
 
class UserForm(Form):
    id = IntegerField('id',[
        validators.number_range(min=1, max=20, message='valor no valido')
    ])
   
    nombre = StringField('nombre',[
        validators.DataRequired(message='El nombre es requerido'),
        validators.length(min=4, max=20, message='requiere minimo 4, maximo 20')
    ])
   
    apaterno = StringField('apaterno',[
        validators.DataRequired(message='El apellido es requerido')
    ])
   
    email = EmailField('correo',[
        validators.DataRequired(message='El correo es requerido'),
        validators.Email(message='Ingrese un correo valido')
    ])