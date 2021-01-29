from django.db import models


class Company(models.Model):
    name = models.CharField('организация', max_length=50, unique=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Организация'


class Account(models.Model):
    name = models.CharField('счет', max_length=50, db_index=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='account', verbose_name='организация')
    currency = models.CharField('валюта счета', max_length=5, db_index=True)

    def __str__(self):
        return f"{self.company} {self.name} {self.currency}"

    class Meta:
        verbose_name_plural = 'Вид счета'


class Flow(models.Model):
    date = models.DateField('дата', db_index=True)
    inflow = models.DecimalField('поступление', max_digits=9, decimal_places=2, db_index=True)
    outflow = models.DecimalField('списание', max_digits=9, decimal_places=2, db_index=True)
    balance = models.DecimalField('баланс', max_digits=9, decimal_places=2, db_index=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='flow', verbose_name='вид счета')

    def __str__(self):
        return str(self.date)

    class Meta:
        verbose_name_plural = 'Движение средств'
