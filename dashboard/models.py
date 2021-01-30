from django.db import models


class Company(models.Model):
    name = models.CharField('организация', max_length=50, unique=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Организация'


class Currency(models.Model):
    name = models.CharField('вид счета', max_length=5, db_index=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='currency', verbose_name='организация')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Вид счета'


class Account(models.Model):
    name = models.CharField('счет', max_length=50, db_index=True)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='account', verbose_name='валюта счета')

    def __str__(self):
        return f"{self.currency.company} {self.name} {self.currency}"

    class Meta:
        verbose_name_plural = 'Cчет'


class Flow(models.Model):
    date = models.DateField('дата', db_index=True)
    inflow = models.DecimalField('поступление', max_digits=9, decimal_places=2, db_index=True)
    outflow = models.DecimalField('списание', max_digits=9, decimal_places=2, db_index=True)
    balance = models.DecimalField('баланс', max_digits=9, decimal_places=2, db_index=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='flow', verbose_name='вид счета')
    week = models.IntegerField('неделя')
    month = models.CharField('месяц', max_length=3, db_index=True)
    year = models.IntegerField('год')

    def __str__(self):
        return str(self.date)

    class Meta:
        verbose_name_plural = 'Движение средств'
