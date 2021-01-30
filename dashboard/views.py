from datetime import datetime

from django.db.models import Sum
from django.shortcuts import render

from dashboard.forms import DateForm
from dashboard.models import Flow, Company, Currency


def main_view(request):
    if request.method == 'GET':
        date_form = DateForm()
        date = datetime.strptime('01.09.2020', '%d.%m.%Y')

    if request.method == 'POST':
        date_form = DateForm(request.POST)
        if date_form.is_valid():
            date = date_form.cleaned_data['date']

    companies = Company.objects.all()
    currencies = Currency.objects.filter(account__flow__date=date).annotate(total_balance=Sum('account__flow__balance'))
    flows = Flow.objects.filter(date=date)

    return render(request, 'dashboard/index.html',
                  context={'form': date_form, 'companies': companies, 'flows': flows, 'currencies': currencies,
                           'date': date.strftime('%d.%m.%Y')})
