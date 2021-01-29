from django import forms

from dashboard.models import Flow


class FlowForm(forms.ModelForm):

    class Meta:
        model = Flow
        fields = ('date',)

        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control'})
        }
