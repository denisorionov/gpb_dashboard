import csv
from datetime import datetime

from django.core.management.base import BaseCommand

from dashboard.models import Company, Account, Flow, Currency


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('csv_file', nargs='+', type=str)

    def handle(self, *args, **options):
        for csv_file in options['csv_file']:
            data_reader = csv.reader(open(csv_file), delimiter=',', quotechar='"')
            for row in data_reader:
                if row[0] == 'id':
                    continue
                new_company, com_created = Company.objects.get_or_create(name=row[1])
                new_currency, cur_created = Currency.objects.get_or_create(name=row[3], company=new_company)
                new_account, acc_created = Account.objects.get_or_create(name=row[2], currency=new_currency)
                Flow.objects.create(
                    date=datetime.strptime(row[4], '%d.%m.%Y'),
                    inflow=row[8],
                    outflow=row[9],
                    balance=row[7],
                    account=new_account,
                    week=row[10],
                    month=row[11],
                    year=row[12]
                )

        print("Data loaded")
