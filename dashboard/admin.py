from django.contrib import admin

from dashboard.models import Company, Flow, Account, Currency


class AccountItemInline(admin.TabularInline):
    model = Account
    extra = 0
    fields = ['name', 'currency']


class CurrencyItemInline(admin.TabularInline):
    model = Currency
    extra = 0
    fields = ['name']


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    inlines = [CurrencyItemInline]


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    inlines = [AccountItemInline]
    list_display = ['name']
    list_display_links = ['name']


class FlowItemInline(admin.TabularInline):
    model = Flow
    extra = 0
    fields = ['date', 'inflow', 'outflow', 'balance']


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    inlines = [FlowItemInline]


@admin.register(Flow)
class FlowAdmin(admin.ModelAdmin):
    list_display = ['date', 'account', 'inflow', 'outflow', 'balance']
    list_display_links = ['account', 'date']


