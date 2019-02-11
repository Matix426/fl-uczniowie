# -*- coding: utf-8 -*-
# quiz-orm/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, HiddenField, FieldList
from wtforms import SelectField, FormField, BooleanField
from wtforms.validators import Required

blad1 = 'To pole jest wymagane'


class KlasaForm(FlaskForm):
    id = HiddenField()
    klasa = CharFieldField('Klasa: ', validators=[Required(message=blad1)])
    rok_naboru = IntegerField()
    rok_matury = IntegerField()


class UczenForm(FlaskForm):
    imie = CharField()
    nazwisko = CharField()
    plec = IntegerField()
