from django.urls import path
from .views import (
    create_report_view,
    ReportListView,
    ReportDetailView,
    render_pdf_view,
)

app_name = 'reports'

urlpatterns = [
    path('save/', create_report_view, name='save-report'),
    path('<pk>/', ReportDetailView.as_view(), name='report'),
    path('', ReportListView.as_view(), name = 'reports'),
    path('<pk>/pdf/', render_pdf_view, name = 'pdf'),
]
