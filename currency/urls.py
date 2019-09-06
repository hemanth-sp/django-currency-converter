from django.urls import path

from currency import views

urlpatterns = [
    path('', views.convert_currency, name='convert_currency'),
]