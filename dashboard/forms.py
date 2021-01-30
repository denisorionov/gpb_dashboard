import datetime

from django import forms
from django.forms import SelectDateWidget


class DateForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}))
