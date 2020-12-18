from django.contrib import admin

from ledger.models import (
    Person, Contact, Month, Savings, Credit, RePayment
)


class PersonAdmin(admin.ModelAdmin):
    pass


class ContactAdmin(admin.ModelAdmin):
    pass


class MonthAdmin(admin.ModelAdmin):
    pass


class SavingsAdmin(admin.ModelAdmin):
    pass


class CreditAdmin(admin.ModelAdmin):
    pass


class RePaymentAdmin(admin.ModelAdmin):
    pass




admin.site.register(Person, PersonAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Month, MonthAdmin)
admin.site.register(Savings, SavingsAdmin)
admin.site.register(Credit, CreditAdmin)
admin.site.register(RePayment, RePaymentAdmin)
