from django.urls import path
from .views import HomePageView, SavingsCreateView, CreditCreateView, RePaymentCreateView, UserListView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('savings', SavingsCreateView.as_view(), name='savings-create'),
    path('credit', CreditCreateView.as_view(), name='credit-create'),
    path('re-payment', RePaymentCreateView.as_view(), name='re-payment-create'),
    path('account-statement', HomePageView.as_view(), name='home-x'),
    path('users', UserListView.as_view(), name='users-list')
]
