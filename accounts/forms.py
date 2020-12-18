import datetime

from django import forms
from django.forms import ModelForm
from wtforms import Form, TextField, StringField
from wtforms.validators import DataRequired, Length

from accounts.models import Ritarget, Matching, advnum
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
#from wtforms import Form, BooleanField, StringField, validators, DateTimeField, TextAreaField, IntegerField



class RitargetForm(forms.ModelForm):
    xrow=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Transaction'}),required=True,max_length=100,initial=advnum)
    xriid=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'000001'}),required=True,max_length=100)
    xtsoid=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'000001'}),required=True,max_length=100)
    xziid=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'000001'}),required=True,max_length=100)

    class Meta:
        # Model I want to interact
        model = Ritarget
        # Filed i want to show according to serial
        fields = ['xrow','xriid','xtsoid', 'xziid']
        labels = {
            'xrow': 'ID','xriid': 'RI Code','xtsoid':'AI Code' , 'xziid': 'ZI Code'
        }


class MatchingForm(Form):
    matchnum = StringField(validators=[DataRequired(), Length(max=100)])
    xrow = StringField(validators=[DataRequired(), Length(max=255)])


