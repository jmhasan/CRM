import datetime

from django import forms
from django.forms import ModelForm
from wtforms import Form, TextField, StringField
from wtforms.validators import DataRequired, Length

from accounts.models import Ritarget, Matching, advnum, Prmst
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
#from wtforms import Form, BooleanField, StringField, validators, DateTimeField, TextAreaField, IntegerField

TITLE_CHOICES = (
    ('MR', '0222.'),
    ('MRS', '4545.'),
    ('MS', '456654.'),
)

#house = forms.ModelChoiceField(queryset=House.objects.all(), initial=0)
class RitargetForm(forms.ModelForm):
    xrow=forms.CharField(label='Transction No',widget=forms.TextInput(attrs={'class':'form-control','readonly': 'readonly'}), required=True, max_length=100, initial=advnum)
    xriid=forms.CharField(widget=forms.Select(choices=TITLE_CHOICES,attrs={'class':'form-control','placeholder':'000001'}),required=True,max_length=100)
    xtsoid=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'000001'}),required=True)
    xziid=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'000001'}),required=True,max_length=100)

    #favorite_fruit = forms.CharField(label='naee', widget=forms.Select(choices=TITLE_CHOICES))
    class Meta:
        # Model I want to interact
        model = Ritarget
        # Filed i want to show according to serial
        fields = ['xrow','xriid','xtsoid', 'xziid','xqty']
        labels = {
            'xrow': 'Transaction No', 'xriid': 'RI Code', 'xtsoid':'AI Code' , 'xziid': 'ZI Code',
            'xqty' : 'Target Qty'
        }
        widgets = {
            'xrow': forms.TextInput(attrs={'readonly': 'readonly'}),
        }





class MatchingForm(Form):
    matchnum = StringField(validators=[DataRequired(), Length(max=100)])
    xrow = StringField(validators=[DataRequired(), Length(max=255)])


