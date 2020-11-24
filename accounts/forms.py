from django import forms

from accounts.models import Ritarget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit



class RitargetForm(forms.ModelForm):

    class Meta:
        # Model I want to interact
        model = Ritarget
        # Filed i want to show according to serial
        fields = ['xrow','xriid','xtsoid', 'xziid']
        labels = {
            'xrow': 'ID','xriid': 'RI Code','xtsoid':'AI Code' , 'xziid': 'ZI Code'
        }
