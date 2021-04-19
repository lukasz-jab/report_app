from django.urls import path
from .views import (
    home_view,
    SalesView,
    SalesDetailView,
)

app_name = 'sales'

urlpatterns = [
    path('', home_view, name='home'),
    path('sales/', SalesView.as_view(), name='list'),
    path('detail/<pk>/', SalesDetailView.as_view(), name='detail'),

]
