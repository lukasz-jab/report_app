from django.urls import path
from .views import (
    home_view,
    SalesView,
    SalesDetailView,
    UploadTemplateView,
    csv_upload_view,
)

app_name = 'sales'

urlpatterns = [
    path('', home_view, name='home'),
    path('sales/', SalesView.as_view(), name='list'),
    path('detail/<pk>/', SalesDetailView.as_view(), name='detail'),
    path('from-file/', UploadTemplateView.as_view(), name='from-file'),
    path('upload/', csv_upload_view, name='upload'),

]
