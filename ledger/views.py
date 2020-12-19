from django.views.generic.base import TemplateView
from django.views.generic import CreateView, ListView
from .models import Savings, Credit, RePayment, Person
from django.db.models import Sum

class ContextMixin:
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data()
        ctx['total_savings'] = Savings.objects.all().count()
        ctx['navbar_title'] = 'Bachat'
        ctx['site_url'] = 'https://asperoph.com'
        ctx['nav_items'] = [
            {
                'title': 'Users',
                'url': '/users'
            },
            {
                'title': 'Savings',
                'url': '/savings'
            },
            {
                'title': 'Credit',
                'url': '/credit'
            },
            {
                'title': 'RePayment',
                'url': '/re-payment'
            },
            {
                'title': 'Account Statement',
                'url': '/account-statement'
            },
            
        ]
        return ctx


class HomePageView(ContextMixin, TemplateView):
    template_name = "home.html"

    def get_charts_info(self):
        return [
            {
                'title': 'Total Savings',
                'number': Savings.objects.count(),
            },
            {
                'title': 'To Pay Credits',
                'number': Credit.objects.count(),
            },
            {
                'title': 'Total Repayment',
                'number': RePayment.objects.count(),
            },
        ]

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data()
        ctx['charts_info'] = self.get_charts_info()
        return ctx


# from django import forms

# class NameForm(forms.Form):
#     your_name = forms.CharField(label='Your name', max_length=100)


class TableHeaderMixin:
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data()
        ctx['headers'] = [f.name.title() for f in self.model._meta.fields]
        print(ctx)
        return ctx



class SavingsCreateView(TableHeaderMixin, ListView):
    template_name = 'create-savings.html'
    model = Savings
    fields = '__all__'


class CreditCreateView(TableHeaderMixin, ListView):
    template_name = 'create-savings.html'
    model = Credit
    fields = '__all__'


class RePaymentCreateView(TableHeaderMixin, ListView):
    template_name = 'create-savings.html'
    model = RePayment
    fields = '__all__'


class UserListView(TableHeaderMixin, ListView):
    template_name = 'user-list.html'
    model = Person

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data()
        objl = []
        for obj in ctx['object_list']:
            obj.total_savings = Savings.objects.filter(person__consumer_id=obj.id).aggregate(
                total_savings=Sum('amount')
            ).get('total_savings')
            print(obj.total_savings)
            objl.append(obj)
        ctx['object_list'] = objl
        return ctx
