import json
from datetime import datetime

from django.db.models import Sum
from django.shortcuts import render

from dashboard.forms import DateForm
from dashboard.models import Flow, Company, Currency, Account


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

    date_from = datetime.strptime('01.09.2020', '%d.%m.%Y')
    date_end = datetime.strptime('07.09.2020', '%d.%m.%Y')
    date_list = [date.strftime('%d.%m.%Y') for date in sorted(list(set([flow.date for flow in Flow.objects.filter(date__gte=date_from, date__lte=date_end)])))]
    datasets = []
    charts_data = {}

    for company in companies:
        color = ['blue', 'green', 'yellow', 'red']
        for account in Account.objects.filter(currency__name="RUB").filter(currency__company__name=company.name):
            inflow_list = [int(flow.inflow) for flow in
                    Flow.objects.filter(account=account).filter(date__gte=date_from, date__lte=date_end)]
            datasets.append(
                {
                    'label': account.name,
                    'backgroundColor': 'transparent',
                    'borderColor': color.pop(),
                    'data': inflow_list,
                }
            )

        chart_data = {
            'labels': date_list,
            'datasets': datasets,
        }

        if company.name == "ЭТП_ГПБ":
            charts_data["ETP_GPB"] = json.dumps(chart_data, ensure_ascii=False)
        if company.name == "Консалтинг_ГПБ":
            charts_data["Consalting_GPB"] = json.dumps(chart_data, ensure_ascii=False)
        if company.name == "Юр лицо":
            charts_data["LTD"] = json.dumps(chart_data, ensure_ascii=False)
        datasets = []

    return render(request, 'dashboard/index.html',
                  context={'form': date_form, 'companies': companies, 'flows': flows, 'currencies': currencies,
                           'date': date.strftime('%d.%m.%Y'), 'charts_data': charts_data})
