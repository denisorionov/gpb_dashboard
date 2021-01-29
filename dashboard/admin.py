from django.contrib import admin

from dashboard.models import Company, Flow, Account


class AccountItemInline(admin.TabularInline):
    model = Account
    extra = 0
    fields = ['name', 'currency']


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    inlines = [AccountItemInline]


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

