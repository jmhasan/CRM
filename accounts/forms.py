from django import forms
from django.forms import ModelForm
from wtforms import Form, TextField, StringField
from wtforms.validators import DataRequired, Length

from accounts.models import Ritarget, Matching
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
#from wtforms import Form, BooleanField, StringField, validators, DateTimeField, TextAreaField, IntegerField


class RitargetForm(forms.ModelForm):

    class Meta:
        # Model I want to interact
        model = Ritarget
        # Filed i want to show according to serial
        fields = ['xrow','xriid','xtsoid', 'xziid','xqty']
        labels = {
            'xrow': 'ID','xriid': 'RI Code','xtsoid':'AI Code' , 'xziid': 'ZI Code',
            'xqty' : 'Target Qty'
        }


class MatchingForm(Form):
    matchnum = StringField(validators=[DataRequired(), Length(max=100)])
    xrow = StringField(validators=[DataRequired(), Length(max=255)])

