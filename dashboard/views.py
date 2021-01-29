from django.shortcuts import render
from django.views import View

from dashboard.forms import FlowForm
from dashboard.models import Flow


class MainView(View):
    def get(self, request):
        date_form = FlowForm()
        return render(request, 'dashboard/index.html', context={'form': date_form})

    def post(self, request, *args, **kwargs):
        date_form = FlowForm()
        if date_form.is_valid():
            date = date_form.cleaned_data['date']

            flow = Flow.objects.filter(date=date)
            return render(request, 'adminlte/index.html', context={'flow': flow, 'form': date_form})
        return render(request, 'adminlte/index.html')

