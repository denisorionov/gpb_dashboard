import datetime

from django import forms
from django.forms import SelectDateWidget


class DateForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control pull-right', 'data-date-format': "mm/dd/yyyy", 'id': 'date'}))
